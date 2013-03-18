from lxml     import etree
from io       import BytesIO
from time     import strptime
from datetime import time, date

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
      created_at = strptime(log.findtext("created-at"), "%Y-%m-%d %H:%M:%S")

      duration = time(int(log.findtext("duration-h")), int(log.findtext("duration-m")), int(log.findtext("duration-s")))
      d        = log.findtext("date").split("-")
      log_date = date(int(d[0]), int(d[1]), int(d[2]))

      log_entry["sport_id"]   = log.findtext("sport-id")
      log_entry["date"]       = log_date
      log_entry["duration"]   = duration
      log_entry["created_at"] = created_at
      log_entry["notes"]      = log.findtext("notes")
      log_list.append(log_entry)
      log_entry = {}

    return log_list




