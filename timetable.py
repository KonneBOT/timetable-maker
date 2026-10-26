"""Compatibility entry point for the modular timetable application."""

from main import (
    MEX_TUEBINGEN_REUTLINGEN,
    RE17_TUEBINGEN_REUTLINGEN,
    RS5_TUEBINGEN_ENGSTINGEN,
    TRAINS,
    main,
)
from diagrams import generate_line_timetable, plot_route_timetable
from train import (
    STATIONS,
    Car,
    Station,
    Train,
    Visit,
    create_train,
    station_code_to_id,
    stationCodeToId,
    train,
    trains_to_dataframe,
)


if __name__ == "__main__":
    main()
