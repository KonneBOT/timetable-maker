from train import Train, station_code_to_id, trains_to_dataframe
from diagrams import generate_line_timetable, plot_route_timetable


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
        {"station_id": station_code_to_id("TT"), "arrival": None, "departure": 0},
        {"station_id": station_code_to_id("TRE"), "arrival": 9, "departure": 10},
    ],
}


TRAINS = [
    Train.from_blueprint(
        "1001", RS1_TUEBINGEN_REUTLINGEN, "RS 1", "08:00",
        "LPLPL", "REGIONAL", 120, "X1",
    ),
    Train.from_blueprint(
        "1002", Train.reverse_blueprint(RS1_TUEBINGEN_REUTLINGEN),
        "RS 1", "08:15", "LPLPL", "REGIONAL", 120, "X1",
    ),
    Train.from_blueprint(
        "1003", RS1_TUEBINGEN_REUTLINGEN, "RS 1", "08:15",
        "LPLPL", "REGIONAL", 120, "X1",
    ),
    Train.from_blueprint(
        "19213", MEX_RE_TUEBINGEN_REUTLINGEN, "MEX 13", "08:17",
        "LPPPL", "COMMUTER", 120, "X1",
    ),
    Train.from_blueprint(
        "19173", MEX_RE_TUEBINGEN_REUTLINGEN, "RE 17", "08:12",
        "LPPPL", "COMMUTER", 120, "X1",
    ),
]


def main():
    selected_section = "Tübingen - Reutlingen"
    timetable_df = trains_to_dataframe(TRAINS)
    if timetable_df.empty:
        print(f"The worksheet '{selected_section}' does not yet contain any timetable data.")
        return

    plot_route_timetable(timetable_df, selected_section)
    generate_line_timetable(timetable_df, selected_section)


if __name__ == "__main__":
    main()
