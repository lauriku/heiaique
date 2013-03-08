from lxml import etree

class Parser:

  def __init__(self):
    pass

  def parse(self, data):
    try:
      etree.parse(data)
    except etree.XMLSyntaxError, e:
      pass # just put the exception into e



