import re
from datetime import datetime, timedelta
text = """        # Erster Zug startet in TT 5:53 (demnach early in Engstingen später)
    S5_33501 = Train.from_blueprint(33501, RS5_ENGSTINGEN_ENTRINGEN, "RS 5", "04:59", "LPLPL")
    S5_33501.extend_stop(station_code_to_id("TT"), 2)
    # Wendet auf S5_33506

    S5_33503 = Train.from_blueprint(33503, RS5_ENGSTINGEN_ENTRINGEN, "RS 5", "05:29", "LPLPL")
    S5_33503.extend_stop(station_code_to_id("TT"), 2)
    # Wendet auf S5_33508

    S5_33505 = Train.from_blueprint(33505, RS5_ENGSTINGEN_ENTRINGEN, "RS 5", "05:59", "LPLPL")
    S5_33505.extend_stop(station_code_to_id("TT"), 2)
    # Wendet auf S5_33510

    S5_33507 = Train.from_blueprint(33507, RS5_ENGSTINGEN_ENTRINGEN, "RS 5", "06:29", "LPLPL")
    S5_33507.extend_stop(station_code_to_id("TT"), 2)
    # Wendet auf S5_33512

    S5_33509 = Train.from_blueprint(33509, RS5_ENGSTINGEN_ENTRINGEN, "RS 5", "06:59", "LPLPL")
    S5_33509.extend_stop(station_code_to_id("TT"), 2)  
    # Wendet auf S5_33514

    S5_33511 = Train.from_blueprint(33511, RS5_ENGSTINGEN_ENTRINGEN, "RS 5", "07:29", "LPLPL")
    S5_33511.extend_stop(station_code_to_id("TT"), 2)
    # Wendet auf S5_33516

    S5_33513 = Train.from_blueprint(33513, RS5_ENGSTINGEN_ENTRINGEN, "RS 5", "07:59", "LPLPL")
    S5_33513.extend_stop(station_code_to_id("TT"), 2)
    # Wendet auf S5_33518

    S5_33515 = Train.from_blueprint(33515, RS5_ENGSTINGEN_ENTRINGEN, "RS 5", "08:29", "LPLPL")
    S5_33515.extend_stop(station_code_to_id("TT"), 2)
    # Wendet auf S5_33520

    S5_33517 = Train.from_blueprint(33517, RS5_ENGSTINGEN_ENTRINGEN, "RS 5", "08:59", "LPLPL")
    S5_33517.extend_stop(station_code_to_id("TT"), 2)
    # Wendet auf S5_33522

    S5_33519 = Train.from_blueprint(33519, RS5_ENGSTINGEN_TUEBINGEN, "RS 5", "09:29", "LPLPL")
    S5_33519.set_ending(station_code_to_id("TTBW"), 2, platform=1)
    S5_33519.extend_stop(station_code_to_id("TT"), 2)
    
    S5_33521 = Train.from_blueprint(33521, RS5_ENGSTINGEN_TUEBINGEN, "RS 5", "09:59", "LPLPL")
    S5_33521.set_ending(station_code_to_id("TTBW"), 2, platform=1)
    S5_33521.extend_stop(station_code_to_id("TT"), 2)
"""

def shift_time(match):
    time = datetime.strptime(match.group(1), "%H:%M")
    shifted_time = time - timedelta(minutes=5)
    return f'"{shifted_time.strftime("%H:%M")}"'


shifted_text = re.sub(r'"(\d{1,2}:\d{2})"', shift_time, text)
print(shifted_text)