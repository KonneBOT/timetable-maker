from train import Train, station_code_to_id, trains_to_dataframe
from diagrams import generate_line_timetable, plot_route_timetable, plot_station_departures
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
        {"station_id": station_code_to_id("TAET"), "arrival": 1, "departure": 1, "platform": 1},
    ]
}

RS1_ALBSTADT_TUEBINGEN = {
    "name": "RS 1",
    "stops": [
        {"station_id": station_code_to_id("TAET"), "arrival": 0, "departure": 0, "platform": 1},
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

RS11_TUEBINGEN_MOESSINGEN = {
    "name": "RS 11",
    "stops": [
        {"station_id": station_code_to_id("TT"), "arrival": None, "departure": 0, "platform": 11},
        {"station_id": station_code_to_id("TMUS"), "arrival": 2, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TDD"), "arrival": 1, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TST"), "arrival": 1, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TDU"), "arrival": 5, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TDUO"), "arrival": 1, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("NSCH"), "arrival": 2, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("NMI"), "arrival": 2, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("NSU"), "arrival": 1, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TMS"), "arrival": 2, "departure": None, "platform": 2},
    ]
}

RS11_MOESSINGEN_TUEBINGEN = {
    "name": "RS 11",
    "stops": [
        {"station_id": station_code_to_id("TMS"), "arrival": None, "departure": 0, "platform": 2},
        {"station_id": station_code_to_id("NSU"), "arrival": 2, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("NMI"), "arrival": 1, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("NSCH"), "arrival": 2, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TDUO"), "arrival": 2, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TDU"), "arrival": 1, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TST"), "arrival": 5, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TDD"), "arrival": 1, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TMUS"), "arrival": 1, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TT"), "arrival": 2, "departure": None, "platform": 11},
    ]
}

RS12_TUEBINGEN_RTS = {
    "name": "RS 12",
    "stops": [
        {"station_id": station_code_to_id("TT"), "arrival": None, "departure": 0, "platform": 11},
        {"station_id": station_code_to_id("TMUS"), "arrival": 2, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TDD"), "arrival": 1, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TST"), "arrival": 1, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TDU"), "arrival": 5, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TDUO"), "arrival": 1, "departure": 1, "platform": 2},
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
        {"station_id": station_code_to_id("RTS"), "arrival": 2, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("RTS"), "arrival": 1, "departure": 7, "platform": 3},
    ]
}

RS12_RTS_TUEBINGEN = {
    "name": "RS 12",
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
        {"station_id": station_code_to_id("ROHW"), "arrival": 2, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("RGOO"), "arrival": 4, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("RGOM"), "arrival": 1, "departure": 2, "platform": 1},
        {"station_id": station_code_to_id("RGOT"), "arrival": 1, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TDUO"), "arrival": 2, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TDU"), "arrival": 1, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TST"), "arrival": 5, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TDD"), "arrival": 1, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TMUS"), "arrival": 1, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TT"), "arrival": 2, "departure": None, "platform": 11},#
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
        {"station_id": station_code_to_id("TMS"), "arrival": 3, "departure": 3, "platform": 3},
        {"station_id": station_code_to_id("TMSA"), "arrival": 1, "departure": 0, "platform": 1},
    ]
}

RS2_MOESSINGEN_RTS = {
    "name": "RS 2",
    "stops": [
        {"station_id": station_code_to_id("TMSA"), "arrival": None, "departure": 0, "platform": 1},
        {"station_id": station_code_to_id("TMS"), "arrival": 1, "departure": 5, "platform": 3},
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

RS2_RTS_ROHW = {
    "name": "RS 2",
    "stops": [
        {"station_id": station_code_to_id("RTS"), "arrival": None, "departure": 0, "platform": 1},
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
        {"station_id": station_code_to_id("ROHA"), "arrival": 1, "departure": 0, "platform": 1},
    ]
}

RS2_ROHW_RTS = {
    "name": "RS 2",
    "stops": [
        {"station_id": station_code_to_id("ROHA"), "arrival": None, "departure": 0, "platform": 1},
        {"station_id": station_code_to_id("ROHW"), "arrival": 1, "departure": 4, "platform": 1},
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
        {"station_id": station_code_to_id("TT"), "arrival": 2, "departure": None},
    ]
}

RS31_TUEBINGENGBF_ROTTENBURG = {
    "name": "RS 31",
    "stops": [
        {"station_id": station_code_to_id("TTG"), "arrival": None, "departure": 1, "platform": 3},
        {"station_id": station_code_to_id("TT"), "arrival": 2, "departure": 1, "platform": 3},
        {"station_id": station_code_to_id("TMUN"), "arrival": 2, "departure": 1, "platform": 3},
        {"station_id": station_code_to_id("TWEI"), "arrival": 1, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TKI"), "arrival": 2, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TBU"), "arrival": 2, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TKIB"), "arrival": 2, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TRTD"), "arrival": 2, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TRT"), "arrival": 1, "departure": None},
    ]
}

RS31_ROTTENBURG_TUEBINGENGBF = {
    "name": "RS 31",
    "stops": [
        {"station_id": station_code_to_id("TRT"), "arrival": None, "departure": 1},
        {"station_id": station_code_to_id("TRTD"), "arrival": 1, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TKIB"), "arrival": 2, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TBU"), "arrival": 2, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TKI"), "arrival": 1, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TWEI"), "arrival": 2, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TMUN"), "arrival": 1, "departure": 1, "platform": 4},
        {"station_id": station_code_to_id("TT"), "arrival": 2, "departure": 1},
        {"station_id": station_code_to_id("TTG"), "arrival": 2, "departure": None, "platform": 3},
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
        {"station_id": station_code_to_id("TRE"), "arrival": 3, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("RTU"), "arrival": 1, "departure": 0, "platform": 1}
    ],
}

RE_REUTLINGEN_TUEBINGEN = {
    "name": "RE 17",
    "stops": [
        {"station_id": station_code_to_id("RTU"), "arrival": None, "departure": 0, "platform": 2},
        {"station_id": station_code_to_id("TRE"), "arrival": 1, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("RBE"), "arrival": 3, "departure": 0, "platform": 1},
        {"station_id": station_code_to_id("TKI"), "arrival": 1, "departure": 0, "platform": 1},
        {"station_id": station_code_to_id("TT"), "arrival": 5, "departure": None}
    ]
}

RE17A_REUTLINGEN_ALBSTADT = {
    "name": "RE 17a",
    "stops": [
        {"station_id": station_code_to_id("RTU"), "arrival": None, "departure": 0, "platform": 2},
        {"station_id": station_code_to_id("TRE"), "arrival": 1, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("RBE"), "arrival": 3, "departure": 0, "platform": 1},
        {"station_id": station_code_to_id("TKI"), "arrival": 1, "departure": 0, "platform": 1},
        {"station_id": station_code_to_id("TT"), "arrival": 5, "departure": 2},
        {"station_id": station_code_to_id("TMS"), "arrival": 10, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TBOD"), "arrival": 3, "departure": 0, "platform": 1},
        {"station_id": station_code_to_id("THCH"), "arrival": 3, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TBIS"), "arrival": 6, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TBG"), "arrival": 4, "departure": 1, "platform": 3},
        {"station_id": station_code_to_id("TLA"), "arrival": 4, "departure": 0, "platform": 1},
        {"station_id": station_code_to_id("TAE"), "arrival": 6, "departure": None, "platform": 2},
    ]
}

