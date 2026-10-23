# Timetable Maker

This project builds timetable data in Python and exports it in the
`trains.txt` format.

## Workflow

1. Define a blueprint or create a `Train` directly.
2. Create each finished train as a named variable with a stable ID.
3. Add only the trains that should be exported to `TRAINS` in `main.py`.
4. Export the staged trains with `export_trains_txt`.
5. Combine the generated timetable section with the station/reference section
   when producing the final `trains.txt`.

The stable ID is useful when locating and editing a train later. Use names
such as `train_19317`, while the numeric or external reporting number remains
the first argument passed to `Train.from_blueprint`.

```python
train_19317 = Train.from_blueprint(
    "19317",
    MEX_TUEBINGEN_REUTLINGEN,
    "MEX 13",
    "08:17",
    "LPPPL",
    "REG",
    120,
    "X1",
)

TRAINS = [
    train_19317,
]
```

## Getting a usable `trains.txt`

`trains.txt` has two parts:

- the station/reference section, which defines station symbols, names, and
  platforms;
- the `+++timetable` section, which contains train rows.

Keep the station/reference section in the final file. The exporter generates
only the `+++timetable` section from the staged Python trains:

```python
from export import export_trains_txt
from main import TRAINS

export_trains_txt(TRAINS, "generated_timetable.txt")
```

Copy the generated `+++timetable` section below the station/reference section
to create the final `trains.txt`. If the target file already exists, the
exporter asks whether it may overwrite it. If overwriting is declined, it
offers clipboard copying or terminal output instead.

Without a file path, the exporter directly offers clipboard copying or
terminal output:

```python
export_trains_txt(TRAINS)
```

Clipboard support uses the first available `wl-copy`, `xclip`, or `xsel`
command. If none is installed and clipboard output is selected, the exporter
raises an explicit error.

The generated file must use station references that are present in the
station section. The exporter obtains these references from `stations.txt`.
If you add a station, add it to `stations.txt` first and make sure its
platform is valid.

A timetable row has this shape:

```text
Name|ReportingNumber TYPE MaxSpeed Composition Flags : Visit Visit ...
```

Each visit has this shape:

```text
StationReference#Platform#From#DurationMinutes
```

For example:

```text
S3|S3 REG 160 LPPPP X1 : þ#1#08:00:00#1 ü#1#08:02:00#1
```

`From` is an absolute time. The duration is the dwell time:

- `0` for a passing visit;
- `1` or another positive value for a stop;
- `0` for a terminal visit without a departure.

The exporter writes `REGIONAL` trains as `REG`, as required by the file
format. Other train types are written as configured.

## Creating a multi-leg train

Only `REG`/`REGIONAL` trains may have multiple legs. Create every leg as a
normal `Train`, then append it to the first leg with `add_leg`. The
`intermission` is the number of minutes between the last `From` time of the
previous leg and the first `From` time of the next leg.

```python
train_19317 = Train.from_blueprint(
    "19317",
    FIRST_LEG_BLUEPRINT,
    "MEX 13",
    "08:00",
    "LPPPL",
    "REG",
    120,
    "X1",
)

train_19317_leg_b = Train.from_blueprint(
    "19317B",
    SECOND_LEG_BLUEPRINT,
    "MEX 13",
    "09:00",
    "LPPPL",
    "REG",
    120,
    "X1",
)

train_19317.add_leg(train_19317_leg_b, intermission=12)
TRAINS = [train_19317]
```

For a train named `MEX 13`, the exported reporting numbers are:

```text
MEX 13|MEX 13A
MEX 13|MEX 13B
```

Names are not normalized: the space in `MEX 13` remains present.

Use `timetable()` while building a train. It displays the stable train ID,
leg boundaries, intermissions, and one-based positions:

```python
print(train_19317.timetable())
```

`insert_stop(position=2, ...)` inserts a stop after position 2. For a
multi-leg train, specify the leg:

```python
train_19317.insert_stop(
    position=2,
    station_id="RBE",
    arrival="08:10",
    departure="08:11",
    platform=1,
    leg="A",
)
```

Use `set_origin` and `set_ending` when a train needs an additional first or
last station. Both support passing and stopping visits:

```python
train_19317.set_origin("TTG", travel_time=2, stopping=True, platform=1)
train_19317.set_ending("TRE", travel_time=4, stopping=False, platform=1)
```

## Running

The project uses the virtual environment in `venv/`:

```bash
venv/bin/python main.py
```

The plotting entry point uses the trains currently staged in `TRAINS`.
