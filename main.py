from train import Train, station_code_to_id, trains_to_dataframe
from diagrams import generate_line_timetable, plot_route_timetable


RS5_TUEBINGEN_REUTLINGEN = {
    "name": "RS 5",
    "stops": [
        {"station_id": 1, "arrival": None, "departure": 0},
        {"station_id": 2, "arrival": 2, "departure": 1},
        {"station_id": 3, "arrival": 2, "departure": 1},
        {"station_id": 4, "arrival": 3, "departure": 1},
        {"station_id": 5, "arrival": 2, "departure": 1},
        {"station_id": 6, "arrival": 2, "departure": 1},
        {"station_id": 7, "arrival": 1, "departure": 1},
        {"station_id": 8, "arrival": 1, "departure": 1},
        {"station_id": 9, "arrival": 2, "departure": None},
    ],
}

RE_TUEBINGEN_REUTLINGEN = {
    "name": "RE 17",
    "stops": [
        {"station_id": station_code_to_id("TT"), "arrival": None, "departure": 0},
        {"station_id": station_code_to_id("TRE"), "arrival": 9, "departure": None},
    ],
}

MEX_TUEBINGEN_REUTLINGEN = {
    "name": "MEX 13",
    "stops": [
        {"station_id": station_code_to_id("TT"), "arrival": None, "departure": 0},
        {"station_id": station_code_to_id("TKI"), "arrival": 6, "departure": 1},
        {"station_id": station_code_to_id("TRE"), "arrival": 4, "departure": None},
    ],
}

TRAINS = [
    Train.from_blueprint(
        "1001", RS5_TUEBINGEN_REUTLINGEN, "RS 5", "08:00",
        "LPLPL", "REGIONAL", 100, "X1",
    ),
    Train.from_blueprint(
        "1002", Train.reverse_blueprint(RS5_TUEBINGEN_REUTLINGEN),
        "RS 5", "08:15", "LPLPL", "REGIONAL", 100, "X1",
    ),
    Train.from_blueprint(
        "1003", RS5_TUEBINGEN_REUTLINGEN, "RS 5", "08:15",
        "LPLPL", "REGIONAL", 100, "X1",
    ),
    Train.from_blueprint(
        "19213", MEX_TUEBINGEN_REUTLINGEN, "MEX 13", "08:17",
        "LPPPL", "COMMUTER", 120, "X1",
    ),
    Train.from_blueprint(
        "19173", RE_TUEBINGEN_REUTLINGEN, "RE 17", "08:12",
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
