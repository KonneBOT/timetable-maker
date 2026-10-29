import os
from functools import cmp_to_key
from pathlib import Path

import matplotlib
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd

from sections import get_section
from train import Station, trains_to_dataframe

if os.environ.get("DISPLAY", "") == "" and os.name != "nt":
    matplotlib.use("Agg")


OUTPUT_DIR = Path(__file__).resolve().parent / "output"


def output_path(filename):
    """Return a path inside the output directory for generated files."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    path = Path(filename)
    return path if path.is_absolute() else OUTPUT_DIR / path


def display_or_save(fig, filename_prefix, title_name):
    """Save plots in the output directory and show them in interactive mode."""
    safe_title = title_name.replace(" ", "_").replace("/", "_")
    fig.savefig(output_path(f"{filename_prefix}_{safe_title}.png"),
                dpi=200, bbox_inches="tight")

    if matplotlib.get_backend().lower() == "agg":
        plt.close(fig)
    else:
        plt.show()


def _filter_section_dataframe(
    df, section, minimum_visits=True, bidirectional=True
):
    section = get_section(section)
    station_refs = list(section.station_codes)
    station_codes = {
        ref: index for index, ref in enumerate(station_refs)
        if isinstance(ref, str)
    }
    station_ids = {
        ref: index for index, ref in enumerate(station_refs)
        if isinstance(ref, int)
    }
    section_stations = df[
        df["Station code"].isin(
            code for code in station_codes
        )
        | df["Station ID"].isin(
            station_id for station_id in station_ids
        )
    ].copy()
    if minimum_visits:
        section_stations["_section_position"] = section_stations.apply(
            lambda row: station_ids.get(
                row["Station ID"], station_codes.get(row["Station code"])
            ),
            axis=1,
        )
        eligible = []
        for train_number, train_data in section_stations.groupby(
            "Train number", sort=False
        ):
            positions = train_data["_section_position"].tolist()
            is_forward = all(
                earlier < later for earlier, later in zip(positions, positions[1:])
            )
            is_reverse = all(
                earlier > later for earlier, later in zip(positions, positions[1:])
            )
            if len(set(positions)) >= 2 and (
                is_forward or (bidirectional and is_reverse)
            ):
                eligible.append(train_number)
        section_stations = section_stations[
            section_stations["Train number"].isin(eligible)
        ].copy()
    return section, section_stations


def plot_route_timetable(
    df, title_name, start_time="00:00", duration=24 * 60
):
    """Plot the route timetable as a distance-time diagram for a time window."""
    start = _parse_time(start_time)
    if pd.isna(start):
        raise ValueError(f"Invalid start time: {start_time!r}")
    if not isinstance(duration, int) or isinstance(duration, bool) or duration <= 0:
        raise ValueError("Duration must be a positive integer in minutes")
    end = start + pd.Timedelta(minutes=duration)

    section, df = _filter_section_dataframe(df, title_name)
    if df.empty:
        raise ValueError(f"No trains have at least two visits in section {section.name!r}")
    if section.name == "TMS - RTS" or section.name == "RTS - TMS" or section.name == "Mössingen - Betzingen" or section.name == "Betzingen - Mössingen":
        tms_rows = df["Station code"].isin(["TMS", "RTW", "RBO"])
        df.loc[tms_rows, "Km"] = df.loc[tms_rows, "Km values"].map(
            lambda values: values[1] if len(values) > 1 else values[0]
        )
    df["arrival_dt"] = pd.to_datetime(df["Arrival"], format="%H:%M", errors="coerce")
    df["departure_dt"] = pd.to_datetime(
        df["Departure"], format="%H:%M", errors="coerce"
    )
    in_window = (
        df["arrival_dt"].between(start, end, inclusive="left")
        | df["departure_dt"].between(start, end, inclusive="left")
    )
    eligible_trains = df.loc[in_window, "Train number"].unique()
    df = df[df["Train number"].isin(eligible_trains)].copy()
    if df.empty:
        raise ValueError(
            f"No trains have visits in section {section.name!r} "
            "in the requested time window"
        )

    stations = df[["Stop", "Station code", "Station ID", "Km"]].drop_duplicates()
    station_order = []
    for station_ref in section.station_codes:
        matches = stations[
            (stations["Station code"] == station_ref)
            | (stations["Station ID"] == station_ref)
        ]
        for station_code in matches["Station code"]:
            if station_code not in station_order:
                station_order.append(station_code)
    stations["order"] = stations["Station code"].map(
        {code: index for index, code in enumerate(station_order)}
    )
    stations = stations.sort_values("order")
    fig, ax = plt.subplots(
        figsize=(max(12, len(df["Train number"].unique()) * 0.45 + 6),
                 max(7, len(stations) * 0.35 + 3))
    )

    for _, row in stations.iterrows():
        ax.axhline(row["Km"], color="lightgray", linewidth=0.8, zorder=1)

    for train_number, train_data in df.groupby("Train number"):
        path_points = []
        through_points = []
        for _, row in train_data.iterrows():
            if pd.notnull(row["arrival_dt"]):
                path_points.append((row["arrival_dt"], row["Km"]))
                if row.get("Through run", False):
                    through_points.append((row["arrival_dt"], row["Km"]))
            if pd.notnull(row["departure_dt"]):
                path_points.append((row["departure_dt"], row["Km"]))
        path_points.sort(key=lambda item: item[0])
        if path_points:
            times, distances = zip(*path_points)
            ax.plot(times, distances, linewidth=2,
                    label=train_number, zorder=3)
            if through_points:
                through_times, through_distances = zip(*through_points)
                ax.scatter(
                    through_times,
                    through_distances,
                    facecolors="none",
                    edgecolors="C0",
                    s=40,
                    zorder=4,
                )

    ax.set_yticks(stations["Km"])
    ax.set_yticklabels(
        stations["Station code"], fontsize=10, fontweight="bold"
    )
    ax.set_ylabel("Route profile (stops)", fontsize=11)
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
    ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=5))
    ax.xaxis.set_minor_locator(mdates.MinuteLocator(interval=1))
    ax.set_xlim(start, end)
    ax.set_xlabel("Time", fontsize=11)
    plt.xticks(rotation=45)
    ax.grid(True, which="major", axis="y", color="gainsboro", linestyle=":")
    ax.grid(True, which="major", axis="x", color="gainsboro", linestyle=":")
    ax.grid(True, which="minor", axis="x", color="lightgray", linestyle="--")
    plt.title(
        f"Route timetable (graphic timetable): {title_name} "
        f"({start_time}, {duration} min)",
        fontsize=14,
    )
    plt.legend(title="Trains", loc="upper left", bbox_to_anchor=(1.01, 1))
    plt.tight_layout()
    display_or_save(fig, "route_timetable", title_name)


def _parse_time(time_text):
    return pd.to_datetime(time_text, format="%H:%M", errors="coerce")


def _sort_line_timetable_trains(df, train_numbers, base_order):
    """Keep the base order unless trains share a later station."""
    train_numbers = list(train_numbers)
    train_rank = {
        train_number: rank for rank, train_number in enumerate(base_order)
    }
    train_rows = {
        train_number: train_data.set_index("_section_position")
        for train_number, train_data in df.groupby("Train number", sort=False)
    }

    def compare(left, right):
        common_positions = sorted(
            set(train_rows[left].index) & set(train_rows[right].index)
        )
        if common_positions:
            position = common_positions[0]
            left_time = _parse_time(
                train_rows[left].loc[position, "Event time"]
            )
            right_time = _parse_time(
                train_rows[right].loc[position, "Event time"]
            )
            if left_time != right_time:
                return -1 if left_time < right_time else 1
        return train_rank[left] - train_rank[right]

    return sorted(train_numbers, key=cmp_to_key(compare))


def plot_station_departures(
    trains, station, start_time="00:00", duration=24 * 60
):
    """Plot all departures from a station in a time window."""
    start = _parse_time(start_time)
    if pd.isna(start):
        raise ValueError(f"Invalid start time: {start_time!r}")
    if not isinstance(duration, int) or isinstance(duration, bool) or duration <= 0:
        raise ValueError("Duration must be a positive integer in minutes")
    end = start + pd.Timedelta(minutes=duration)

    df = trains_to_dataframe(trains)
    if isinstance(station, Station):
        station_rows = df[df["Station ID"] == station.id].copy()
    elif isinstance(station, int) and not isinstance(station, bool):
        station_rows = df[df["Station ID"] == station].copy()
    elif isinstance(station, str):
        station_rows = df[df["Station code"] == station].copy()
    else:
        raise ValueError(
            "Station must be a Station, station code or numeric station ID"
        )
    if station_rows.empty:
        raise ValueError(f"No visits found for station {station!r}")

    station_rows["arrival_dt"] = pd.to_datetime(
        station_rows["Arrival"], format="%H:%M", errors="coerce"
    )
    station_rows["departure_dt"] = pd.to_datetime(
        station_rows["Departure"], format="%H:%M", errors="coerce"
    )
    station_rows = station_rows[
        station_rows["departure_dt"].between(start, end, inclusive="left")
    ].sort_values(["departure_dt", "Train number"])
    if station_rows.empty:
        raise ValueError(
            f"No trains depart from station {station!r} "
            "in the requested time window"
        )

    table_data = [
        [
            row["Train number"],
            row["Arrival"] or "-",
            row["Departure"],
            row["Platform"],
            row["Destination"],
        ]
        for _, row in station_rows.iterrows()
    ]
    columns = ["Train", "Arrival", "Departure", "Platform", "Direction"]
    fig, ax = plt.subplots(
        figsize=(max(10, len(columns) * 1.8),
                 max(2.5, len(table_data) * 0.45 + 1.5))
    )
    ax.axis("off")
    table = ax.table(
        cellText=table_data,
        colLabels=columns,
        loc="center",
        cellLoc="center",
        colWidths=[0.28, 0.14, 0.14, 0.14, 0.30],
    )
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.1, 1.7)
    for (row, col), cell in table.get_celld().items():
        if row == 0:
            cell.set_facecolor("#003366")
            cell.get_text().set_color("white")
            cell.get_text().set_weight("bold")
        elif col == 0:
            cell.set_facecolor("#f2f2f2")
            cell.get_text().set_weight("bold")
            cell.get_text().set_ha("left")

    station_name = station_rows.iloc[0]["Stop"]
    plt.title(
        f"Station departures: {station_name} ({start_time}, {duration} min)",
        fontweight="bold",
    )
    plt.tight_layout()
    display_or_save(fig, "station_departures", str(station))


def generate_line_timetable(
    trains, section, start_time="00:00", duration=24 * 60
):
    """Create a section-specific line timetable for a time window.

    ``duration`` is measured in minutes. The section is defined by the
    ordered station codes in ``sections.LINE_SECTIONS``.
    """
    section = get_section(section)
    start = _parse_time(start_time)
    if pd.isna(start):
        raise ValueError(f"Invalid start time: {start_time!r}")
    if not isinstance(duration, int) or isinstance(duration, bool) or duration <= 0:
        raise ValueError("Duration must be a positive integer in minutes")
    end = start + pd.Timedelta(minutes=duration)
    df = trains_to_dataframe(trains)
    section, df = _filter_section_dataframe(
        df, section, bidirectional=False
    )
    if df.empty:
        raise ValueError(f"No visits found for section {section.name!r}")

    # A train may enter the section after its configured endpoint. Use its
    # first actual visit so partial services are included as well.
    first_rows = (
        df.sort_values(["Train number", "_section_position"])
        .drop_duplicates("Train number", keep="first")
        .copy()
    )
    first_rows["departure_dt"] = pd.to_datetime(
        first_rows["Departure"], format="%H:%M", errors="coerce"
    )
    eligible_trains = first_rows.loc[
        first_rows["departure_dt"].between(start, end, inclusive="left"),
        "Train number",
    ].unique()
    df = df[df["Train number"].isin(eligible_trains)].copy()
    if df.empty:
        raise ValueError(
            f"No trains depart from the first station of section {section.name!r} "
            "in the requested time window"
        )

    def display_time(row):
        event_time = row["Arrival"] if row["Through run"] else (
            row["Departure"] or row["Arrival"]
        )
        if row["Through run"]:
            return f"{event_time} ○"
        if row["Platform"] == "any":
            return event_time
        return f"{event_time} / {row['Platform']}"

    df["Event time"] = df.apply(
        lambda row: row["Arrival"]
        if row["Through run"]
        else (row["Departure"] or row["Arrival"]),
        axis=1,
    )
    df["Time"] = df.apply(display_time, axis=1)
    base_order = (
        first_rows[first_rows["Train number"].isin(eligible_trains)]
        .groupby("Train number")["Departure"]
        .first()
        .map(_parse_time)
        .sort_values()
        .index
    )
    timetable_table = df.pivot_table(
        index="Station code", columns="Train number", values="Time", aggfunc="first"
    )
    station_order = []
    for station_ref in section.station_codes:
        if isinstance(station_ref, str):
            code = station_ref
        else:
            matches = df.loc[df["Station ID"] == station_ref, "Station code"]
            code = matches.iloc[0] if not matches.empty else None
        if code in timetable_table.index and code not in station_order:
            station_order.append(code)
    departure_order = _sort_line_timetable_trains(
        df, eligible_trains, base_order
    )
    timetable_table = timetable_table.reindex(station_order)
    for train_number in timetable_table.columns:
        present = timetable_table[train_number].notna()
        if not present.any():
            timetable_table[train_number] = ""
            continue
        first_stop = present.idxmax()
        last_stop = present[::-1].idxmax()
        before_first = timetable_table.index.get_loc(first_stop)
        after_last = timetable_table.index.get_loc(last_stop) + 1
        timetable_table.loc[
            timetable_table.index[:before_first], train_number
        ] = ""
        timetable_table.loc[
            timetable_table.index[after_last:], train_number
        ] = ""
    timetable_table = timetable_table.fillna("|")
    timetable_table = timetable_table.reindex(columns=departure_order)

    fig, ax = plt.subplots(
        figsize=(max(8, len(timetable_table.columns) * 1.4 + 2),
                 max(2.5, len(station_order) * 0.5 + 1.5))
    )
    ax.axis("off")
    table_data = [
        [station] + list(row.values)
        for station, row in timetable_table.iterrows()
    ]
    table = ax.table(
        cellText=table_data,
        colLabels=["Station"] + list(timetable_table.columns),
        loc="center",
        cellLoc="center",
    )
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.8)
    for (row, col), cell in table.get_celld().items():
        if row == 0:
            cell.set_facecolor("#003366")
            cell.get_text().set_color("white")
            cell.get_text().set_weight("bold")
        elif col == 0:
            cell.set_facecolor("#f2f2f2")
            cell.get_text().set_weight("bold")
            cell.get_text().set_ha("left")

    plt.title(
        f"Line timetable / display: {section.name} ({start_time}, {duration} min)",
        fontweight="bold",
    )
    plt.tight_layout()
    display_or_save(fig, "line_timetable", section.name)
