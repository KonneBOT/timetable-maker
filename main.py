from train import Train, station_code_to_id, trains_to_dataframe
from diagrams import generate_line_timetable, plot_route_timetable
from export import export_trains_txt

RS1_TUEBINGEN_ALBSTADT = {
    "name": "RS 1",
    "stops": [
        {"station_id": station_code_to_id("TT"), "arrival": None, "departure": 0, "platform": 11},
        {"station_id": station_code_to_id("TMUS"), "arrival": 2, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TDD"), "arrival": 1, "departure": 1, "platform": 2},
        #{"station_id": station_code_to_id("TST"), "arrival": 1, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TDU"), "arrival": 6, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TNEH"), "arrival": 3, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TMS"), "arrival": 2, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TBSB"), "arrival": 1, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TBOD"), "arrival": 3, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("THCH"), "arrival": 3, "departure": 3, "platform": 1},
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
        {"station_id": station_code_to_id("TLA"), "arrival": 2, "departure": 0},
        {"station_id": station_code_to_id("TLAO"), "arrival": 1, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TLAU"), "arrival": 3, "departure": 1, "platform": 1},
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
        {"station_id": station_code_to_id("TLAU"), "arrival": 3, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TLAO"), "arrival": 2, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TLA"), "arrival": 1, "departure": 0},
        {"station_id": station_code_to_id("TFR"), "arrival": 2, "departure": 1, "platform": 1},
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
        #{"station_id": station_code_to_id("TST"), "arrival": 5, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TDD"), "arrival": 6, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TMUS"), "arrival": 1, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TT"), "arrival": 2, "departure": None, "platform": 11},
    ]
}

RS2_RTS_MOESSINGEN = {
    "name": "RS 2",
    "stops": [
        {"station_id": station_code_to_id("RTS"), "arrival": None, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("RECH"), "arrival": 2, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("RALB"), "arrival": 1, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("RGA"), "arrival": 1, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("RHbfK"), "arrival": 2, "departure": 1, "platform": 22},
        {"station_id": station_code_to_id("RTW"), "arrival": 2, "departure": 1, "platform": 4},
        {"station_id": station_code_to_id("RBO"), "arrival": 1, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("RBES"), "arrival": 2, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("RBEM"), "arrival": 2, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("RBAK"), "arrival": 2, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("ROHO"), "arrival": 2, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("ROHM"), "arrival": 2, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("ROHW"), "arrival": 2, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("RGOO"), "arrival": 4, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("RGOM"), "arrival": 1, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("RGOT"), "arrival": 1, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("NSCH"), "arrival": 2, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("NMI"), "arrival": 2, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("NSU"), "arrival": 1, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TMS"), "arrival": 3, "departure": None},
    ]
}

RS2_MOESSINGEN_RTS = {
    "name": "RS 2",
    "stops": [
        {"station_id": station_code_to_id("TMS"), "arrival": None, "departure": 1},
        {"station_id": station_code_to_id("NSU"), "arrival": 2, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("NMI"), "arrival": 1, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("NSCH"), "arrival": 2, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("RGOT"), "arrival": 2, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("RGOM"), "arrival": 1, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("RGOO"), "arrival": 1, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("ROHW"), "arrival": 4, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("ROHM"), "arrival": 1, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("ROHO"), "arrival": 2, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("RBAK"), "arrival": 2, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("RBEM"), "arrival": 2, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("RBES"), "arrival": 2, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("RBO"), "arrival": 2, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("RTW"), "arrival": 1, "departure": 1, "platform": 3},
        {"station_id": station_code_to_id("RHbfK"), "arrival": 2, "departure": 1, "platform": 21},
        {"station_id": station_code_to_id("RGA"), "arrival": 2, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("RALB"), "arrival": 1, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("RECH"), "arrival": 1, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("RTS"), "arrival": 2, "departure": None, "platform": 2},
    ]
}

RE17B_TUEBINGEN_ROTTENBURG = {
    "name": "RE 17b",
    "stops": [
        {"station_id": station_code_to_id("TT"), "arrival": None, "departure": 1},
        {"station_id": station_code_to_id("TRT"), "arrival": 7, "departure": None},
    ]
}

RE17B_ROTTENBURG_TUEBINGEN = {
    "name": "RE 17b",
    "stops": [
        {"station_id": station_code_to_id("TRT"), "arrival": None, "departure": 1},
        {"station_id": station_code_to_id("TT"), "arrival": 7, "departure": None},
    ]
}

RS3_TUEBINGEN_ROTTENBURG = {
    "name": "RS 3",
    "stops": [
        {"station_id": station_code_to_id("TT"), "arrival": None, "departure": 1},
        {"station_id": station_code_to_id("TMUN"), "arrival": 2, "departure": 1, "platform": 3},
        {"station_id": station_code_to_id("TWEI"), "arrival": 1, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TKI"), "arrival": 2, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TBU"), "arrival": 2, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TKIB"), "arrival": 2, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TRTD"), "arrival": 2, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TRT"), "arrival": 1, "departure": None},
    ]
}

RS3_ROTTENBURG_TUEBINGEN = {
    "name": "RS 3",
    "stops": [
        {"station_id": station_code_to_id("TRT"), "arrival": None, "departure": 1},
        {"station_id": station_code_to_id("TRTD"), "arrival": 1, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TKIB"), "arrival": 2, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TBU"), "arrival": 2, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TKI"), "arrival": 1, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TWEI"), "arrival": 2, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TMUN"), "arrival": 1, "departure": 1, "platform": 4},
        {"station_id": station_code_to_id("TT"), "arrival": 2, "departure": 1},
    ]
}

