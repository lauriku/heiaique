from lxml import etree
from io   import BytesIO

class Parser:

  def __init__(self):
    pass

  def parse_training_logs(self, data):
    file_like_object = BytesIO(data)
    context = etree.iterparse(file_like_object)
    training_log = {}
    training_log_entries = []
    for action, elem in context:
      if not elem.text:
        text = "None"
      else:
        text = elem.text
      training_log[elem.tag] = text
      if elem.tag == "training-log":
        training_log_entries.append(training_log)
    return training_log_entries



