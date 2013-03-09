from lxml import etree
from io   import BytesIO

class Parser:

  def __init__(self):
    pass

  def parse_sport_list(self, data):
    file_like_object = BytesIO(data)
    context = etree.iterparse(file_like_object)
    sport = {}
    sportlist = []
    for action, elem in context:
      if not elem.text or elem.text.isspace():
        text = None
      else:
        text = elem.text
        sport[elem.tag] = text
      if elem.tag == "sport":
        sportlist.append(sport)
        sport = {}
    return sportlist

  def parse_single_sport(self, data):
    file_like_object = BytesIO(data)
    context = etree.iterparse(file_like_object)
    sport = {}
    for action, elem in context:
      if not elem.text or elem.text.isspace():
        text = None
      else:
        text = elem.text
        sport[elem.tag] = text
    return sport

  def parse_training_logs(self, data):
    """Parse the xml from HeiaHeia into a list of training entries, 
    each training entry as a dictionary"""

    file_like_object = BytesIO(data)
    context = etree.iterparse(file_like_object)
    training_log = {}
    training_log_entries = []
    for action, elem in context:
      if not elem.text or elem.text.isspace():
        text = None
      else:
        text = elem.text
      training_log[elem.tag] = text
      if elem.tag == "training-log":
        training_log_entries.append(training_log)
        training_log = {}
    return training_log_entries



