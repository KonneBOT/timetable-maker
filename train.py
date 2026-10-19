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

    @staticmethod
    def _station(station):
        if isinstance(station, Station):
            return station
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
        """Extend a stop's dwell time by shifting its departure later."""
        station = self._station(station_id)
        if not isinstance(minutes, int) or isinstance(minutes, bool) or minutes < 0:
            raise ValueError("Stop extension must be a non-negative integer")

        for stop in self.visits:
            if stop.station is station:
                if stop.departure is None:
                    raise ValueError(
                        f"Stop at station {station_id} has no departure time"
                    )
                departure = datetime.strptime(stop.departure, "%H:%M")
                stop.departure = (
                    departure + timedelta(minutes=minutes)
                ).strftime("%H:%M")
                return self

        raise ValueError(
            f"Train {self.id} has no stop at station ID {station_id}"
        )

    def change_platform(self, station_id, platform):
        """Change the platform assigned to a station stop."""
        station = self._station(station_id)
        platform = self._validate_platform(station, platform)

        for stop in self.visits:
            if stop.station is station:
                stop.platform = platform
                return self

        raise ValueError(
            f"Train {self.id} has no stop at station ID {station_id}"
        )

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
        train = cls(
            train_id, name, composition, train_type, max_speed_kmph, flags
        )

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
                departure = (current_time + timedelta(minutes=dwell_time)).strftime(
                    "%H:%M"
                )
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

    @staticmethod
    def reverse_blueprint(blueprint):
        """Return a local-time blueprint for the same service in reverse."""
        stops = blueprint["stops"]
        return {
            "name": blueprint["name"],
            "stops": [
                {
                    "station_id": stop["station_id"],
                    "platform": stop.get("platform", "any"),
                    "arrival": (
                        None
                        if index == 0
                        else stops[len(stops) - index]["arrival"]
                    ),
                    "departure": (
                        0
                        if index == 0
                        else (
                            None
                            if index == len(stops) - 1
                            else stop["departure"]
                        )
                    ),
                }
                for index, stop in enumerate(reversed(stops))
            ],
        }


def trains_to_dataframe(trains, stations=STATIONS):
    """Flatten structured station/train data for plotting and tabular output."""
    rows = []
    for train in trains:
        for stop in train.stops:
            station_id = stop.station.id
            try:
                station = stations[station_id]
            except KeyError as error:
                raise ValueError(
                    f"Unknown station ID in train {train.id}: {station_id}"
                ) from error

            rows.append({
                "Train number": f"{train.name} ({train.id})",
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


def reverse_blueprint(blueprint):
    """Compatibility wrapper for :meth:`Train.reverse_blueprint`."""
    return Train.reverse_blueprint(blueprint)


def create_train(train_id, blueprint, name, start_time, **train_options):
    """Compatibility wrapper for :meth:`Train.from_blueprint`."""
    return Train.from_blueprint(
        train_id, blueprint, name, start_time, **train_options
    )


# Compatibility aliases for callers using the earlier naming style.
stationCodeToId = station_code_to_id
train = Train
