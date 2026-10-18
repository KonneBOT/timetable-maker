import os
from pathlib import Path

import matplotlib
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd


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


def plot_route_timetable(df, title_name):
    """Plot the route timetable as a distance-time diagram."""
    fig, ax = plt.subplots(figsize=(12, 7))
    df["arrival_dt"] = pd.to_datetime(df["Arrival"], format="%H:%M", errors="coerce")
    df["departure_dt"] = pd.to_datetime(
        df["Departure"], format="%H:%M", errors="coerce"
    )
    stations = df[["Stop", "Km"]].drop_duplicates().sort_values("Km")

    for _, row in stations.iterrows():
        ax.axhline(row["Km"], color="lightgray", linewidth=0.8, zorder=1)

    for train_number, train_data in df.groupby("Train number"):
        path_points = []
        for _, row in train_data.iterrows():
            if pd.notnull(row["arrival_dt"]):
                path_points.append((row["arrival_dt"], row["Km"]))
            if pd.notnull(row["departure_dt"]):
                path_points.append((row["departure_dt"], row["Km"]))
        path_points.sort(key=lambda item: item[0])
        if path_points:
            times, distances = zip(*path_points)
            ax.plot(times, distances, marker="o", markersize=4, linewidth=2,
                    label=train_number, zorder=3)

    ax.set_yticks(stations["Km"])
    ax.set_yticklabels(stations["Stop"], fontsize=10, fontweight="bold")
    ax.set_ylabel("Route profile (stops)", fontsize=11)
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
    ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=5))
    ax.xaxis.set_minor_locator(mdates.MinuteLocator(interval=1))
    ax.set_xlabel("Time", fontsize=11)
    plt.xticks(rotation=45)
    ax.grid(True, which="major", axis="y", color="gainsboro", linestyle=":")
    ax.grid(True, which="major", axis="x", color="gainsboro", linestyle=":")
    ax.grid(True, which="minor", axis="x", color="lightgray", linestyle="--")
    plt.title(f"Route timetable (graphic timetable): {title_name}", fontsize=14)
    plt.legend(title="Trains", loc="upper left", bbox_to_anchor=(1.01, 1))
    plt.tight_layout()
    display_or_save(fig, "route_timetable", title_name)


def generate_line_timetable(df, title_name):
    """Create a classic line timetable as a matrix table."""
    df["Time"] = df["Departure"].fillna(df["Arrival"])
    timetable_table = df.pivot(index="Stop", columns="Train number", values="Time")
    station_order = df[["Stop", "Km"]].drop_duplicates().sort_values("Km")["Stop"]
    timetable_table = timetable_table.reindex(station_order).fillna("|")

    fig, ax = plt.subplots(figsize=(8, len(station_order) * 0.5 + 1.5))
    ax.axis("off")
    table_data = [
        [station] + list(row.values)
        for station, row in timetable_table.iterrows()
    ]
    table = ax.table(
        cellText=table_data,
        colLabels=["Stop / Train"] + list(timetable_table.columns),
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

    plt.title(f"Line timetable / display: {title_name}", fontweight="bold")
    plt.tight_layout()
    display_or_save(fig, "line_timetable", title_name)
