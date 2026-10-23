from datetime import datetime, timedelta
from dataclasses import dataclass, field
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent
STATIONS_FILE = BASE_DIR / "stations.txt"


@dataclass(eq=False)
class Station:
    """A station and the visits currently assigned to it."""

    id: int
    abbrev: str
    name: str
    code: str
    km: float | None
    platforms: frozenset = field(default_factory=frozenset)
    visits: list = field(default_factory=list, repr=False)

    def __getitem__(self, key):
        """Provide compatibility with the former station dictionaries."""
        return getattr(self, key)

    def add_visit(self, visit):
        if visit not in self.visits:
            self.visits.append(visit)

    def remove_visit(self, visit):
        if visit in self.visits:
            self.visits.remove(visit)

    def departures(self):
        """Return visits with a departure time, ordered by departure."""
        return sorted(
            (visit for visit in self.visits if visit.departure is not None),
            key=lambda visit: visit.departure,
        )


@dataclass(eq=False)
class Visit:
    """A train's scheduled visit at a station."""

    station: Station
    arrival: str | None = None
    departure: str | None = None
    platform: int | str = "any"
    train: object = field(default=None, repr=False)

    @property
    def is_through_run(self):
        return (
            self.arrival is not None
            and self.departure is not None
            and self.arrival == self.departure
        )

    @property
    def is_stop(self):
        return self.departure is not None and not self.is_through_run

    def __getitem__(self, key):
        """Provide compatibility with the former stop dictionaries."""
        if key == "station_id":
            return self.station.id
        if key == "platform":
            return self.platform
        return getattr(self, key)


