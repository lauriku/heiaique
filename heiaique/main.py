import os

from lib import HeiaClient
from lib import XMLParser

if __name__ == '__main__':
  client = HeiaClient()

  main_path = os.path.dirname(os.path.abspath(__file__))
  config_file = os.path.join(main_path, "config.cfg")

  if client.read_config(config_file):
    print client.list_sports()
  else:
    print "Config file not found!"
