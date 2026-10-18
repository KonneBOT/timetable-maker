"""Compatibility entry point for the modular timetable application."""

from main import (
    MEX_RE_TUEBINGEN_REUTLINGEN,
    RS1_TUEBINGEN_REUTLINGEN,
    TRAINS,
    main,
)
from diagrams import create_sample_excel, generate_line_timetable, plot_route_timetable
from train import (
    STATIONS,
    Car,
    Train,
    create_train,
    reverse_blueprint,
    station_code_to_id,
    stationCodeToId,
    train,
    trains_to_dataframe,
)


if __name__ == "__main__":
    main()