RE17A_ALBSTADT_REUTLINGEN = {
    "name": "RE 17a",
    "stops": [
        {"station_id": station_code_to_id("TAE"), "arrival": None, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TLAU"), "arrival": 3, "departure": 0, "platform": 2},
        {"station_id": station_code_to_id("TBG"), "arrival": 8, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TBIS"), "arrival": 4, "departure": 1,"platform": 1},
        {"station_id": station_code_to_id("THCH"), "arrival": 6, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("TBOD"), "arrival": 3, "departure": 0, "platform": 1},
        {"station_id": station_code_to_id("TMS"), "arrival": 3, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TT"), "arrival": 10, "departure": 2},
        {"station_id": station_code_to_id("TKI"), "arrival": 5, "departure": 0, "platform": 2},
        {"station_id": station_code_to_id("RBE"), "arrival": 1, "departure": 0, "platform": 2},
        {"station_id": station_code_to_id("TRE"), "arrival": 3, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("RTU"), "arrival": 1, "departure": None, "platform": 1}
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

MEX_TUEBINGEN_REUTLINGEN = {
    "name": "MEX 13",
    "stops": [
        {"station_id": station_code_to_id("TT"), "arrival": None, "departure": 0, "platform": 5},
        {"station_id": station_code_to_id("TKI"), "arrival": 6, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("RBE"), "arrival": 2, "departure": 0, "platform": 2},
        {"station_id": station_code_to_id("TRE"), "arrival": 2, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("RTU"), "arrival": 1, "departure": 0, "platform": 1}
    ],
}

MEX_REUTLINGEN_TUEBINGEN = {
    "name": "MEX 13",
    "stops": [
        {"station_id": station_code_to_id("RTU"), "arrival": None, "departure": 0, "platform": 2},
        {"station_id": station_code_to_id("TRE"), "arrival": 1, "departure": 1, "platform": 2},
        {"station_id": station_code_to_id("RBE"), "arrival": 2, "departure": 0, "platform": 1},
        {"station_id": station_code_to_id("TKI"), "arrival": 2, "departure": 1, "platform": 1},
        {"station_id": station_code_to_id("TT"), "arrival": 5, "departure": None, "platform": 5}
    ]
}

######################################
############# TRAIN LEGS #############
######################################
## Naming Convention (RS: 33XXX, MEX: 193XX, RE 17: 197XX, RE 17a/b: 32XX)
## RS_1: 33100 - 33169, RS_11: 33170 - 33199, RS_12: 33200-33220, RS_2: 33220 - 33229
## RS_3: 33300 - 33369, RS_31: 33370 - 33399, RS_4: 334XX, RS_5: 335XX, RS_6: 336XX, RS_7: 337XX

# Format: train_ID = Train.from_blueprint(id, blueprint, name, starttime, train_format, train_type, max_speed, penalties)
MEX_19301 = Train.from_blueprint(19301, MEX_TUEBINGEN_REUTLINGEN, "MEX 13", "5:11", "LPPLPPL", "REGIONAL", 160)
MEX_19301.set_origin(station_code_to_id("TTBW"), 2)
MEX_19301.change_platform(station_code_to_id("TT"), 5)
MEX_19301.extend_stop(station_code_to_id("TT"), 1)

MEX_19303 = Train.from_blueprint(19303, MEX_TUEBINGEN_REUTLINGEN, "MEX 13", "5:40", "LPPLPPL", "REGIONAL", 160)
MEX_19303.extend_stop(station_code_to_id("TT"), 3)

MEX_19305 = Train.from_blueprint(19305, MEX_TUEBINGEN_REUTLINGEN, "MEX 13", "6:10", "LPPLPPL", "REGIONAL", 160)
MEX_19305.extend_stop(station_code_to_id("TT"), 3)

MEX_19307 = Train.from_blueprint(19307, MEX_TUEBINGEN_REUTLINGEN, "MEX 13", "6:40", "LPPLPPL", "REGIONAL", 160)
MEX_19307.extend_stop(station_code_to_id("TT"), 3)

MEX_19309 = Train.from_blueprint(19309, MEX_TUEBINGEN_REUTLINGEN, "MEX 13", "7:10", "LPPLPPL", "REGIONAL", 160)
MEX_19309.extend_stop(station_code_to_id("TT"), 3)

MEX_19311 = Train.from_blueprint(19311, MEX_TUEBINGEN_REUTLINGEN, "MEX 13", "7:40", "LPPLPPL", "REGIONAL", 160)
MEX_19311.extend_stop(station_code_to_id("TT"), 3)

MEX_19313 = Train.from_blueprint(19313, MEX_TUEBINGEN_REUTLINGEN, "MEX 13", "8:10", "LPPLPPL", "REGIONAL", 160)
MEX_19313.extend_stop(station_code_to_id("TT"), 3)

MEX_19315 = Train.from_blueprint(19315, MEX_TUEBINGEN_REUTLINGEN, "MEX 13", "8:40", "LPPLPPL", "REGIONAL", 160)
MEX_19315.extend_stop(station_code_to_id("TT"), 3)

MEX_19317 = Train.from_blueprint(19317, MEX_TUEBINGEN_REUTLINGEN, "MEX 13", "9:10", "LPPLPPL", "REGIONAL", 160)
MEX_19317.extend_stop(station_code_to_id("TT"), 3)

MEX_19319 = Train.from_blueprint(19319, MEX_TUEBINGEN_REUTLINGEN, "MEX 13", "9:40", "LPPLPPL", "REGIONAL", 160)
MEX_19319.extend_stop(station_code_to_id("TT"), 3)

MEX_19321 = Train.from_blueprint(19321, MEX_TUEBINGEN_REUTLINGEN, "MEX 13", "10:40", "LPPLPPL", "REGIONAL", 160)
MEX_19321.extend_stop(station_code_to_id("TT"), 3)

MEX_19323 = Train.from_blueprint(19323, MEX_TUEBINGEN_REUTLINGEN, "MEX 13", "10:40", "LPPLPPL", "REGIONAL", 160)
MEX_19323.extend_stop(station_code_to_id("TT"), 3)

## RT -> Tü
MEX_19302 = Train.from_blueprint(19302, MEX_REUTLINGEN_TUEBINGEN, "MEX 13", "5:04", "LPPLPPL", "REGIONAL", 160)
MEX_19302.extend_stop(station_code_to_id("TT"), 4)
MEX_19302.add_leg(MEX_19303)

MEX_19304 = Train.from_blueprint(19304, MEX_REUTLINGEN_TUEBINGEN, "MEX 13", "5:34", "LPPL", "REGIONAL", 160)
MEX_19304.extend_stop(station_code_to_id("TT"), 4)
MEX_19304.add_leg(MEX_19305)

MEX_19306 = Train.from_blueprint(19306, MEX_REUTLINGEN_TUEBINGEN, "MEX 13", "6:04", "LPPLPL", "REGIONAL", 160)
MEX_19306.extend_stop(station_code_to_id("TT"), 4)
MEX_19306.add_leg(MEX_19307)

MEX_19308 = Train.from_blueprint(19308, MEX_REUTLINGEN_TUEBINGEN, "MEX 13", "6:34", "LPPLPPL", "REGIONAL", 160)
MEX_19308.extend_stop(station_code_to_id("TT"), 4)
MEX_19308.add_leg(MEX_19309)

MEX_19310 = Train.from_blueprint(19310, MEX_REUTLINGEN_TUEBINGEN, "MEX 13", "7:04", "LPPLPPL", "REGIONAL", 160)
MEX_19310.extend_stop(station_code_to_id("TT"), 4)
MEX_19310.add_leg(MEX_19311)

MEX_19312 = Train.from_blueprint(19312, MEX_REUTLINGEN_TUEBINGEN, "MEX 13", "7:34", "LPLPPL", "REGIONAL", 160)
MEX_19312.extend_stop(station_code_to_id("TT"), 4)
MEX_19312.add_leg(MEX_19313)

MEX_19314 = Train.from_blueprint(19314, MEX_REUTLINGEN_TUEBINGEN, "MEX 13", "8:04", "LPPLPPL", "REGIONAL", 160)
MEX_19314.extend_stop(station_code_to_id("TT"), 4)
MEX_19314.add_leg(MEX_19315)

MEX_19316 = Train.from_blueprint(19316, MEX_REUTLINGEN_TUEBINGEN, "MEX 13", "8:34", "LPLPPL", "REGIONAL", 160)
MEX_19316.extend_stop(station_code_to_id("TT"), 4)
MEX_19316.add_leg(MEX_19317)

MEX_19318 = Train.from_blueprint(19318, MEX_REUTLINGEN_TUEBINGEN, "MEX 13", "9:04", "LPPLPPL", "REGIONAL", 160)
MEX_19318.extend_stop(station_code_to_id("TT"), 4)
MEX_19318.add_leg(MEX_19319)

MEX_19320 = Train.from_blueprint(19320, MEX_REUTLINGEN_TUEBINGEN, "MEX 13", "9:34", "LPLPPL", "REGIONAL", 160)
MEX_19320.extend_stop(station_code_to_id("TT"), 4)
MEX_19320.add_leg(MEX_19321)

MEX_19322 = Train.from_blueprint(19322, MEX_REUTLINGEN_TUEBINGEN, "MEX 13", "10:04", "LPPLPPL", "REGIONAL", 160)
MEX_19322.extend_stop(station_code_to_id("TT"), 4)
MEX_19322.add_leg(MEX_19323)

MEX_19324 = Train.from_blueprint(19324, MEX_REUTLINGEN_TUEBINGEN, "MEX 13", "10:34", "LPLPPL", "REGIONAL", 160)
MEX_19324.set_ending(station_code_to_id("TTBW"), 2, 1)
MEX_19324.extend_stop(station_code_to_id("TT"), 4)

MEX_TRAINS = [MEX_19301, MEX_19302, MEX_19303, MEX_19304, MEX_19305, MEX_19306, MEX_19307, MEX_19308, MEX_19309, 
               MEX_19310, MEX_19311, MEX_19312, MEX_19313, MEX_19314, MEX_19315, MEX_19316, MEX_19317, MEX_19318, 
               MEX_19319, MEX_19320, MEX_19321, MEX_19322, MEX_19323, MEX_19324]

_MEX_TRAINS = [train for train in MEX_TRAINS if train._leg_parent is None]

## RE 17a
RE_3250 = Train.from_blueprint(3250, RE17A_ALBSTADT_REUTLINGEN, "RE 17a", "5:15", "LPPLPPL", "REGIONAL", 160)
RE_3250.set_origin(station_code_to_id("TAEA"), 1, platform=2)
RE_3250.change_platform(station_code_to_id("TT"), 3)

RE_3251 = Train.from_blueprint(3251, RE17A_REUTLINGEN_ALBSTADT, "RE 17a", "5:47", "LPPLPPL", "REGIONAL", 160)
RE_3251.change_platform(station_code_to_id("TT"), 2)
RE_3251.change_platform(station_code_to_id("TBG"), 3)
RE_3251.extend_stop(station_code_to_id("TAE"), 3)

RE_3252 = Train.from_blueprint(3252, RE17A_ALBSTADT_REUTLINGEN, "RE 17a", "6:15", "LPPLPPL", "REGIONAL", 160)
RE_3252.set_origin(station_code_to_id("TAEA"), 1, platform=2)
RE_3252.change_platform(station_code_to_id("TBG"), 2)
RE_3252.change_platform(station_code_to_id("TT"), 3)

RE_3253 = Train.from_blueprint(3253, RE17A_REUTLINGEN_ALBSTADT, "RE 17a", "6:47", "LPPLPPL", "REGIONAL", 160)
RE_3253.change_platform(station_code_to_id("TT"), 2)
RE_3253.set_ending(station_code_to_id("TAEA"), 1, platform=2)
RE_3253.extend_stop(station_code_to_id("TAE"), 3)
RE_3253.change_platform(station_code_to_id("TBG"), 3)

RE_3254 = Train.from_blueprint(3254, RE17A_ALBSTADT_REUTLINGEN, "RE 17a", "7:14", "LPPLPPL", "REGIONAL", 160)
RE_3254.change_platform(station_code_to_id("TT"), 3)
RE_3254.change_platform(station_code_to_id("TBG"), 2)
RE_3254.extend_stop(station_code_to_id("TAE"), 2)
RE_3251.add_leg(RE_3254)

RE_3255 = Train.from_blueprint(3255, RE17A_REUTLINGEN_ALBSTADT, "RE 17a", "7:47", "LPPLPPL", "REGIONAL", 160)
RE_3255.change_platform(station_code_to_id("TT"), 2)
RE_3255.set_ending(station_code_to_id("TAEA"), 1, platform=2)
RE_3255.extend_stop(station_code_to_id("TAE"), 3)
RE_3255.change_platform(station_code_to_id("TBG"), 3)

RE_3256 = Train.from_blueprint(3254, RE17A_ALBSTADT_REUTLINGEN, "RE 17a", "8:14", "LPPLPPL", "REGIONAL", 160)
RE_3256.change_platform(station_code_to_id("TT"), 3)
RE_3256.change_platform(station_code_to_id("TBG"), 2)
RE_3256.extend_stop(station_code_to_id("TAE"), 2)
RE_3253.add_leg(RE_3256)

RE_3257 = Train.from_blueprint(3257, RE17A_REUTLINGEN_ALBSTADT, "RE 17a", "8:47", "LPPLPPL", "REGIONAL", 160)
RE_3257.change_platform(station_code_to_id("TT"), 2)
RE_3257.set_ending(station_code_to_id("TAEA"), 1, platform=2)
RE_3257.extend_stop(station_code_to_id("TAE"), 3)
RE_3257.change_platform(station_code_to_id("TBG"), 3)

RE_3258 = Train.from_blueprint(3258, RE17A_ALBSTADT_REUTLINGEN, "RE 17a", "9:14", "LPPLPPL", "REGIONAL", 160)
RE_3258.change_platform(station_code_to_id("TT"), 3)
RE_3258.change_platform(station_code_to_id("TBG"), 2)
RE_3258.extend_stop(station_code_to_id("TAE"), 2)
RE_3255.add_leg(RE_3258)

RE_3259 = Train.from_blueprint(3259, RE17A_REUTLINGEN_ALBSTADT, "RE 17a", "9:47", "LPPLPPL", "REGIONAL", 160)
RE_3259.change_platform(station_code_to_id("TT"), 2)
RE_3259.set_ending(station_code_to_id("TAEA"), 1, platform=2)
RE_3259.extend_stop(station_code_to_id("TAE"), 3)
RE_3259.change_platform(station_code_to_id("TBG"), 3)

RE_3260 = Train.from_blueprint(3260, RE17A_ALBSTADT_REUTLINGEN, "RE 17a", "10:14", "LPPLPPL", "REGIONAL", 160)
RE_3260.change_platform(station_code_to_id("TT"), 3)
RE_3260.change_platform(station_code_to_id("TBG"), 2)
RE_3260.extend_stop(station_code_to_id("TAE"), 2)
RE_3257.add_leg(RE_3260)

## RE 17
RE_19701 = Train.from_blueprint(19701, RE_REUTLINGEN_TUEBINGEN, "RE 17", "5:19", "LPPL", max_speed_kmph=160)
RE_19701.change_platform(station_code_to_id("TT"), 9)
RE_19701.extend_stop(station_code_to_id("TT"), 5)

RE_19702 = Train.from_blueprint(19702, RE_TUEBINGEN_REUTLINGEN, "RE 17", "5:27", "LPPL", max_speed_kmph=160)
RE_19702.set_origin(station_code_to_id("TTBW"), 2, platform=2)
RE_19702.change_platform(station_code_to_id("TT"), 3)

RE_19703 = Train.from_blueprint(19703, RE_REUTLINGEN_TUEBINGEN, "RE 17", "6:19", "LPPL", max_speed_kmph=160)
RE_19703.change_platform(station_code_to_id("TT"), 9)
RE_19703.extend_stop(station_code_to_id("TT"), 5)

RE_19704 = Train.from_blueprint(19704, RE_TUEBINGEN_REUTLINGEN, "RE 17", "6:27", "LPPL", max_speed_kmph=160)
RE_19704.set_origin(station_code_to_id("TTBW"), 2, platform=2)
RE_19704.change_platform(station_code_to_id("TT"), 3)
RE_19701.add_leg(RE_19704)

RE_19705 = Train.from_blueprint(19705, RE_REUTLINGEN_TUEBINGEN, "RE 17", "7:19", "LPPL", max_speed_kmph=160)
RE_19705.change_platform(station_code_to_id("TT"), 9)
RE_19705.extend_stop(station_code_to_id("TT"), 5)

RE_19706 = Train.from_blueprint(19706, RE_TUEBINGEN_REUTLINGEN, "RE 17", "7:26", "LPPL", max_speed_kmph=160)
RE_19706.extend_stop(station_code_to_id("TT"), 2)
RE_19706.change_platform(station_code_to_id("TT"), 9)
RE_19703.add_leg(RE_19706)

RE_19707 = Train.from_blueprint(19707, RE_REUTLINGEN_TUEBINGEN, "RE 17", "8:19", "LPPL", max_speed_kmph=160)
RE_19707.change_platform(station_code_to_id("TT"), 9)
RE_19707.extend_stop(station_code_to_id("TT"), 5)

RE_19708 = Train.from_blueprint(19708, RE_TUEBINGEN_REUTLINGEN, "RE 17", "8:26", "LPPL", max_speed_kmph=160)
RE_19708.extend_stop(station_code_to_id("TT"), 2)
RE_19708.change_platform(station_code_to_id("TT"), 9)
RE_19705.add_leg(RE_19708)

RE_19709 = Train.from_blueprint(19709, RE_REUTLINGEN_TUEBINGEN, "RE 17", "9:19", "LPPL", max_speed_kmph=160)
RE_19709.change_platform(station_code_to_id("TT"), 9)
RE_19709.extend_stop(station_code_to_id("TT"), 5)

RE_19710 = Train.from_blueprint(19710, RE_TUEBINGEN_REUTLINGEN, "RE 17", "9:26", "LPPL", max_speed_kmph=160)
RE_19710.extend_stop(station_code_to_id("TT"), 2)
RE_19710.change_platform(station_code_to_id("TT"), 9)
RE_19707.add_leg(RE_19710)

RE_19711 = Train.from_blueprint(19711, RE_REUTLINGEN_TUEBINGEN, "RE 17", "10:19", "LPPL", max_speed_kmph=160)
RE_19711.set_ending(station_code_to_id("TTBW"), 2)
RE_19711.change_platform(station_code_to_id("TT"), 2)

RE_19712 = Train.from_blueprint(19712, RE_TUEBINGEN_REUTLINGEN, "RE 17", "10:26", "LPPL", max_speed_kmph=160)
RE_19712.extend_stop(station_code_to_id("TT"), 2)
RE_19712.change_platform(station_code_to_id("TT"), 9)
RE_19709.add_leg(RE_19712)

RE17_TRAINS = [RE_3250, RE_3251, RE_3252, RE_3253, RE_3254, RE_3255, RE_3256, RE_3257, RE_3258, RE_3259, RE_3260,
                RE_19702, RE_19703, RE_19704, RE_19705, RE_19706, RE_19707, RE_19708, RE_19709, RE_19710, RE_19711, RE_19712]

_RE17_TRAINS = [train for train in RE17_TRAINS if train._leg_parent is None]

## S1 Trains
S1_33101 = Train.from_blueprint(33101, RS1_TUEBINGEN_ALBSTADT, "RS 1", "5:09", "LPL")
S1_33101.set_origin(station_code_to_id("TTBW"), 2, platform=1)
S1_33101.change_platform(station_code_to_id("TT"), 11)
S1_33101.extend_stop(station_code_to_id("TLAU"), 1)

S1_33103 = Train.from_blueprint(33103, RS1_TUEBINGEN_ALBSTADT, "RS 1", "5:38", "LPL")
S1_33103.set_origin(station_code_to_id("TTBW"), 2, platform=1)
S1_33103.change_platform(station_code_to_id("TT"), 11)
S1_33103.extend_stop(station_code_to_id("TBG"), 2) # Overtake
S1_33103.change_platform(station_code_to_id("TBG"), 1)
#S1_33103.extend_stop(station_code_to_id("TFRW"), 1)
S1_33103.extend_stop(station_code_to_id("THCH"), -2)
S1_33103.extend_stop(station_code_to_id("TAEW"), 1)

S1_33105 = Train.from_blueprint(33105, RS1_TUEBINGEN_ALBSTADT, "RS 1", "6:09", "LPLPL")
S1_33105.set_origin(station_code_to_id("TTBW"), 2, platform=1)
S1_33105.change_platform(station_code_to_id("TT"), 11)
S1_33105.extend_stop(station_code_to_id("TLAU"), 1)

S1_33107 = Train.from_blueprint(33107, RS1_TUEBINGEN_ALBSTADT, "RS 1", "6:38", "LPLPL")
S1_33107.set_origin(station_code_to_id("TTBW"), 2, platform=1)
S1_33107.change_platform(station_code_to_id("TT"), 11)
S1_33107.extend_stop(station_code_to_id("TBG"), 2)
S1_33107.change_platform(station_code_to_id("TBG"), 1)
S1_33107.extend_stop(station_code_to_id("TFRW"), 1)
S1_33107.extend_stop(station_code_to_id("THCH"), -2)
S1_33107.extend_stop(station_code_to_id("TAEW"), 1)

S1_33109 = Train.from_blueprint(33109, RS1_TUEBINGEN_ALBSTADT, "RS 1", "7:09", "LPLPL")
S1_33109.set_origin(station_code_to_id("TTBW"), 2, platform=1)
S1_33109.change_platform(station_code_to_id("TT"), 11)
S1_33109.extend_stop(station_code_to_id("TLAU"), 1)

S1_33111 = Train.from_blueprint(33111, RS1_TUEBINGEN_ALBSTADT, "RS 1", "7:38", "LPLPL")
S1_33111.set_origin(station_code_to_id("TTBW"), 2, platform=1)
S1_33111.change_platform(station_code_to_id("TT"), 11)
S1_33111.extend_stop(station_code_to_id("TBG"), 2)
S1_33111.change_platform(station_code_to_id("TBG"), 1)
S1_33111.extend_stop(station_code_to_id("TFRW"), 1)
S1_33111.extend_stop(station_code_to_id("THCH"), -2)
S1_33111.extend_stop(station_code_to_id("TAEW"), 1)

S1_33113 = Train.from_blueprint(33113, RS1_TUEBINGEN_ALBSTADT, "RS 1", "8:09", "LPLPL")
S1_33113.set_origin(station_code_to_id("TTBW"), 2, platform=1)
S1_33113.change_platform(station_code_to_id("TT"), 11)
S1_33113.extend_stop(station_code_to_id("TLAU"), 1)

S1_33115 = Train.from_blueprint(33111, RS1_TUEBINGEN_ALBSTADT, "RS 1", "8:38", "LPLPL")
S1_33115.set_origin(station_code_to_id("TTBW"), 2, platform=1)
S1_33115.change_platform(station_code_to_id("TT"), 11)
S1_33115.extend_stop(station_code_to_id("TBG"), 2)
S1_33115.change_platform(station_code_to_id("TBG"), 1)
S1_33115.extend_stop(station_code_to_id("TFRW"), 1)
S1_33115.extend_stop(station_code_to_id("THCH"), -2)
S1_33115.extend_stop(station_code_to_id("TAEW"), 1)

S1_33113 = Train.from_blueprint(33113, RS1_TUEBINGEN_ALBSTADT, "RS 1", "8:09", "LPLPL")
S1_33113.set_origin(station_code_to_id("TTBW"), 2, platform=1)
S1_33113.change_platform(station_code_to_id("TT"), 11)
S1_33113.extend_stop(station_code_to_id("TLAU"), 1)

S1_33115 = Train.from_blueprint(33115, RS1_TUEBINGEN_ALBSTADT, "RS 1", "8:38", "LPLPL")
S1_33115.set_origin(station_code_to_id("TTBW"), 2, platform=1)
S1_33115.change_platform(station_code_to_id("TT"), 11)
S1_33115.extend_stop(station_code_to_id("TBG"), 2)
S1_33115.change_platform(station_code_to_id("TBG"), 1)
S1_33115.extend_stop(station_code_to_id("TFRW"), 1)
S1_33115.extend_stop(station_code_to_id("THCH"), -2)
S1_33115.extend_stop(station_code_to_id("TAEW"), 1)

S1_33117 = Train.from_blueprint(33117, RS1_TUEBINGEN_ALBSTADT, "RS 1", "9:09", "LPLPL")
S1_33117.set_origin(station_code_to_id("TTBW"), 2, platform=1)
S1_33117.change_platform(station_code_to_id("TT"), 11)
S1_33117.extend_stop(station_code_to_id("TLAU"), 1)

S1_33119 = Train.from_blueprint(33119, RS1_TUEBINGEN_ALBSTADT, "RS 1", "9:38", "LPLPL")
S1_33119.set_origin(station_code_to_id("TTBW"), 2, platform=1)
S1_33119.change_platform(station_code_to_id("TT"), 11)
S1_33119.extend_stop(station_code_to_id("TBG"), 2)
S1_33119.change_platform(station_code_to_id("TBG"), 1)
S1_33119.extend_stop(station_code_to_id("TFRW"), 1)
S1_33119.extend_stop(station_code_to_id("THCH"), -2)
S1_33119.extend_stop(station_code_to_id("TAEW"), 1)

S1_33121 = Train.from_blueprint(33121, RS1_TUEBINGEN_ALBSTADT, "RS 1", "10:09", "LPLPL")
S1_33121.set_origin(station_code_to_id("TTBW"), 2, platform=1)
S1_33121.change_platform(station_code_to_id("TT"), 11)
S1_33121.extend_stop(station_code_to_id("TBG"), 2)
S1_33121.change_platform(station_code_to_id("TBG"), 1)
S1_33121.extend_stop(station_code_to_id("TFRW"), 1)
S1_33121.extend_stop(station_code_to_id("THCH"), -2)
S1_33121.extend_stop(station_code_to_id("TAEW"), 1)

S1_33123 = Train.from_blueprint(33123, RS1_TUEBINGEN_ALBSTADT, "RS 1", "10:38", "LPLPL")
S1_33123.set_origin(station_code_to_id("TTBW"), 2, platform=1)
S1_33123.change_platform(station_code_to_id("TT"), 11)
S1_33123.extend_stop(station_code_to_id("TLAU"), 1)

#######################

S1_33102 = Train.from_blueprint(33102, RS1_ALBSTADT_TUEBINGEN, "RS 1", "5:20", "LPL")
S1_33102.change_platform(station_code_to_id("TT"), 6)
S1_33102.set_ending(station_code_to_id("TTBW"), 2)
S1_33102.extend_stop(station_code_to_id("TBG"), 1)
S1_33102.extend_stop(station_code_to_id("TBOD"), 1) # Kreuzung mit RE

S1_33104 = Train.from_blueprint(33104, RS1_ALBSTADT_TUEBINGEN, "RS 1", "5:49", "LPLPL")
S1_33104.change_platform(station_code_to_id("TT"), 6)
S1_33104.set_ending(station_code_to_id("TTBW"), 2)
S1_33104.extend_stop(station_code_to_id("TFRW"), 1)
S1_33104.extend_stop(station_code_to_id("TBOD"), 3) # overtake by RE

S1_33106 = Train.from_blueprint(33106, RS1_ALBSTADT_TUEBINGEN, "RS 1", "6:20", "LPLPL")
S1_33106.change_platform(station_code_to_id("TT"), 6)
S1_33106.set_ending(station_code_to_id("TTBW"), 2)
S1_33106.extend_stop(station_code_to_id("TLA"), 1)
S1_33106.change_platform(station_code_to_id("TLA"), 2)
S1_33106.extend_stop(station_code_to_id("TBOD"), 1)

S1_33108 = Train.from_blueprint(33108, RS1_ALBSTADT_TUEBINGEN, "RS 1", "6:49", "LPLPL")
S1_33108.change_platform(station_code_to_id("TT"), 6)
S1_33108.set_ending(station_code_to_id("TTBW"), 2)
S1_33108.extend_stop(station_code_to_id("TFRW"), 1)
S1_33108.extend_stop(station_code_to_id("TBOD"), 3) # overtake by RE

S1_33110 = Train.from_blueprint(33110, RS1_ALBSTADT_TUEBINGEN, "RS 1", "7:20", "LPLPL")
S1_33110.change_platform(station_code_to_id("TT"), 6)
S1_33110.set_ending(station_code_to_id("TTBW"), 2)
S1_33110.extend_stop(station_code_to_id("TLA"), 1)
S1_33110.change_platform(station_code_to_id("TLA"), 2)
S1_33110.extend_stop(station_code_to_id("TBOD"), 1)

S1_33112 = Train.from_blueprint(33112, RS1_ALBSTADT_TUEBINGEN, "RS 1", "7:49", "LPLPL")
S1_33112.change_platform(station_code_to_id("TT"), 6)
S1_33112.set_ending(station_code_to_id("TTBW"), 2)
S1_33112.extend_stop(station_code_to_id("TFRW"), 1)
S1_33112.extend_stop(station_code_to_id("TBOD"), 3) # overtake by RE

S1_33114 = Train.from_blueprint(33114, RS1_ALBSTADT_TUEBINGEN, "RS 1", "8:20", "LPLPL")
S1_33114.change_platform(station_code_to_id("TT"), 6)
S1_33114.set_ending(station_code_to_id("TTBW"), 2)
S1_33114.extend_stop(station_code_to_id("TLA"), 1)
S1_33114.change_platform(station_code_to_id("TLA"), 2)
S1_33114.extend_stop(station_code_to_id("TBOD"), 1)

S1_33116 = Train.from_blueprint(33116, RS1_ALBSTADT_TUEBINGEN, "RS 1", "8:49", "LPLPL")
S1_33116.change_platform(station_code_to_id("TT"), 6)
S1_33116.set_ending(station_code_to_id("TTBW"), 2)
S1_33116.extend_stop(station_code_to_id("TFRW"), 1)
S1_33116.extend_stop(station_code_to_id("TBOD"), 3) # overtake by RE

S1_33118 = Train.from_blueprint(33118, RS1_ALBSTADT_TUEBINGEN, "RS 1", "9:20", "LPLPL")
S1_33118.change_platform(station_code_to_id("TT"), 6)
S1_33118.set_ending(station_code_to_id("TTBW"), 2)
S1_33118.extend_stop(station_code_to_id("TLA"), 1)
S1_33118.change_platform(station_code_to_id("TLA"), 2)
S1_33118.extend_stop(station_code_to_id("TBOD"), 1)

S1_33120 = Train.from_blueprint(33120, RS1_ALBSTADT_TUEBINGEN, "RS 1", "9:49", "LPLPL")
S1_33120.change_platform(station_code_to_id("TT"), 6)
S1_33120.set_ending(station_code_to_id("TTBW"), 2)
S1_33120.extend_stop(station_code_to_id("TFRW"), 1)
S1_33120.extend_stop(station_code_to_id("TBOD"), 3) # overtake by RE

S1_33122 = Train.from_blueprint(33122, RS1_ALBSTADT_TUEBINGEN, "RS 1", "10:20", "LPLPL")
S1_33122.change_platform(station_code_to_id("TT"), 6)
S1_33122.set_ending(station_code_to_id("TTBW"), 2)
S1_33122.extend_stop(station_code_to_id("TLA"), 1)
S1_33122.change_platform(station_code_to_id("TLA"), 2)
S1_33122.extend_stop(station_code_to_id("TBOD"), 1)

S1_TRAINS = [S1_33101, S1_33102, S1_33103, S1_33104, S1_33105, S1_33106, S1_33107, S1_33108, S1_33109, S1_33110, S1_33111, S1_33112,
              S1_33113, S1_33114, S1_33115, S1_33116, S1_33117, S1_33118, S1_33119, S1_33120, S1_33121, S1_33122, S1_33123]

_S1_TRAINS = [train for train in S1_TRAINS if train._leg_parent is None]  # Filter out trains that are legs of other trains

## S11 Trains
S11_33171 = Train.from_blueprint(33171, RS11_TUEBINGEN_MOESSINGEN, "RS 11", "6:01", "LPL")
S11_33171.set_origin(station_code_to_id("TTBW"), 2, platform=1)
S11_33171.change_platform(station_code_to_id("TMS"), 1)
S11_33171.extend_stop(station_code_to_id("TMS"), 3)

S11_33173 = Train.from_blueprint(33173, RS11_TUEBINGEN_MOESSINGEN, "RS 11", "6:21", "LPL")
S11_33173.set_origin(station_code_to_id("TTBW"), 2, platform=1)
S11_33173.set_ending(station_code_to_id("TMSA"), 1, platform=1)

S11_33175 = Train.from_blueprint(33175, RS11_TUEBINGEN_MOESSINGEN, "RS 11", "7:01", "LPL")
S11_33175.set_origin(station_code_to_id("TTBW"), 2, platform=1)
S11_33175.change_platform(station_code_to_id("TMS"), 1)
S11_33175.extend_stop(station_code_to_id("TMS"), 3)

S11_33177 = Train.from_blueprint(33177, RS11_TUEBINGEN_MOESSINGEN, "RS 11", "7:21", "LPL")
S11_33177.set_origin(station_code_to_id("TTBW"), 2, platform=1)
S11_33177.set_ending(station_code_to_id("TMSA"), 1, platform=1)

S11_33179 = Train.from_blueprint(33179, RS11_TUEBINGEN_MOESSINGEN, "RS 11", "8:01", "LPL")
S11_33179.set_origin(station_code_to_id("TTBW"), 2, platform=1)
S11_33179.change_platform(station_code_to_id("TMS"), 1)
S11_33179.extend_stop(station_code_to_id("TMS"), 3)

S11_33181 = Train.from_blueprint(33181, RS11_TUEBINGEN_MOESSINGEN, "RS 11", "8:21", "LPL")
S11_33181.set_origin(station_code_to_id("TTBW"), 2, platform=1)
S11_33181.set_ending(station_code_to_id("TMSA"), 1, platform=1)

S11_33183 = Train.from_blueprint(33183, RS11_TUEBINGEN_MOESSINGEN, "RS 11", "9:01", "LPL")
S11_33183.set_origin(station_code_to_id("TTBW"), 2, platform=1)
S11_33183.change_platform(station_code_to_id("TMS"), 1)
S11_33183.extend_stop(station_code_to_id("TMS"), 3)

S11_33185 = Train.from_blueprint(33185, RS11_TUEBINGEN_MOESSINGEN, "RS 11", "9:21", "LPL")
S11_33185.set_origin(station_code_to_id("TTBW"), 2, platform=1)
S11_33185.set_ending(station_code_to_id("TMSA"), 1, platform=1)

S11_33187 = Train.from_blueprint(33187, RS11_TUEBINGEN_MOESSINGEN, "RS 11", "10:01", "LPL")
S11_33187.set_origin(station_code_to_id("TTBW"), 2, platform=1)
S11_33187.change_platform(station_code_to_id("TMS"), 1)
S11_33187.extend_stop(station_code_to_id("TMS"), 3)

S11_33189 = Train.from_blueprint(33189, RS11_TUEBINGEN_MOESSINGEN, "RS 11", "10:21", "LPL")
S11_33189.set_origin(station_code_to_id("TTBW"), 2, platform=1)
S11_33189.set_ending(station_code_to_id("TMSA"), 1, platform=1)


########

S11_33172 = Train.from_blueprint(33172, RS11_MOESSINGEN_TUEBINGEN, "RS 11", "6:31", "LPL")
S11_33172.change_platform(station_code_to_id("TMS"), 1)
S11_33172.extend_stop(station_code_to_id("TMS"), 1)
S11_33171.add_leg(S11_33172)

S11_33174 = Train.from_blueprint(33174, RS11_MOESSINGEN_TUEBINGEN, "RS 11", "7:03", "LPL")
S11_33174.set_origin(station_code_to_id("TMSA"), 1, platform=1)

S11_33176 = Train.from_blueprint(33176, RS11_MOESSINGEN_TUEBINGEN, "RS 11", "7:31", "LPL")
S11_33176.set_origin(station_code_to_id("TMSA"), 1, platform=1)
S11_33176.extend_stop(station_code_to_id("TMS"), 1)
S11_33175.add_leg(S11_33176)

S11_33178 = Train.from_blueprint(33178, RS11_MOESSINGEN_TUEBINGEN, "RS 11", "8:03", "LPL")
S11_33178.set_origin(station_code_to_id("TMSA"), 1, platform=1)

S11_33180 = Train.from_blueprint(33180, RS11_MOESSINGEN_TUEBINGEN, "RS 11", "8:31", "LPL")
S11_33180.set_origin(station_code_to_id("TMSA"), 1, platform=1)
S11_33180.extend_stop(station_code_to_id("TMS"), 1)

S11_33182 = Train.from_blueprint(33182, RS11_MOESSINGEN_TUEBINGEN, "RS 11", "9:03", "LPL")
S11_33182.set_origin(station_code_to_id("TMSA"), 1, platform=1)

S11_33184 = Train.from_blueprint(33184, RS11_MOESSINGEN_TUEBINGEN, "RS 11", "9:31", "LPL")
S11_33184.set_origin(station_code_to_id("TMSA"), 1, platform=1)
S11_33184.extend_stop(station_code_to_id("TMS"), 1)

S11_33186 = Train.from_blueprint(33186, RS11_MOESSINGEN_TUEBINGEN, "RS 11", "10:03", "LPL")
S11_33186.set_origin(station_code_to_id("TMSA"), 1, platform=1)

S11_33188 = Train.from_blueprint(33188, RS11_MOESSINGEN_TUEBINGEN, "RS 11", "10:31", "LPL")
S11_33188.set_origin(station_code_to_id("TMSA"), 1, platform=1)
S11_33188.extend_stop(station_code_to_id("TMS"), 1)

S11_TRAINS = [S11_33171, S11_33173, S11_33174, S11_33175, S11_33177, S11_33178, 
               S11_33179, S11_33180, S11_33181, S11_33182, S11_33183, S11_33184, 
               S11_33185, S11_33186, S11_33187, S11_33188, S11_33189]

_S11_TRAINS = [train for train in S11_TRAINS if train._leg_parent is None]  # Filter out trains that are legs of other trains

## S12 Trains
S12_33201 = Train.from_blueprint(33201, RS12_TUEBINGEN_RTS, "RS 12", "5:49", "LPL")
S12_33201.set_origin(station_code_to_id("TTBW"), 2, platform=1)

S12_33203 = Train.from_blueprint(33203, RS12_TUEBINGEN_RTS, "RS 12", "6:49", "LPL")
S12_33203.set_origin(station_code_to_id("TTBW"), 2, platform=1)

S12_33205 = Train.from_blueprint(33205, RS12_TUEBINGEN_RTS, "RS 12", "7:49", "LPL")
S12_33205.set_origin(station_code_to_id("TTBW"), 2, platform=1)

S12_33207 = Train.from_blueprint(33207, RS12_TUEBINGEN_RTS, "RS 12", "8:49", "LPL")
S12_33207.set_origin(station_code_to_id("TTBW"), 2, platform=1)

S12_33209 = Train.from_blueprint(33209, RS12_TUEBINGEN_RTS, "RS 12", "9:49", "LPL")
S12_33209.set_origin(station_code_to_id("TTBW"), 2, platform=1)

S12_33202 = Train.from_blueprint(33202, RS12_RTS_TUEBINGEN, "RS 12", "5:13", "LPL")
S12_33202.set_origin(station_code_to_id("PFAB"), 10, platform=2)
S12_33202.set_ending(station_code_to_id("TTBW"), 2, platform=1)

S12_33204 = Train.from_blueprint(33204, RS12_RTS_TUEBINGEN, "RS 12", "6:13", "LPL")
S12_33204.set_origin(station_code_to_id("PFAB"), 10, platform=2)
S12_33204.set_ending(station_code_to_id("TTBW"), 2, platform=1)

S12_33206 = Train.from_blueprint(33206, RS12_RTS_TUEBINGEN, "RS 12", "7:12", "LPL")
S12_33206.set_ending(station_code_to_id("TTBW"), 2, platform=1)
S12_33206.extend_stop(station_code_to_id("RTS"), 2)

S12_33208 = Train.from_blueprint(33208, RS12_RTS_TUEBINGEN, "RS 12", "8:12", "LPL")
S12_33208.set_ending(station_code_to_id("TTBW"), 2, platform=1)
S12_33208.extend_stop(station_code_to_id("RTS"), 2)

S12_33210 = Train.from_blueprint(33210, RS12_RTS_TUEBINGEN, "RS 12", "9:12", "LPL")
S12_33210.set_ending(station_code_to_id("TTBW"), 2, platform=1)
S12_33210.extend_stop(station_code_to_id("RTS"), 2)

S12_TRAINS = [S12_33201, S12_33202, S12_33203, S12_33204, S12_33205, S12_33206, S12_33207, S12_33208, S12_33209, S12_33210]
_S12_TRAINS = [train for train in S12_TRAINS if train._leg_parent is None]

## S2 Trains
S2_33221 = Train.from_blueprint(33221, RS2_MOESSINGEN_RTS, "RS 2", "6:06", "LPLPL")
S2_33221.set_ending(station_code_to_id("RTS"), 1, True, platform=3, departure=7)
S2_33221.add_leg(S12_33206)

S2_33223 = Train.from_blueprint(33223, RS2_ROHW_RTS, "RS 2", "6:42", "LPLPL")
S2_33223.set_ending(station_code_to_id("RTS"), 1, True, platform=3, departure=7)

S2_33225 = Train.from_blueprint(33225, RS2_MOESSINGEN_RTS, "RS 2", "6:36", "LPLPL")
S2_33225.set_ending(station_code_to_id("RTS"), 1, True, platform=3, departure=7)

S2_33227 = Train.from_blueprint(33227, RS2_MOESSINGEN_RTS, "RS 2", "7:06", "LPLPL")
S2_33227.set_ending(station_code_to_id("RTS"), 1, True, platform=3, departure=7)
S2_33227.add_leg(S12_33208)

S2_33229 = Train.from_blueprint(33229, RS2_ROHW_RTS, "RS 2", "7:42", "LPLPL")
S2_33229.set_ending(station_code_to_id("RTS"), 1, True, platform=3, departure=7)

S2_33231 = Train.from_blueprint(33231, RS2_MOESSINGEN_RTS, "RS 2", "7:36", "LPLPL")
S2_33231.set_ending(station_code_to_id("RTS"), 1, True, platform=3, departure=7)

S2_33233 = Train.from_blueprint(33233, RS2_MOESSINGEN_RTS, "RS 2", "8:06", "LPLPL")
S2_33233.set_ending(station_code_to_id("RTS"), 1, True, platform=3, departure=7)

S2_33235 = Train.from_blueprint(33235, RS2_ROHW_RTS, "RS 2", "8:42", "LPLPL")
S2_33235.set_ending(station_code_to_id("RTS"), 1, True, platform=3, departure=7)

S2_33237 = Train.from_blueprint(33237, RS2_MOESSINGEN_RTS, "RS 2", "8:36", "LPLPL")
S2_33237.set_ending(station_code_to_id("RTS"), 1, True, platform=3, departure=7)

S2_33239 = Train.from_blueprint(33239, RS2_MOESSINGEN_RTS, "RS 2", "9:06", "LPLPL")
S2_33239.set_ending(station_code_to_id("RTS"), 1, True, platform=3, departure=7)

S2_33241 = Train.from_blueprint(33241, RS2_MOESSINGEN_RTS, "RS 2", "9:36", "LPLPL")
S2_33241.set_ending(station_code_to_id("RTS"), 1, True, platform=3, departure=7)

S2_33243 = Train.from_blueprint(33243, RS2_MOESSINGEN_RTS, "RS 2", "10:06", "LPLPL")
S2_33243.set_ending(station_code_to_id("RTS"), 1, True, platform=3, departure=7)

S2_33245 = Train.from_blueprint(33245, RS2_MOESSINGEN_RTS, "RS 2", "10:36", "LPLPL")
S2_33245.set_ending(station_code_to_id("RTS"), 1, True, platform=3, departure=7)

####################

S2_33222 = Train.from_blueprint(33222, RS2_RTS_MOESSINGEN, "RS 2", "5:28", "LPLPL")
S2_33222.set_origin(station_code_to_id("PFAB"), 10, platform=2)

S2_33224 = Train.from_blueprint(33224, RS2_RTS_ROHW, "RS 2", "5:44", "LPLPL")
S2_33224.set_origin(station_code_to_id("PFAB"), 10, platform=2)

S2_33226 = Train.from_blueprint(33226, RS2_RTS_MOESSINGEN, "RS 2", "5:58", "LPLPL")
S2_33226.set_origin(station_code_to_id("PFAB"), 10, platform=2)

S2_33228 = Train.from_blueprint(33228, RS2_RTS_MOESSINGEN, "RS 2", "6:28", "LPLPL")
S2_33228.set_origin(station_code_to_id("PFAB"), 10, platform=2)

S2_33230 = Train.from_blueprint(33230, RS2_RTS_ROHW, "RS 2", "6:44", "LPLPL")
S2_33230.set_origin(station_code_to_id("PFAB"), 10, platform=2)

S2_33232 = Train.from_blueprint(33232, RS2_RTS_MOESSINGEN, "RS 2", "6:57", "LPLPL")
S2_33232.extend_stop(station_code_to_id("RTS"), 2)
S12_33201.add_leg(S2_33232)

S2_33234 = Train.from_blueprint(33234, RS2_RTS_MOESSINGEN, "RS 2", "7:27", "LPLPL")
S2_33234.extend_stop(station_code_to_id("RTS"), 2)
S2_33223.add_leg(S2_33234)

S2_33236 = Train.from_blueprint(33236, RS2_RTS_ROHW, "RS 2", "7:43", "LPLPL")
S2_33236.extend_stop(station_code_to_id("RTS"), 2)
S2_33225.add_leg(S2_33236)

S2_33238 = Train.from_blueprint(33238, RS2_RTS_MOESSINGEN, "RS 2", "7:57", "LPLPL")
S2_33238.extend_stop(station_code_to_id("RTS"), 2)
S12_33203.add_leg(S2_33238)

S2_33240 = Train.from_blueprint(33240, RS2_RTS_MOESSINGEN, "RS 2", "8:27", "LPLPL")
S2_33240.extend_stop(station_code_to_id("RTS"), 2)

S2_33242 = Train.from_blueprint(33242, RS2_RTS_ROHW, "RS 2", "8:43", "LPLPL")
S2_33242.extend_stop(station_code_to_id("RTS"), 2)

S2_33244 = Train.from_blueprint(33244, RS2_RTS_MOESSINGEN, "RS 2", "8:57", "LPLPL")
S2_33244.extend_stop(station_code_to_id("RTS"), 2)

S2_33246 = Train.from_blueprint(33246, RS2_RTS_MOESSINGEN, "RS 2", "9:27", "LPLPL")
S2_33246.extend_stop(station_code_to_id("RTS"), 2)

S2_33248 = Train.from_blueprint(33248, RS2_RTS_MOESSINGEN, "RS 2", "9:57", "LPLPL")
S2_33248.extend_stop(station_code_to_id("RTS"), 2)

S2_33250 = Train.from_blueprint(33250, RS2_RTS_MOESSINGEN, "RS 2", "10:27", "LPLPL")
S2_33250.extend_stop(station_code_to_id("RTS"), 2)


S2_TRAINS = [S2_33221, S2_33222, S2_33223, S2_33224, S2_33225, S2_33226, S2_33227,
              S2_33228, S2_33229, S2_33230, S2_33231, S2_33232, S2_33233, S2_33234, S2_33235, S2_33236, S2_33237,
              S2_33238, S2_33239, S2_33240, S2_33241, S2_33242, S2_33243, S2_33244, S2_33245, S2_33246, S2_33248, S2_33250]

_S2_TRAINS = [train for train in S2_TRAINS if train._leg_parent is None]

#################################
############# TRAINS #############
#################################

TRAINS = [
    *_MEX_TRAINS,
    *_RE17_TRAINS,
    #*_S1_TRAINS,
    #*_S11_TRAINS,
    #*_S12_TRAINS,
    #*_S2_TRAINS
]


def main():
    selected_section = "Tübingen - Albstadt"

    timetable_df = trains_to_dataframe(TRAINS)
    if timetable_df.empty:
        print(f"The worksheet '{selected_section}' does not yet contain any timetable data.")
        return
    #plot_route_timetable(timetable_df, selected_section, "05:40", 140)
    #plot_route_timetable(timetable_df, "Tübingen - Betzingen", "05:40", 140)
    #generate_line_timetable(TRAINS, "Tübingen - Betzingen", "05:00", 160)
    #generate_line_timetable(TRAINS, "RT Hbf K / B - RT Süd", "05:40", 140)
    #generate_line_timetable(TRAINS, "TMS - RTS", "5:40", 140)
    # plot_station_departures(TRAINS, "RTS", "05:20", 180)
    #plot_station_departures(TRAINS, "TT", "05:00", 180)
    print(MEX_19302.timetable())
    print(MEX_19304.timetable())
    print(MEX_19306.timetable())
    print(MEX_19316.timetable())
    print(MEX_19322.timetable())

    export_trains_txt(TRAINS)


if __name__ == "__main__":
    main()
