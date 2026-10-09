import os
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd
import matplotlib

if os.environ.get("DISPLAY", "") == "" and os.name != "nt":
    matplotlib.use("Agg")

import matplotlib.pyplot as plt
import matplotlib.dates as mdates


OUTPUT_DIR = Path(__file__).resolve().parent / "output"


def output_path(filename):
    """Return a path inside the output directory for generated files."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    path = Path(filename)
    return path if path.is_absolute() else OUTPUT_DIR / path


# Stations are defined once and trains refer to them by ID.  This keeps names,
# abbreviations, and route positions consistent across all timetable sources.
STATIONS = {
    1: {"name": "Tübingen Hbf", "code": "TT", "km": 0.0},
    2: {"name": "Tübingen Güterbahnhof", "code": "TTG", "km": 1.4},
    3: {"name": "Tübingen Neckaraue", "code": "TTN", "km": 2.5},
    4: {"name": "Kirchentellinsfurt", "code": "TKI", "km": 7.4},
    5: {"name": "Wannweil", "code": "TWAN", "km": 9.5},
    6: {"name": "Reutlingen Betzingen", "code": "TREB", "km": 12.0},
    7: {"name": "Reutlinge Bösmannsäcker", "code": "TRBO", "km": 13.1},
    8: {"name": "Reutlingen West", "code": "RTW", "km": 13.9},
    9: {"name": "Reutlingen Hbf", "code": "TRE", "km": 14.8},
}

def stationCodeToId(name):
    """Return the station ID for a given station code."""
    for station_id, station in STATIONS.items():
        if station["code"] == name:
            return station_id
    raise ValueError(f"Unknown station code: {name}")

# A blueprint contains only relative times.  Changing the first departure
# shifts the complete train while keeping all running and dwell times intact.
RS1_TUEBINGEN_REUTLINGEN = {
    "name": "RS 1",
    "stops": [
        {"station_id": 1, "arrival": None, "departure": 0},
        {"station_id": 2, "arrival": 1, "departure": 2},
        {"station_id": 3, "arrival": 3, "departure": 4},
        {"station_id": 4, "arrival": 8, "departure": 9},
        {"station_id": 5, "arrival": 12, "departure": 13},
        {"station_id": 6, "arrival": 16, "departure": 17},
        {"station_id": 7, "arrival": 19, "departure": 20},
        {"station_id": 8, "arrival": 22, "departure": 23},
        {"station_id": 9, "arrival": 25, "departure": None},
    ],
}

MEX_RE_TUEBINGEN_REUTLINGEN = {
    "name": "MEX RE",
    "stops": [
        {"station_id": stationCodeToId("TT"), "arrival": None, "departure": 0},
        {"station_id": stationCodeToId("TRE"), "arrival": 9, "departure": 10}
    ]
}


def reverse_blueprint(blueprint):
    """Return the same run in the opposite direction."""
    end = max(
        offset
        for stop in blueprint["stops"]
        for offset in (stop["arrival"], stop["departure"])
        if offset is not None
    )
    reversed_stops = []
    for stop in reversed(blueprint["stops"]):
        reversed_stops.append({
            "station_id": stop["station_id"],
            "arrival": None if stop["departure"] is None else end - stop["departure"],
            "departure": None if stop["arrival"] is None else end - stop["arrival"],
        })
    return {"name": blueprint["name"], "stops": reversed_stops}


def create_train(train_id, blueprint, start_time):
    """Create one concrete train from a relative-time blueprint."""
    start = datetime.strptime(start_time, "%H:%M")
    stops = []

    for stop in blueprint["stops"]:
        station_id = stop["station_id"]
        if station_id not in STATIONS:
            raise ValueError(f"Unknown station ID in blueprint: {station_id}")

        def absolute_time(offset):
            if offset is None:
                return None
            return (start + timedelta(minutes=offset)).strftime("%H:%M")

        stops.append({
            "station_id": station_id,
            "arrival": absolute_time(stop["arrival"]),
            "departure": absolute_time(stop["departure"]),
        })

    return {"id": train_id, "name": blueprint["name"], "stops": stops}


def trains_to_dataframe(trains, stations=STATIONS):
    """Flatten structured station/train data for plotting and tabular output."""
    rows = []
    for train in trains:
        for stop in train["stops"]:
            station_id = stop["station_id"]
            try:
                station = stations[station_id]
            except KeyError as error:
                raise ValueError(f"Unknown station ID in train {train['id']}: {station_id}") from error

            rows.append({
                "Train number": f"{train['name']} ({train['id']})",
                "Stop": station["name"],
                "Station code": station["code"],
                "Station ID": station_id,
                "Km": station["km"],
                "Arrival": stop["arrival"],
                "Departure": stop["departure"],
            })
    return pd.DataFrame(rows)


TRAINS = [
    create_train("1001", RS1_TUEBINGEN_REUTLINGEN, "08:00"),
    create_train("1002", reverse_blueprint(RS1_TUEBINGEN_REUTLINGEN), "08:10"),
    create_train("1003", RS1_TUEBINGEN_REUTLINGEN, "08:10"),
    create_train("19213", MEX_RE_TUEBINGEN_REUTLINGEN, "08:08"),
]


def display_or_save(fig, filename_prefix, title_name):
    """Save plots in the output directory and show them in interactive mode."""
    safe_title = title_name.replace(" ", "_").replace("/", "_")
    filename = output_path(f"{filename_prefix}_{safe_title}.png")
    fig.savefig(filename, dpi=200, bbox_inches="tight")

    if matplotlib.get_backend().lower() == "agg":
        plt.close(fig)
    else:
        plt.show()


def create_sample_excel(filename="RS_timetable_data.xlsx"):
    """Creates a sample Excel file with data for the RS Neckar-Alb."""
    filename = output_path(filename)
    # Create Excel with different tabs for the sections
    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        trains_to_dataframe(TRAINS).to_excel(
            writer, sheet_name="Tübingen - Reutlingen", index=False
        )
        
        # Empty/placeholder sheets for the remaining required sections
        for sheet in ["RT-Betzingen-Ohmenhausen", "Tübingen - Albstadt", "Tübingen - Rottenburg", "Tübingen - Entringen"]:
            pd.DataFrame(columns=["Train number", "Stop", "Km", "Arrival", "Departure"]).to_excel(writer, sheet_name=sheet, index=False)

    print(f"Excel file '{filename}' successfully created with sample data.")

def plot_route_timetable(df, title_name):
    """Plots the route timetable (graphic timetable / distance-time diagram)."""
    fig, ax = plt.subplots(figsize=(12, 7))

    # Convert times to datetime objects
    df['arrival_dt'] = pd.to_datetime(df['Arrival'], format='%H:%M', errors='coerce')
    df['departure_dt'] = pd.to_datetime(df['Departure'], format='%H:%M', errors='coerce')

    # Determine unique stations and km positions
    stations = df[['Stop', 'Km']].drop_duplicates().sort_values('Km')
    
    # Horizontal lines for stations
    for _, row in stations.iterrows():
        ax.axhline(y=row['Km'], color='lightgray', linestyle='-', linewidth=0.8, zorder=1)

    # Draw train paths in chronological order to avoid backtracking between
    # arrival and departure points at the same stop.
    for train_number, train_data in df.groupby('Train number'):
        path_points = []

        for _, row in train_data.iterrows():
            km = row['Km']
            arrival = row['arrival_dt']
            departure = row['departure_dt']

            if pd.notnull(arrival):
                path_points.append((arrival, km))
            if pd.notnull(departure):
                path_points.append((departure, km))

        if not path_points:
            continue

        path_points.sort(key=lambda item: item[0])
        times = [point[0] for point in path_points]
        distances = [point[1] for point in path_points]

        # Plot route
        ax.plot(times, distances, marker='o', markersize=4, linewidth=2, label=train_number, zorder=3)

    # Formatting of the Y-axis (stations)
    ax.set_yticks(stations['Km'])
    ax.set_yticklabels(stations['Stop'], fontsize=10, fontweight='bold')
    ax.set_ylabel("Route profile (stops)", fontsize=11)

    # Formatting of the X-axis (time)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=5))
    ax.xaxis.set_minor_locator(mdates.MinuteLocator(interval=1))
    ax.set_xlabel("Time", fontsize=11)
    
    plt.xticks(rotation=45)
    ax.grid(True, which='major', axis='y', color='gainsboro', linestyle=':', linewidth=0.8, zorder=0)
    ax.grid(True, which='major', axis='x', color='gainsboro', linestyle=':', linewidth=1.6, zorder=0)
    ax.grid(True, which='minor', axis='x', color='lightgray', linestyle='--', linewidth=0.6, zorder=0)
    plt.title(f"Route timetable (graphic timetable): {title_name}", fontsize=14, pad=15)
    plt.legend(title="Trains", loc='upper left', bbox_to_anchor=(1.01, 1))

    plt.tight_layout()
    display_or_save(fig, "route_timetable", title_name)

def generate_line_timetable(df, title_name):
    """Creates a classic display line timetable as a matrix table."""
    
    # Combination of arrival/departure for compact display
    df['Time'] = df['Departure'].fillna(df['Arrival'])
    
    # Pivot table: stops as rows, train numbers as columns
    timetable_table = df.pivot(index='Stop', columns='Train number', values='Time')
    
    # Restore proper sorting of stops by km
    station_order = df[['Stop', 'Km']].drop_duplicates().sort_values('Km')['Stop']
    timetable_table = timetable_table.reindex(station_order).fillna('|')

    # Visual output of the timetable as a table via Matplotlib
    fig, ax = plt.subplots(figsize=(8, len(station_order) * 0.5 + 1.5))
    ax.axis('off')

    table_data = []
    headers = ["Stop / Train"] + list(timetable_table.columns)
    
    for station, row in timetable_table.iterrows():
        table_data.append([station] + list(row.values))

    table = ax.table(cellText=table_data, colLabels=headers, loc='center', cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.8)

    # Display styling
    for (row, col), cell in table.get_celld().items():
        if row == 0:
            cell.set_facecolor('#003366')
            cell.get_text().set_color('white')
            cell.get_text().set_weight('bold')
        elif col == 0:
            cell.set_facecolor('#f2f2f2')
            cell.get_text().set_weight('bold')
            cell.get_text().set_ha('left')

    plt.title(f"Line timetable / display: {title_name}", fontsize=14, fontweight='bold', pad=20)
    plt.tight_layout()
    display_or_save(fig, "line_timetable", title_name)

if __name__ == "__main__":
    excel_file = output_path("rsna_timetable_data.xlsx")

    # 1. Create sample file (when run for the first time)
    # create_sample_excel(excel_file)

    # 2. Build the selected section from the structured station/train data.

    selected_section = "Tübingen - Reutlingen"
    timetable_df = trains_to_dataframe(TRAINS)

    # 3. Generate diagrams
    if not timetable_df.empty:
        plot_route_timetable(timetable_df, selected_section)
        generate_line_timetable(timetable_df, selected_section)
    else:
        print(f"The worksheet '{selected_section}' does not yet contain any timetable data.")