RS4_TUEBINGEN_HERRENBERG = {
    "name": "RS 4",
    "stops": [
        {"station_id": station_code_to_id("TT"), "arrival": None, "departure": 1},
        {"station_id": station_code_to_id("TTW"), "arrival": 2, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TUJS"), "arrival": 3, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TUJM"), "arrival": 2, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TPG"), "arrival": 2, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TENT"), "arrival": 2, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TALT"), "arrival": 4, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TGU"), "arrival": 2, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TZWE"), "arrival": 2, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("THEZ"), "arrival": 2, "departure": 1, "platform": 102},
    ]
}

RS4_HERRENBERG_TUEBINGEN = {
    "name": "RS 4",
    "stops": [
        {"station_id": station_code_to_id("THEZ"), "arrival": None, "departure": 1, "platform": 102},
        {"station_id": station_code_to_id("TZWE"), "arrival": 2, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TGU"), "arrival": 2, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TALT"), "arrival": 2, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TENT"), "arrival": 2, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TPG"), "arrival": 2, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TUJM"), "arrival": 2, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TUJS"), "arrival": 1, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TTW"), "arrival": 3, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TT"), "arrival": 2, "departure": None},
    ]
}

RE17A_REUTLINGEN_ALBSTADT = {
    "name": "RE 17a",
    "stops": [
        {"station_id": station_code_to_id("TRE"), "arrival": None, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("RBE"), "arrival": 3, "departure": 0, "platform": 1},
        {"station_id": station_code_to_id("TKI"), "arrival": 1, "departure": 0, "platform": 1},
        {"station_id": station_code_to_id("TT"), "arrival": 5, "departure": 2},
        {"station_id": station_code_to_id("TMS"), "arrival": 10, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TBOD"), "arrival": 3, "departure": 0, "platform": 1},
        {"station_id": station_code_to_id("THCH"), "arrival": 3, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TBIS"), "arrival": 6, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TBG"), "arrival": 5, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TLA"), "arrival": 4, "departure": 0, "platform": 1},
        {"station_id": station_code_to_id("TAE"), "arrival": 6, "departure": None, "platform": 2},
    ]
}

RE17A_ALBSTADT_REUTLINGEN = {
    "name": "RE 17a",
    "stops": [
        {"station_id": station_code_to_id("TAE"), "arrival": None, "departure": 1},
        {"station_id": station_code_to_id("TLAU"), "arrival": 3, "departure": 0, "platform": 2},
        {"station_id": station_code_to_id("TBG"), "arrival": 8, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TBIS"), "arrival": 4, "departure": 1,"platform": 1},
        {"station_id": station_code_to_id("THCH"), "arrival": 6, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TBOD"), "arrival": 3, "departure": 0, "platform": 1},
        {"station_id": station_code_to_id("TMS"), "arrival": 3, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TT"), "arrival": 10, "departure": 2},
        {"station_id": station_code_to_id("TKI"), "arrival": 5, "departure": 0, "platform": 2},
        {"station_id": station_code_to_id("RBE"), "arrival": 1, "departure": 0, "platform": 2},
        {"station_id": station_code_to_id("TRE"), "arrival": 3, "departure": None, "platform": 1},
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

RS5_ENGSTINGEN_TUEBINGEN = {
    "name": "RS 5",
    "stops": [
        {"station_id": station_code_to_id("TKL"), "arrival": None, "departure": 0, "platform": 1},
        {"station_id": station_code_to_id("PFS"), "arrival": 1, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("PFK"), "arrival": 2, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("PFM"), "arrival": 1, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("PFB"), "arrival": 1, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("PFA"), "arrival": 2, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("RTS"), "arrival": 2, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("RECH"), "arrival": 2, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("RALB"), "arrival": 1, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("RGA"), "arrival": 2, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("RHbfK"), "arrival": 2, "departure": 1, "platform": 21},
        {"station_id": station_code_to_id("RTW"), "arrival": 2, "departure": 1, "platform": 3},
        {"station_id": station_code_to_id("RBO"), "arrival": 1, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("RBE"), "arrival": 1, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TWAN"), "arrival": 2, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TKI"), "arrival": 2, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TTN"), "arrival": 3, "departure": 1, "platform": 3},
        {"station_id": station_code_to_id("TTG"), "arrival": 2, "departure": 1, "platform": 3},
        {"station_id": station_code_to_id("TT"), "arrival": 2, "departure": None, "platform": 2},
    ],
}

RE_TUEBINGEN_REUTLINGEN = {
    "name": "RE 17",
    "stops": [
        {"station_id": station_code_to_id("TT"), "arrival": None, "departure": 0},
        {"station_id": station_code_to_id("TKI"), "arrival": 5, "departure": 0, "platform": 2},
        {"station_id": station_code_to_id("RBE"), "arrival": 1, "departure": 0, "platform": 2},
        {"station_id": station_code_to_id("TRE"), "arrival": 3, "departure": None},
    ],
}

RE_REUTLINGEN_TUEBINGEN = {
    "name": "RE 17",
    "stops": [
        {"station_id": station_code_to_id("TRE"), "arrival": None, "departure": 0},
        {"station_id": station_code_to_id("RBE"), "arrival": 3, "departure": 0, "platform": 1},
        {"station_id": station_code_to_id("TKI"), "arrival": 1, "departure": 0, "platform": 1},
        {"station_id": station_code_to_id("TT"), "arrival": 5, "departure": None}
    ]
}

MEX_TUEBINGEN_REUTLINGEN = {
    "name": "MEX 13",
    "stops": [
        {"station_id": station_code_to_id("TT"), "arrival": None, "departure": 0},
        {"station_id": station_code_to_id("TKI"), "arrival": 6, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("RBE"), "arrival": 2, "departure": 0, "platform": 2},
        {"station_id": station_code_to_id("TRE"), "arrival": 2, "departure": None},
    ],
}

MEX_REUTLINGEN_TUEBINGEN = {
    "name": "MEX 13",
    "stops": [
        {"station_id": station_code_to_id("TRE"), "arrival": None, "departure": 0},
        {"station_id": station_code_to_id("RBE"), "arrival": 2, "departure": 0, "platform": 1},
        {"station_id": station_code_to_id("TKI"), "arrival": 2, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TT"), "arrival": 5, "departure": None}
    ]
}

######################################
############# TRAIN LEGS #############
######################################
## Naming Convention (RS: 33XXX, MEX: 193XX, RE 17: 197XX, RE 17a/b: 32XX)
## RS_1: 33100 - 33169, RS_11: 33170 - 33199, RS_12: 33200-33220, RS_2: 33220 - 33229
## RS_3: 33300 - 33369, RS_31: 33370 - 33399, RS_4: 334XX, RS_5: 335XX, RS_6: 336XX, RS_7: 337XX

# Format: train_ID = Train.from_blueprint(id, blueprint, name, starttime, train_format, train_type, max_speed, penalties)
MEX_19301 = Train.from_blueprint(19301, MEX_TUEBINGEN_REUTLINGEN, "MEX 13", "5:13", "LPPLPPL", "COMMUTER", 160)
MEX_19301.set_origin(station_code_to_id("TTBW"), 2)
MEX_19301.set_ending(station_code_to_id("RTU"), 1, platform=1)
MEX_19301.change_platform(station_code_to_id("TT"), 5)
MEX_19301.change_platform(station_code_to_id("TRE"), 1)

MEX_19303 = Train.from_blueprint(19303, MEX_TUEBINGEN_REUTLINGEN, "MEX 13", "5:43", "LPPLPPL", "COMMUTER", 160)
MEX_19303.set_origin(station_code_to_id("TTBW"), 2)
MEX_19303.set_ending(station_code_to_id("RTU"), 1, platform=1)
MEX_19303.change_platform(station_code_to_id("TT"), 5)
MEX_19303.change_platform(station_code_to_id("TRE"), 1)

MEX_19305 = Train.from_blueprint(19305, MEX_TUEBINGEN_REUTLINGEN, "MEX 13", "6:13", "LPPLPPL", "COMMUTER", 160)
MEX_19305.set_origin(station_code_to_id("TTBW"), 2)
MEX_19305.set_ending(station_code_to_id("RTU"), 1, platform=1)
MEX_19305.change_platform(station_code_to_id("TT"), 5)
MEX_19305.change_platform(station_code_to_id("TRE"), 1)

MEX_19307 = Train.from_blueprint(19307, MEX_TUEBINGEN_REUTLINGEN, "MEX 13", "6:43", "LPPLPPL", "COMMUTER", 160)
MEX_19307.set_origin(station_code_to_id("TTBW"), 2)
MEX_19307.set_ending(station_code_to_id("RTU"), 1, platform=1)
MEX_19307.change_platform(station_code_to_id("TT"), 5)
MEX_19307.change_platform(station_code_to_id("TRE"), 1)

MEX_19309 = Train.from_blueprint(19309, MEX_TUEBINGEN_REUTLINGEN, "MEX 13", "7:13", "LPPLPPL", "COMMUTER", 160)
MEX_19309.set_origin(station_code_to_id("TTBW"), 2)
MEX_19309.set_ending(station_code_to_id("RTU"), 1, platform=1)
MEX_19309.change_platform(station_code_to_id("TT"), 5)
MEX_19309.change_platform(station_code_to_id("TRE"), 1)

MEX_19311 = Train.from_blueprint(19311, MEX_TUEBINGEN_REUTLINGEN, "MEX 13", "7:43", "LPPLPPL", "COMMUTER", 160)
MEX_19311.set_origin(station_code_to_id("TTBW"), 2)
MEX_19311.set_ending(station_code_to_id("RTU"), 1, platform=1)
MEX_19311.change_platform(station_code_to_id("TT"), 5)
MEX_19311.change_platform(station_code_to_id("TRE"), 1)

## RT -> Tü
MEX_19302 = Train.from_blueprint(19302, MEX_REUTLINGEN_TUEBINGEN, "MEX 13", "5:04", "LPPLPPL", "COMMUTER", 160)
MEX_19302.set_origin(station_code_to_id("RTU"),1,platform=2)
MEX_19302.set_ending(station_code_to_id("TTBW"), 2, 1)
MEX_19302.change_platform(station_code_to_id("TT"), 2)
MEX_19302.change_platform(station_code_to_id("TRE"), 2)

MEX_19304 = Train.from_blueprint(19304, MEX_REUTLINGEN_TUEBINGEN, "MEX 13", "5:34", "LPPL", "COMMUTER", 160)
MEX_19304.set_origin(station_code_to_id("RTU"),1,platform=2)
MEX_19304.set_ending(station_code_to_id("TTBW"), 2, 1)
MEX_19304.change_platform(station_code_to_id("TT"), 2)
MEX_19304.change_platform(station_code_to_id("TRE"), 2)

MEX_19306 = Train.from_blueprint(19306, MEX_REUTLINGEN_TUEBINGEN, "MEX 13", "6:04", "LPPLPL", "COMMUTER", 160)
MEX_19306.set_origin(station_code_to_id("RTU"),1,platform=2)
MEX_19306.set_ending(station_code_to_id("TTBW"), 2, 1)
MEX_19306.change_platform(station_code_to_id("TT"), 2)
MEX_19306.change_platform(station_code_to_id("TRE"), 2)

MEX_19308 = Train.from_blueprint(19308, MEX_REUTLINGEN_TUEBINGEN, "MEX 13", "6:34", "LPPLPPL", "COMMUTER", 160)
MEX_19308.set_origin(station_code_to_id("RTU"),1,platform=2)
MEX_19308.set_ending(station_code_to_id("TTBW"), 2, 1)
MEX_19308.change_platform(station_code_to_id("TT"), 2)
MEX_19308.change_platform(station_code_to_id("TRE"), 2)

MEX_19310 = Train.from_blueprint(19310, MEX_REUTLINGEN_TUEBINGEN, "MEX 13", "7:04", "LPPLPPL", "COMMUTER", 160)
MEX_19310.set_origin(station_code_to_id("RTU"),1,platform=2)
MEX_19310.set_ending(station_code_to_id("TTBW"), 2, 1)
MEX_19310.change_platform(station_code_to_id("TT"), 2)
MEX_19310.change_platform(station_code_to_id("TRE"), 2)

MEX_19312 = Train.from_blueprint(19312, MEX_REUTLINGEN_TUEBINGEN, "MEX 13", "7:34", "LPLPPL", "COMMUTER", 160)
MEX_19312.set_origin(station_code_to_id("RTU"),1,platform=2)
MEX_19312.set_ending(station_code_to_id("TTBW"), 2, 1)
MEX_19312.change_platform(station_code_to_id("TT"), 2)
MEX_19312.change_platform(station_code_to_id("TRE"), 2)

_MEX_TRAINS = [MEX_19301, MEX_19302, MEX_19303, MEX_19304, MEX_19305, MEX_19306, MEX_19307, MEX_19308, MEX_19309, MEX_19310, MEX_19311, MEX_19312]

## RE 17a
RE_3250 = Train.from_blueprint(3250, RE17A_ALBSTADT_REUTLINGEN, "RE 17a", "5:16", "LPPLPPL", "REGIONAL", 160)
RE_3250.set_origin(station_code_to_id("TAEA"), 1, platform=1)
RE_3250.change_platform(station_code_to_id("TAE"), 2)
RE_3250.set_ending(station_code_to_id("RTU"), 1, platform=1)
RE_3250.change_platform(station_code_to_id("TT"), 3)

RE_3251 = Train.from_blueprint(3251, RE17A_REUTLINGEN_ALBSTADT, "RE 17a", "5:47", "LPPLPPL", "REGIONAL", 160)
RE_3251.set_origin("RTU", 1, platform=2)
RE_3251.change_platform(station_code_to_id("TT"), 2)
RE_3251.change_platform(station_code_to_id("TBG"), 3)
RE_3251.extend_stop(station_code_to_id("TAE"), 3)

RE_3252 = Train.from_blueprint(3252, RE17A_ALBSTADT_REUTLINGEN, "RE 17a", "6:16", "LPPLPPL", "REGIONAL", 160)
RE_3252.set_origin(station_code_to_id("TAEA"), 1, platform=1)
RE_3252.change_platform(station_code_to_id("TBG"), 2)
RE_3252.set_ending(station_code_to_id("RTU"), 1, platform=1)
RE_3252.change_platform(station_code_to_id("TT"), 3)

RE_3253 = Train.from_blueprint(3253, RE17A_REUTLINGEN_ALBSTADT, "RE 17a", "6:47", "LPPLPPL", "REGIONAL", 160)
RE_3253.set_origin("RTU", 1, platform=2)
RE_3253.change_platform(station_code_to_id("TT"), 2)
RE_3253.change_platform(station_code_to_id("TBG"), 3)

RE_3254 = Train.from_blueprint(3254, RE17A_ALBSTADT_REUTLINGEN, "RE 17a", "7:15", "LPPLPPL", "REGIONAL", 160)
RE_3254.change_platform(station_code_to_id("TT"), 3)
RE_3254.change_platform(station_code_to_id("TAE"), 2)
RE_3254.change_platform(station_code_to_id("TBG"), 2)
RE_3254.extend_stop(station_code_to_id("TAE"), 2)
RE_3254.set_ending(station_code_to_id("RTU"), 1, platform=1)
RE_3251.add_leg(RE_3254)

## RE 17
RE_19701 = Train.from_blueprint(19701, RE_REUTLINGEN_TUEBINGEN, "RE 17", "5:17", "LPPL", max_speed_kmph=160)
RE_19701.set_origin(station_code_to_id("RTU"), 1, platform=2)
RE_19701.set_ending(station_code_to_id("TTBW"), 2)
RE_19701.change_platform(station_code_to_id("TT"), 2)

RE_19702 = Train.from_blueprint(19702, RE_TUEBINGEN_REUTLINGEN, "RE 17", "5:30", "LPLPL", max_speed_kmph=160)
RE_19702.set_origin(station_code_to_id("TTBW"), 2, platform=2)
RE_19702.set_ending(station_code_to_id("RTU"), 1, platform=1)
RE_19702.change_platform(station_code_to_id("TT"), 3)

RE_19703 = Train.from_blueprint(19703, RE_REUTLINGEN_TUEBINGEN, "RE 17", "6:47", "LPPLPL", max_speed_kmph=160)
RE_19703.set_origin(station_code_to_id("RTU"), 1, platform=2)
RE_19703.set_ending(station_code_to_id("TTBW"), 2)
RE_19703.change_platform(station_code_to_id("TT"), 2)

RE_19704 = Train.from_blueprint(19704, RE_TUEBINGEN_REUTLINGEN, "RE 17", "6:30", "LPL", max_speed_kmph=160)
RE_19704.set_origin(station_code_to_id("TTBW"), 2, platform=2)
RE_19704.set_ending(station_code_to_id("RTU"), 1, platform=1)
RE_19704.change_platform(station_code_to_id("TT"), 3)

_RE17_TRAINS = [RE_3250, RE_3251, RE_3252, RE_3253, RE_19701, RE_19702, RE_19703, RE_19704]

## S1 Trains
S1_33101 = Train.from_blueprint(33101, RS1_TUEBINGEN_ALBSTADT, "RS 1", "5:10", "LPL")
S1_33101.set_origin(station_code_to_id("TTBW"), 2, platform=1)
S1_33101.change_platform(station_code_to_id("TT"), 11)
S1_33101.extend_stop(station_code_to_id("TLAU"), 1)

S1_33103 = Train.from_blueprint(33103, RS1_TUEBINGEN_ALBSTADT, "RS 1", "5:39", "LPL")
S1_33103.set_origin(station_code_to_id("TTBW"), 2, platform=1)
S1_33103.change_platform(station_code_to_id("TT"), 11)
S1_33103.extend_stop(station_code_to_id("TBG"), 2) # Overtake
S1_33103.change_platform(station_code_to_id("TBG"), 1)
S1_33103.extend_stop(station_code_to_id("TFRW"), 1)
S1_33103.extend_stop(station_code_to_id("THCH"), -2)
S1_33103.extend_stop(station_code_to_id("TAEW"), 1)

S1_33105 = Train.from_blueprint(33105, RS1_TUEBINGEN_ALBSTADT, "RS 1", "6:10", "LPLPL")
S1_33105.set_origin(station_code_to_id("TTBW"), 2, platform=1)
S1_33105.change_platform(station_code_to_id("TT"), 11)
S1_33105.extend_stop(station_code_to_id("TLAU"), 1)

S1_33107 = Train.from_blueprint(33107, RS1_TUEBINGEN_ALBSTADT, "RS 1", "6:39", "LPLPL")
S1_33107.set_origin(station_code_to_id("TTBW"), 2, platform=1)
S1_33107.change_platform(station_code_to_id("TT"), 11)
S1_33107.extend_stop(station_code_to_id("TBG"), 2)
S1_33107.change_platform(station_code_to_id("TBG"), 1)
S1_33107.extend_stop(station_code_to_id("TFRW"), 1)
S1_33107.extend_stop(station_code_to_id("THCH"), -2)
S1_33107.extend_stop(station_code_to_id("TAEW"), 1)

S1_33109 = Train.from_blueprint(33109, RS1_TUEBINGEN_ALBSTADT, "RS 1", "7:10", "LPLPL")
S1_33109.set_origin(station_code_to_id("TTBW"), 2, platform=1)
S1_33109.change_platform(station_code_to_id("TT"), 11)
S1_33109.extend_stop(station_code_to_id("TLAU"), 1)

S1_33111 = Train.from_blueprint(33111, RS1_TUEBINGEN_ALBSTADT, "RS 1", "7:39", "LPLPL")
S1_33111.set_origin(station_code_to_id("TTBW"), 2, platform=1)
S1_33111.change_platform(station_code_to_id("TT"), 11)
S1_33111.extend_stop(station_code_to_id("TBG"), 2)
S1_33111.change_platform(station_code_to_id("TBG"), 1)
S1_33103.extend_stop(station_code_to_id("TFRW"), 1)
S1_33111.extend_stop(station_code_to_id("THCH"), -2)
S1_33111.extend_stop(station_code_to_id("TAEW"), 1)

S1_33102 = Train.from_blueprint(33102, RS1_ALBSTADT_TUEBINGEN, "RS 1", "5:21", "LPL")
S1_33102.change_platform(station_code_to_id("TT"), 6)
S1_33102.set_ending(station_code_to_id("TTBW"), 2)
S1_33102.extend_stop(station_code_to_id("TBG"), 1)
S1_33102.extend_stop(station_code_to_id("TBOD"), 1) # Kreuzung mit RE

S1_33104 = Train.from_blueprint(33104, RS1_ALBSTADT_TUEBINGEN, "RS 1", "5:50", "LPLPL")
S1_33104.change_platform(station_code_to_id("TT"), 6)
S1_33104.set_ending(station_code_to_id("TTBW"), 2)
S1_33104.extend_stop(station_code_to_id("TFRW"), 1)
S1_33104.extend_stop(station_code_to_id("TBOD"), 3) # overtake by RE

S1_33106 = Train.from_blueprint(33106, RS1_ALBSTADT_TUEBINGEN, "RS 1", "6:21", "LPLPL")
S1_33106.change_platform(station_code_to_id("TT"), 6)
S1_33106.set_ending(station_code_to_id("TTBW"), 2)
S1_33106.extend_stop(station_code_to_id("TLA"), 1)
S1_33106.change_platform(station_code_to_id("TLA"), 2)
S1_33106.extend_stop(station_code_to_id("TBOD"), 1)

S1_33108 = Train.from_blueprint(33108, RS1_ALBSTADT_TUEBINGEN, "RS 1", "6:50", "LPLPL")
S1_33108.change_platform(station_code_to_id("TT"), 6)
S1_33108.set_ending(station_code_to_id("TTBW"), 2)
S1_33108.extend_stop(station_code_to_id("TFRW"), 1)
S1_33108.extend_stop(station_code_to_id("TBOD"), 3) # overtake by RE

S1_33110 = Train.from_blueprint(33110, RS1_ALBSTADT_TUEBINGEN, "RS 1", "7:21", "LPLPL")
S1_33110.change_platform(station_code_to_id("TT"), 6)
S1_33110.set_ending(station_code_to_id("TTBW"), 2)
S1_33110.extend_stop(station_code_to_id("TLA"), 1)
S1_33110.change_platform(station_code_to_id("TLA"), 2)
S1_33110.extend_stop(station_code_to_id("TBOD"), 1)

S1_33112 = Train.from_blueprint(33112, RS1_ALBSTADT_TUEBINGEN, "RS 1", "7:50", "LPLPL")
S1_33112.change_platform(station_code_to_id("TT"), 6)
S1_33112.set_ending(station_code_to_id("TTBW"), 2)
S1_33112.extend_stop(station_code_to_id("TFRW"), 1)
S1_33112.extend_stop(station_code_to_id("TBOD"), 3) # overtake by RE

_S1_TRAINS = [S1_33101, S1_33102, S1_33103, S1_33104, S1_33105, S1_33106, S1_33107, S1_33108, S1_33109, S1_33110, S1_33111, S1_33112]

#################################
############# TRAINS #############
#################################

TRAINS = [
    *_MEX_TRAINS,
    *_RE17_TRAINS,
    *_S1_TRAINS
]


def main():
    selected_section = "Tübingen - Albstadt"

    timetable_df = trains_to_dataframe(TRAINS)
    if timetable_df.empty:
        print(f"The worksheet '{selected_section}' does not yet contain any timetable data.")
        return
    plot_route_timetable(timetable_df, selected_section, "06:00", 140)

    generate_line_timetable(TRAINS, selected_section, "06:00", 140)
    generate_line_timetable(TRAINS, "Betzingen - Tübingen", "06:00", 140)
    #generate_line_timetable(TRAINS, "Albstadt - Tübingen", "5:00", 140)
    print(RE_3251.timetable())
    print(RE_19703.timetable())
    export_trains_txt(TRAINS)


if __name__ == "__main__":
    main()
