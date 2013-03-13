from lxml import etree
from io   import BytesIO

class Parser:

  def __init__(self):
    pass

  def parse_sport_list(self, data):
    file_like_object = BytesIO(data)
    xml_data = etree.parse(file_like_object)

    sports = xml_data.findall("sport")

    sport_list = {}

    for sport in sports:
      sport_list[sport.findtext("id")] = sport.findtext("name")

    return sport_list


  def parse_single_sport(self, data):
    file_like_object = BytesIO(data)
    xml_data = etree.parse(file_like_object)
    sport = xml_data.findtext("name")
    return sport

  def parse_training_logs(self, data):
    file_like_object = BytesIO(data)
    xml_data = etree.parse(file_like_object)

    training_logs = xml_data.findall("//training-log")

    log_list = []
    log_entry = {}

    for log in training_logs:
      log_entry["sport_id"]   = log.findtext("sport-id")
      log_entry["date"]       = log.findtext("created-at")
      log_entry["duration_h"] = log.findtext("duration-h")
      log_entry["duration_m"] = log.findtext("duration-m")
      log_entry["notes"]      = log.findtext("notes")
      log_list.append(log_entry)
      log_entry = {}

    return log_list




