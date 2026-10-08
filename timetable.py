import os
import pandas as pd
import matplotlib

if os.environ.get("DISPLAY", "") == "" and os.name != "nt":
    matplotlib.use("Agg")

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime


def display_or_save(fig, filename_prefix, title_name):
    """Save a plot when running headless and show it otherwise."""
    safe_title = title_name.replace(" ", "_").replace("/", "_")
    filename = f"{filename_prefix}_{safe_title}.png"

    if matplotlib.get_backend().lower() == "agg":
        fig.savefig(filename, dpi=200, bbox_inches="tight")
        plt.close(fig)
    else:
        plt.show()


def create_sample_excel(filename="RS_timetable_data.xlsx"):
    """Creates a sample Excel file with data for the RS Neckar-Alb."""
    
    # Sample data for section 1: Tübingen -> Reutlingen
    sample_section_data = [
        {"Train number": "RS 1 (1001)", "Stop": "Tübingen Hbf", "Km": 0.0, "Arrival": None, "Departure": "08:00"},
        {"Train number": "RS 1 (1001)", "Stop": "Tübingen Lustnau", "Km": 2.5, "Arrival": "08:03", "Departure": "08:04"},
        {"Train number": "RS 1 (1001)", "Stop": "Kirchentellinsfurt", "Km": 7.1, "Arrival": "08:08", "Departure": "08:09"},
        {"Train number": "RS 1 (1001)", "Stop": "Wannweil", "Km": 10.4, "Arrival": "08:12", "Departure": "08:13"},
        {"Train number": "RS 1 (1001)", "Stop": "Reutlingen West", "Km": 13.8, "Arrival": "08:16", "Departure": "08:17"},
        {"Train number": "RS 1 (1001)", "Stop": "Reutlingen Hbf", "Km": 15.2, "Arrival": "08:19", "Departure": None},
        
        # Opposite direction
        {"Train number": "RS 1 (1002)", "Stop": "Reutlingen Hbf", "Km": 15.2, "Arrival": None, "Departure": "08:10"},
        {"Train number": "RS 1 (1002)", "Stop": "Reutlingen West", "Km": 13.8, "Arrival": "08:12", "Departure": "08:13"},
        {"Train number": "RS 1 (1002)", "Stop": "Wannweil", "Km": 10.4, "Arrival": "08:16", "Departure": "08:17"},
        {"Train number": "RS 1 (1002)", "Stop": "Kirchentellinsfurt", "Km": 7.1, "Arrival": "08:20", "Departure": "08:21"},
        {"Train number": "RS 1 (1002)", "Stop": "Tübingen Lustnau", "Km": 2.5, "Arrival": "08:25", "Departure": "08:26"},
        {"Train number": "RS 1 (1002)", "Stop": "Tübingen Hbf", "Km": 0.0, "Arrival": "08:29", "Departure": None},
    ]

    # Create Excel with different tabs for the sections
    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        pd.DataFrame(sample_section_data).to_excel(writer, sheet_name="Tübingen - Reutlingen", index=False)
        
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
        ax.axhline(y=row['Km'], color='lightgray', linestyle='--', linewidth=0.8, zorder=1)

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
    ax.set_xlabel("Time", fontsize=11)
    
    plt.xticks(rotation=45)
    plt.grid(True, which='both', color='gainsboro', linestyle=':', zorder=0)
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
    excel_file = "rsna_timetable_data.xlsx"

    # 1. Create sample file (when run for the first time)
    create_sample_excel(excel_file)

    # 2. Read selected section
    selected_section = "Tübingen - Reutlingen"
    timetable_df = pd.read_excel(excel_file, sheet_name=selected_section)

    # 3. Generate diagrams
    if not timetable_df.empty:
        plot_route_timetable(timetable_df, selected_section)
        generate_line_timetable(timetable_df, selected_section)
    else:
        print(f"The worksheet '{selected_section}' does not yet contain any timetable data.")