def parse_station_file(file):
    """Load stations from ``abbrev|name|code|km[|platforms]`` records."""
    stations = {}
    codes = {}
    with open(file, "r", encoding="utf-8") as station_file:
        for line_number, line in enumerate(station_file, start=1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            parts = [part.strip() for part in line.split("|")]
            if len(parts) not in {4, 5}:
                raise ValueError(
                    f"Invalid station record in {file}:{line_number}; "
                    "expected abbrev|name|code|km[|platforms]"
                )

            abbrev, name, code, km_text = parts[:4]
            platform_text = parts[4] if len(parts) == 5 else ""
            if not abbrev or not name or not code:
                raise ValueError(
                    f"Invalid station record in {file}:{line_number}; "
                    "abbreviation, name and code are required"
                )
            try:
                km = None if km_text in {"", "X"} else float(km_text)
            except ValueError as error:
                raise ValueError(
                    f"Invalid kilometre value in {file}:{line_number}: {km_text!r}"
                ) from error

            platforms = frozenset(
                int(platform.strip())
                for platform in platform_text.split(",")
                if platform.strip()
            )
            station_id = len(stations) + 1
            station = Station(station_id, abbrev, name, code, km, platforms)
            stations[station_id] = station
            codes.setdefault(code, []).append(station_id)

    if not stations:
        raise ValueError(f"No stations found in {file}")
    return stations


STATIONS = parse_station_file(STATIONS_FILE)
STATION_CODE_TO_IDS = {}
for _station_id, _station in STATIONS.items():
    STATION_CODE_TO_IDS.setdefault(_station.code, []).append(_station_id)


def station_code_to_id(code):
    """Return the station ID for a station code."""
    station_ids = STATION_CODE_TO_IDS.get(code, [])
    if len(station_ids) == 1:
        return station_ids[0]
    if len(station_ids) > 1:
        raise ValueError(f"Ambiguous station code: {code}")
    raise ValueError(f"Unknown station code: {code}")


class Car:
    """One vehicle in a train composition."""

    TYPES = frozenset({"L", "P", "C"})

    def __init__(self, car_type):
        if car_type not in self.TYPES:
            raise ValueError(
                f"Unknown car type {car_type!r}; expected one of "
                f"{', '.join(sorted(self.TYPES))}"
            )
        self.type = car_type

    def __repr__(self):
        return f"Car({self.type!r})"


class Train:
    """A train with vehicles and scheduled station stops."""

    def __init__(
        self,
        train_id,
        name,
        composition="LPL",
        train_type="REGIONAL",
        max_speed_kmph=100,
        flags="X1",
    ):
        if not train_id:
            raise ValueError("A train ID is required")
        if not name:
            raise ValueError("A train name is required")
        self.id = str(train_id)
        self.name = name
        self.train_type = train_type
        self.max_speed_kmph = max_speed_kmph
        self.flags = flags
        self.composition = composition
        self.cars = [Car(car_type) for car_type in composition]
        self.visits = []
        self.stops = self.visits
        self._legs = []
        self._leg_parent = None
        self._leg_index = None

    @staticmethod
    def _station(station):
        if isinstance(station, Station):
            return station
        if isinstance(station, str):
            station_ids = STATION_CODE_TO_IDS.get(station, [])
            if len(station_ids) == 1:
                return STATIONS[station_ids[0]]
        try:
            return STATIONS[station]
        except (KeyError, TypeError) as error:
            raise ValueError(f"Unknown station: {station}") from error

    @staticmethod
    def _validate_platform(station, platform):
        platform = "any" if platform is None else platform
        if platform == "":
            raise ValueError("A platform must not be empty")
        if platform != "any" and station.platforms and platform not in station.platforms:
            raise ValueError(
                f"Platform {platform!r} is not available at station {station.code}"
            )
        return platform

    def add_stop(
        self, station_id, arrival=None, departure=None, platform="any"
    ):
        """Append a stop and return this train for fluent construction."""
        station = self._station(station_id)
        platform = self._validate_platform(station, platform)
        visit = Visit(station, arrival, departure, platform, self)
        self.visits.append(visit)
        station.add_visit(visit)
        return self

    @staticmethod
    def _parse_time(value):
        if value is None:
            return None
        for time_format in ("%H:%M:%S", "%H:%M"):
            try:
                return datetime.strptime(value, time_format)
            except ValueError:
                continue
        raise ValueError(f"Invalid time {value!r}; expected HH:MM or HH:MM:SS")

    @staticmethod
    def _format_time(value, with_seconds=False):
        return value.strftime("%H:%M:%S" if with_seconds else "%H:%M")

    @staticmethod
    def _shift_time(value, delta):
        parsed = Train._parse_time(value)
        return None if parsed is None else Train._format_time(parsed + delta)

    def _shift_visits(self, delta):
        for visit in self.visits:
            visit.arrival = self._shift_time(visit.arrival, delta)
            visit.departure = self._shift_time(visit.departure, delta)

    def set_origin(self, station, travel_time, stopping=False, platform="any"):
        """Add a passing or stopping origin before the current first visit."""
        
        if not isinstance(travel_time, int) or isinstance(travel_time, bool) or travel_time < 0:
            raise ValueError("Travel time must be a non-negative integer")
        if not self.visits or self.visits[0].arrival is not None:
            raise ValueError("The train must have an open origin")

        first = self.visits[0]
        first_departure = self._parse_time(first.departure)
        if first_departure is None:
            raise ValueError("The current origin must have a departure time")

        origin_dwell = 1 if stopping else 0
        self._shift_visits(timedelta(minutes=1 + origin_dwell))
        first_arrival = first_departure + timedelta(minutes=origin_dwell)
        first.arrival = self._format_time(first_arrival)
        origin_arrival = first_arrival - timedelta(minutes=travel_time)
        origin_departure = origin_arrival + timedelta(minutes=origin_dwell)

        self.add_stop(
            station,
            self._format_time(origin_arrival),
            self._format_time(origin_departure),
            platform,
        )
        self.visits.insert(0, self.visits.pop())
        return self

    def set_ending(self, station, travel_time, stopping=False, platform="any"):
        """Add a terminal visit after the current last visit."""

        if not isinstance(travel_time, int) or isinstance(travel_time, bool) or travel_time < 0:
            raise ValueError("Travel time must be a non-negative integer")
        if not self.visits or self.visits[-1].departure is not None:
            raise ValueError("The train must have an open ending")

        last = self.visits[-1]
        last_arrival = self._parse_time(last.arrival)

        if last_arrival is None:
            raise ValueError("The current ending must have an arrival time")

        last_departure = last_arrival + timedelta(minutes=1)
        last.departure = self._format_time(last_departure)
        ending_arrival = last_departure + timedelta(minutes=travel_time)
        ending_departure = (ending_arrival + timedelta(minutes=1) if stopping else None)

        self.add_stop(
            station,
            self._format_time(ending_arrival),
            None if ending_departure is None else self._format_time(ending_departure),
            platform,
        )
        return self

    def _resolve_leg(self, leg=None):
        legs = list(self.iter_legs())
        if leg is None:
            if len(legs) != 1:
                raise ValueError("A leg must be specified for a multi-leg train")
            return legs[0]
        if isinstance(leg, str):
            if len(leg) != 1 or not leg.isalpha():
                raise ValueError("Leg must be a single letter or integer")
            index = ord(leg.upper()) - ord("A")
        elif isinstance(leg, int) and not isinstance(leg, bool):
            index = leg - 1
        else:
            raise ValueError("Leg must be a single letter or integer")
        try:
            return legs[index]
        except IndexError as error:
            raise ValueError(f"Unknown leg: {leg!r}") from error

    def insert_stop(self, position, station_id, arrival, departure, platform="any", leg=None):
        """Insert a visit after the one-based ``position`` in a leg."""

        if not isinstance(position, int) or isinstance(position, bool) or position < 0:
            raise ValueError("Position must be a non-negative integer")
        target_leg = self._resolve_leg(leg)

        if position > len(target_leg.visits):
            raise ValueError("Position is outside the timetable")

        station = self._station(station_id)
        platform = self._validate_platform(station, platform)
        self._parse_time(arrival)
        self._parse_time(departure)

        if arrival is None and position != 0:
            raise ValueError("Only the first position may have no arrival")

        if departure is None and position < len(target_leg.visits):
            raise ValueError("Only the final position may have no departure")

        arrival_time = self._parse_time(arrival)
        departure_time = self._parse_time(departure)

        if (arrival_time is not None and departure_time is not None and departure_time < arrival_time):
            raise ValueError("Departure must not be before arrival")

        previous = target_leg.visits[position - 1] if position else None
        following = (target_leg.visits[position] if position < len(target_leg.visits) else None)

        previous_time = self._parse_time(previous.departure or previous.arrival) if previous else None
        following_time = self._parse_time(following.arrival or following.departure) if following else None
        
        first_time = arrival_time or departure_time
        last_time = departure_time or arrival_time

        if previous_time is not None and first_time < previous_time:
            raise ValueError("Inserted stop is before the previous stop")

        if following_time is not None and last_time > following_time:
            raise ValueError("Inserted stop is after the following stop")

        visit = Visit(station, arrival, departure, platform, target_leg)
        target_leg.visits.insert(position, visit)
        station.add_visit(visit)
        return self

    def remove_stop(self, station_id):
        """Remove the first visit at a station and update its station registry."""
        station = self._station(station_id)
        for visit in self.visits:
            if visit.station is station:
                self.visits.remove(visit)
                station.remove_visit(visit)
                return self
        raise ValueError(f"Train {self.id} has no stop at station ID {station.id}")

    def extend_stop(self, station_id, minutes):
        """Adjust a stop's dwell time by shifting its departure."""
        station = self._station(station_id)
        if not isinstance(minutes, int) or isinstance(minutes, bool):
            raise ValueError("Stop extension must be an integer")

        for stop in self.visits:
            if stop.station is station:
                if stop.departure is None:
                    raise ValueError(f"Stop at station {station_id} has no departure time")

                departure = self._parse_time(stop.departure)
                arrival = self._parse_time(stop.arrival)
                adjusted_departure = departure + timedelta(minutes=minutes)
                if arrival is not None and adjusted_departure < arrival:
                    raise ValueError(
                        "Stop extension would create a negative dwell time"
                    )
                stop.departure = self._format_time(adjusted_departure)
                return self

        raise ValueError(f"Train {self.id} has no stop at station ID {station_id}")

    def change_platform(self, station_id, platform):
        """Change the platform assigned to a station stop."""
        station = self._station(station_id)
        platform = self._validate_platform(station, platform)

        for stop in self.visits:
            if stop.station is station:
                stop.platform = platform
                return self

        raise ValueError(f"Train {self.id} has no stop at station ID {station_id}")

    def add_leg(self, train, intermission):
        """Append ``train`` as the next leg of this REG train."""
        if self.train_type not in {"REG", "REGIONAL"}:
            raise ValueError("Only REG trains may have multiple legs")
        if not isinstance(train, Train):
            raise TypeError("A leg must be another Train")
        if train is self or train._leg_parent is not None:
            raise ValueError("The train is already part of a leg chain")
        if not isinstance(intermission, int) or isinstance(intermission, bool) or intermission < 0:
            raise ValueError("Intermission must be a non-negative integer")
        if not self.visits or not train.visits:
            raise ValueError("Both trains must contain visits")

        previous = list(self.iter_legs())[-1]
        previous_from = previous._from_time(previous.visits[-1])
        next_from = train._from_time(train.visits[0])
        delta = (self._parse_time(previous_from)+ timedelta(minutes=intermission)- self._parse_time(next_from))

        train._shift_visits(delta)
        train._leg_parent = self
        self._legs.append(train)
        return self

    def iter_legs(self):
        yield self
        for leg in self._legs:
            yield from leg.iter_legs()

    @staticmethod
    def _from_time(visit):
        return visit.arrival or visit.departure

    def _reporting_number(self, leg_index, total_legs):
        if total_legs == 1:
            return self.name
        return f"{self.name}{chr(ord('A') + leg_index)}"

    def timetable(self):
        """Return a readable timetable, including leg and insertion positions."""

        legs = list(self.iter_legs())
        lines = [f"{self.name} ({self.id})"]

        for index, leg in enumerate(legs):
            if index:
                previous = legs[index - 1]
                gap = (self._parse_time(self._from_time(leg.visits[0]))- self._parse_time(self._from_time(previous.visits[-1]))).total_seconds() // 60
                lines.append(f"\nIntermission: {int(gap)} minutes")

            suffix = "" if len(legs) == 1 else f" - Leg {chr(ord('A') + index)}"
            lines.append(f"\n{self.name}{suffix} ({self.id})")
            lines.append("Pos  Station                         Arrival    Departure  Platform")
            lines.append("-" * 72)
            for position, visit in enumerate(leg.visits, start=1):
                lines.append(f"{position:>3}  {visit.station.name:<31} "
                    f"{visit.arrival or '-':<10} {visit.departure or '-':<10} "
                    f"{visit.platform}"
                )
        return "\n".join(lines)

    @classmethod
    def from_blueprint(
        cls,
        train_id,
        blueprint,
        name,
        start_time,
        composition="",
        train_type="REGIONAL",
        max_speed_kmph=100,
        flags="X1",
    ):
        """Create a train from travel and dwell times in a blueprint.

        ``arrival`` is the travel time from the previous stop's departure and
        ``departure`` is the dwell time at the current stop. The first stop's
        departure is relative to ``start_time``.
        """
        start = datetime.strptime(start_time, "%H:%M")
        train = cls(train_id, name, composition, train_type, max_speed_kmph, flags)

        current_time = start
        for stop in blueprint["stops"]:
            travel_time = stop["arrival"]
            if travel_time is not None:
                current_time += timedelta(minutes=travel_time)
                arrival = current_time.strftime("%H:%M")
            else:
                arrival = None

            dwell_time = stop["departure"]
            if dwell_time is not None:
                departure = (current_time + timedelta(minutes=dwell_time)).strftime("%H:%M")
                current_time += timedelta(minutes=dwell_time)
            else:
                departure = None

            train.add_stop(
                stop["station_id"],
                arrival,
                departure,
                stop.get("platform", "any"),
            )
        return train

def trains_to_dataframe(trains, stations=STATIONS):
    """Flatten structured station/train data for plotting and tabular output."""
    rows = []
    for train in trains:
        legs = list(train.iter_legs())
        for leg_index, leg in enumerate(legs):
            for stop in leg.stops:
                station_id = stop.station.id

                try:
                    station = stations[station_id]
                except KeyError as error:
                    raise ValueError(f"Unknown station ID in train {train.id}: {station_id}") from error

                rows.append({
                    "Train number": (
                        f"{train.name}{chr(ord('A') + leg_index)} ({train.id})"
                        if len(legs) > 1
                        else f"{train.name} ({train.id})"
                    ),
                    "Stop": station.name,
                    "Abbreviation": station.abbrev,
                    "Station code": station.code,
                    "Station ID": station_id,
                    "Km": station.km,
                    "Arrival": stop.arrival,
                    "Departure": stop.departure,
                    "Platform": stop.platform,
                    "Through run": stop.is_through_run,
                })
    return pd.DataFrame(rows)


def create_train(train_id, blueprint, name, start_time, **train_options):
    """Compatibility wrapper for :meth:`Train.from_blueprint`."""
    return Train.from_blueprint(train_id, blueprint, name, start_time, **train_options)

# Compatibility aliases for callers using the earlier naming style.
stationCodeToId = station_code_to_id
train = Train
