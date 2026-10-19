from train import Train, station_code_to_id, trains_to_dataframe
from diagrams import generate_line_timetable, plot_route_timetable

RS1_TUEBINGEN_ALBSTADT = {
    "name": "RS 1",
    "stops": [
        {"station_id": station_code_to_id("TT"), "arrival": None, "departure": 0, "platform": 11},
        {"station_id": station_code_to_id("TMUS"), "arrival": 2, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TDD"), "arrival": 1, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TST"), "arrival": 1, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TDU"), "arrival": 5, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TNEH"), "arrival": 3, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TMS"), "arrival": 2, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TBSB"), "arrival": 1, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TBOD"), "arrival": 3, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("THCH"), "arrival": 3, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("THST"), "arrival": 2, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("THSU"), "arrival": 2, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TWEZ"), "arrival": 2, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TBIS"), "arrival": 2, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TBSH"), "arrival": 1, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TENG"), "arrival": 2, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TBG"), "arrival": 3, "departure": 1, "platform": 3},
        {"station_id": station_code_to_id("TBGM"), "arrival": 1, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TBGS"), "arrival": 1, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TENO"), "arrival": 1, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TFRW"), "arrival": 1, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TFR"), "arrival": 1, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TLAO"), "arrival": 3, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TALT"), "arrival": 3, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TAEW"), "arrival": 3, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TAEM"), "arrival": 1, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TAE"), "arrival": 1, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TAET"), "arrival": 1, "departure": None, "platform": 1},
    ]
}

RS1_ALBSTADT_TUEBINGEN = {
    "name": "RS 1",
    "stops": [
        {"station_id": station_code_to_id("TAET"), "arrival": None, "departure": 0, "platform": 1},
        {"station_id": station_code_to_id("TAE"), "arrival": 1, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TAEM"), "arrival": 1, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TAEW"), "arrival": 1, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TALT"), "arrival": 3, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TLAO"), "arrival": 2, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TFR"), "arrival": 3, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TFRW"), "arrival": 1, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TENO"), "arrival": 1, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TBGS"), "arrival": 1, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TBGM"), "arrival": 1, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TBG"), "arrival": 1, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TENG"), "arrival": 3, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TBSH"), "arrival": 2, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TBIS"), "arrival": 1, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TWEZ"), "arrival": 2, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("THSU"), "arrival": 2, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("THST"), "arrival": 2, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("THCH"), "arrival": 2, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TBOD"), "arrival": 3, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TBSB"), "arrival": 3, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TMS"), "arrival": 1, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TNEH"), "arrival": 2, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TDU"), "arrival": 3, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TST"), "arrival": 5, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TDD"), "arrival": 1, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TMUS"), "arrival": 1, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TT"), "arrival": 2, "departure": None, "platform": 11},
    ]
}

RS5_TUEBINGEN_ENGSTINGEN = {
    "name": "RS 5",
    "stops": [
        {"station_id": station_code_to_id("TT"), "arrival": None, "departure": 0, "platform": 2},
        {"station_id": station_code_to_id("TTG"), "arrival": 2, "departure": 1, "platform": 3},
        {"station_id": station_code_to_id("TTN"), "arrival": 2, "departure": 1, "platform": 3},
        {"station_id": station_code_to_id("TKI"), "arrival": 3, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TWAN"), "arrival": 2, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("RBE"), "arrival": 2, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("RBO"), "arrival": 1, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("RTW"), "arrival": 1, "departure": 1, "platform": 3},
        {"station_id": station_code_to_id("RHbfK"), "arrival": 2, "departure": 1, "platform": 21},
        {"station_id": station_code_to_id("RGA"), "arrival": 2, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("RALB"), "arrival": 1, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("RECH"), "arrival": 1, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("RTS"), "arrival": 2, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("PFA"), "arrival": 2, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("PFB"), "arrival": 1, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("PFM"), "arrival": 1, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("PFK"), "arrival": 1, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("PFS"), "arrival": 2, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TKL"), "arrival": 1, "departure": 1, "platform": 1},
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
        "1001", RS5_TUEBINGEN_ENGSTINGEN, "RS 5", "08:00",
        "LPLPL", "REGIONAL", 100, "X1",
    ),
    Train.from_blueprint(
        "1002", Train.reverse_blueprint(RS5_TUEBINGEN_ENGSTINGEN),
        "RS 5", "08:15", "LPLPL", "REGIONAL", 100, "X1",
    ),
    Train.from_blueprint(
        "1003", RS5_TUEBINGEN_ENGSTINGEN, "RS 5", "08:15",
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
