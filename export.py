from datetime import datetime
from pathlib import Path
import shutil
import subprocess

from train import STATIONS


def _duration_minutes(arrival, departure):
    if arrival is None or departure is None:
        return 0
    time_format = "%H:%M:%S" if len(arrival.split(":")) == 3 else "%H:%M"
    start = datetime.strptime(arrival, time_format)
    end = datetime.strptime(departure, time_format)
    return int((end - start).total_seconds() // 60)


def _train_type(train):
    return "REG" if train.train_type == "REGIONAL" else train.train_type


def _export_train_id(train):
    """Return the compact identifier used in exported train rows."""
    prefix = train.name.split(maxsplit=1)[0]
    return f"{prefix}_{train.id}"


def _export_train_ids(train, leg_index, total_legs):
    """Return the exported name and reporting number for one leg."""
    if total_legs == 1:
        export_train_id = _export_train_id(train)
        return export_train_id, export_train_id

    parent = train
    while parent._leg_parent is not None:
        parent = parent._leg_parent
    parent_id = _export_train_id(parent)
    return parent_id, f"{parent_id}{chr(ord('A') + leg_index)}"


def _format_from_time(value):
    return value if len(value.split(":")) == 3 else f"{value}:00"


def _format_platform(station, platform):
    if platform == "any":
        return "0"
    if isinstance(platform, int) and not isinstance(platform, bool):
        return str(platform)
    if isinstance(platform, str) and platform.isdigit():
        return platform
    raise ValueError(
        f"Invalid platform {platform!r} for station {station.code}; "
        "trains.txt requires a numeric platform"
    )


def _copy_text_to_clipboard(text):
    """Copy text using an installed Linux clipboard utility."""
    commands = (
        (("wl-copy",), "Wayland"),
        (("xclip", "-selection", "clipboard"), "xclip"),
        (("xsel", "--clipboard", "--input"), "xsel"),
    )
    for command, _name in commands:
        if shutil.which(command[0]):
            subprocess.run(command, input=text, text=True, check=True)
            return
    raise RuntimeError(
        "No clipboard utility found; install wl-clipboard, xclip, or xsel"
    )


def _output_to_clipboard_or_terminal(output):
    choice = input("Copy to clipboard or print to terminal? [c/p/q] ").strip().lower()
    if choice in {"c", "clipboard"}:
        _copy_text_to_clipboard(output)
        print("Timetable copied to the clipboard.")
        return
    if choice == "q":
        return
    print(output, end="")


def export_trains_txt(trains, file_path=None):
    """Export trains and interactively choose file, clipboard, or terminal."""
    lines = ["+++timetable"]
    for train in trains:
        legs = list(train.iter_legs())
        for index, leg in enumerate(legs):
            export_name, export_reporting_number = _export_train_ids(
                train, index, len(legs)
            )
            visits = []
            for visit in leg.visits:
                station = STATIONS[visit.station.id]
                from_time = visit.arrival or visit.departure
                if from_time is None:
                    raise ValueError(
                        f"Train {train.id} has a visit without a timetable time"
                    )
                visits.append(
                    f"{station.abbrev}#{_format_platform(station, visit.platform)}"
                    f"#{_format_from_time(from_time)}#"
                    f"{_duration_minutes(visit.arrival, visit.departure)}"
                )
            lines.append(
                f"{export_name}|{export_reporting_number} {_train_type(train)} "
                f"{train.max_speed_kmph} {train.composition} {train.flags} : "
                + " ".join(visits)
            )

    output = "\n".join(lines) + "\n"
    if file_path is not None:
        path = Path(file_path)
        if path.exists():
            answer = input(f"{path} already exists. Overwrite? [y/N/q] ").strip().lower()
            if answer == "q":
                return output
            if answer not in {"y", "yes"}:
                _output_to_clipboard_or_terminal(output)
                return output
        path.write_text(output, encoding="utf-8")
        print(f"Timetable exported to {path}.")
        return output

    _output_to_clipboard_or_terminal(output)
    return output
