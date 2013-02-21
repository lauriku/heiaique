import xml.etree.ElementTree as ET

class XMLParser:
  
  def __init__(self):
    pass

  def parsexml(self, xml):
    parsed = ET.fromstring(content)
    for child in parsed.findall('training-log'):
      print "Sport-id:", child.find('sport-id').text, "Duration:", child.find('duration-h').text + ":" + child.find('duration-m').text
