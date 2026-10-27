from dataclasses import dataclass


@dataclass(frozen=True)
class LineSection:
    """A manually defined ordered station section for a line timetable."""

    name: str
    station_codes: tuple[str | int, ...]


LINE_SECTIONS = {
    section.name: section
    for section in (
        LineSection(
            "Herrenberg - Tübingen",
            ("THEZ", "TZWE", "TGU", "TALT", "TENT", "TPG", "TUJM", "TUJS", "TTW", "TT"),
        ),
        LineSection(
            "Entringen - Tübingen",
            ("TENT", "TPG", "TUJM", "TUJS", "TTW", "TT"),
        ),
        LineSection(
            "Rottenburg - Tübingen",
            ("TRT", "TRTD", "TKIB", "TBU", "TKC", "TWEI", "TMUN", "TT"),
        ),
        LineSection(
            "Tübingen - Albstadt",
            (
                "TT", "TMUS", "TDD", "TST", "TDU", "TNEH", "TMS",
                "TBSB", "TBOD", "THCH", "THST", "THSU", "TWEZ", "TBIS",
                "TBSH", "TENG", "TBG", "TBGM", "TBGS", "TENO", "TFRW",
                "TFR", "TLAO", "TLAU", "TAEW", "TAEM", "TAE", "TAET",
            ),
        ),
        LineSection(
            "Mössingen - Betzingen",
            ("TMS", "NSU", "NMI", "NSCH", "RGOT", "RGOM", "RGOO", "ROHW", "ROHM", "ROHO", "RBAK", "RBEM", "RBES"),
        ),
        LineSection(
            "Ohmenhausen West - Betzingen",
            ("ROHW", "ROHM", "ROHO", "RBAK", "RBEM", "RBES"),
        ),
        LineSection(
            "Tübingen - Betzingen",
            ("TT", "TTG", "TTN", "TKI", "TWAN", "RBE"),
        ),
        LineSection(
            "Bosmännsäcker - RT Hbf K",
            ("RBO", "RTW", "RHbfK"),
        ),
        LineSection(
            "RT Hbf K / B - RT Süd",
            ("RHbfK", "RHbfB", "RGA", "RALB", "RECH", "RTS"),
        ),
        LineSection(
            "RT Süd - Engstingen",
            ("RTS", "PFA", "PFB", "PFM", "PFK", "PFS", "TKL"),
        ),
    )
}
for section in tuple(LINE_SECTIONS.values()):
    start, end = section.name.split(" - ", 1)
    reverse_name = f"{end} - {start}"
    LINE_SECTIONS.setdefault(
        reverse_name,
        LineSection(reverse_name, tuple(reversed(section.station_codes))),
    )


def get_section(section):
    """Resolve a section name or return an already resolved section."""
    if isinstance(section, LineSection):
        return section
    try:
        return LINE_SECTIONS[section]
    except KeyError as error:
        raise ValueError(f"Unknown line section: {section!r}") from error
