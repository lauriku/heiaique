import json
import os
import sys

from heiaclient import HeiaClient

class Sports:

  def __init__(self):
    main_path = os.path.dirname(os.path.abspath(sys.modules['__main__'].__file__))
    self.sports_file = os.path.join(main_path, "sports.json")

  def list(self):
    if not os.path.exists(self.sports_file):
      self.save_sports_to_file()

    try:
      with open(self.sports_file, 'r') as f:
        return json.load(f)
    except IOError as e:
      print e

  def save_sports_to_file(self):
      client = HeiaClient()
      page = 1
      sport_list = []
      while(True):
        sport_page = client.get_sports(page)
        if not sport_page:
          break
        for sport in sport_page:
          sport_list.append(sport)
        page = page+1

        try:
          with open(self.sports_file, 'w') as outfile:
            json.dump(sport_list, outfile)
        except IOError as e:
          print "Unable to write sports file."