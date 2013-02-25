import os
import sys

from lib import HeiaClient
from lib import XMLParser
from lib import Options

if __name__ == '__main__':
  options = Options()
  opts, args = options.parse(sys.argv[1:])

  client = HeiaClient()

  main_path = os.path.dirname(os.path.abspath(__file__))
  config_file = os.path.join(main_path, "config.cfg")
  if opts.sport_list:
    if client.read_config(config_file):
      print client.list_sports()
    else:
      print "Config file not found!"
