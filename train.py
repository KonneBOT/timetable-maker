from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent
STATIONS_FILE = BASE_DIR / "stations.txt"


def parse_station_file(file):
    """Load station data from ``abbrev|name|code|km`` records."""
    stations = {}
    with open(file, "r", encoding="utf-8") as station_file:
        for line_number, line in enumerate(station_file, start=1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            parts = [part.strip() for part in line.split("|")]
            if len(parts) != 4:
                raise ValueError(
                    f"Invalid station record in {file}:{line_number}; "
                    "expected abbrev|name|code|km"
                )

            abbrev, name, code, km_text = parts
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

            stations[len(stations) + 1] = {
                "name": name,
                "code": code,
                "km": km,
                "abbrev": abbrev,
            }

    if not stations:
        raise ValueError(f"No stations found in {file}")
    return stations


STATIONS = parse_station_file(STATIONS_FILE)


def station_code_to_id(code):
    """Return the station ID for a station code."""
    for station_id, station in STATIONS.items():
        if station["code"] == code:
            return station_id
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
        self.stops = []

    def add_stop(self, station_id, arrival=None, departure=None):
        """Append a stop and return this train for fluent construction."""
        if station_id not in STATIONS:
            raise ValueError(f"Unknown station ID in train {self.id}: {station_id}")
        self.stops.append({
            "station_id": station_id,
            "arrival": arrival,
            "departure": departure,
        })
        return self

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
        """Create a concrete train by applying a start time to a blueprint."""
        start = datetime.strptime(start_time, "%H:%M")
        train = cls(
            train_id, name, composition, train_type, max_speed_kmph, flags
        )

        for stop in blueprint["stops"]:
            def absolute_time(offset):
                if offset is None:
                    return None
                return (start + timedelta(minutes=offset)).strftime("%H:%M")

            train.add_stop(
                stop["station_id"],
                absolute_time(stop["arrival"]),
                absolute_time(stop["departure"]),
            )
        return train

    @staticmethod
    def reverse_blueprint(blueprint):
        """Return a blueprint for the same service in the opposite direction."""
        end = max(
            offset
            for stop in blueprint["stops"]
            for offset in (stop["arrival"], stop["departure"])
            if offset is not None
        )
        return {
            "name": blueprint["name"],
            "stops": [
                {
                    "station_id": stop["station_id"],
                    "arrival": (
                        None
                        if stop["departure"] is None
                        else end - stop["departure"]
                    ),
                    "departure": (
                        None
                        if stop["arrival"] is None
                        else end - stop["arrival"]
                    ),
                }
                for stop in reversed(blueprint["stops"])
            ],
        }


def trains_to_dataframe(trains, stations=STATIONS):
    """Flatten structured station/train data for plotting and tabular output."""
    rows = []
    for train in trains:
        for stop in train.stops:
            station_id = stop["station_id"]
            try:
                station = stations[station_id]
            except KeyError as error:
                raise ValueError(
                    f"Unknown station ID in train {train.id}: {station_id}"
                ) from error

            rows.append({
                "Train number": f"{train.name} ({train.id})",
                "Stop": station["name"],
                "Abbreviation": station["abbrev"],
                "Station code": station["code"],
                "Station ID": station_id,
                "Km": station["km"],
                "Arrival": stop["arrival"],
                "Departure": stop["departure"],
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
