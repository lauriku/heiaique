import os
import sys

from lib import HeiaClient
from lib import Options

if __name__ == '__main__':
  options = Options()
  opts, args = options.parse(sys.argv[1:])

  client = HeiaClient()

  main_path = os.path.dirname(os.path.abspath(__file__))
  config_file = os.path.join(main_path, "config.cfg")
  
  if not client.read_config(config_file):
    sys.exit("Config file not found.")

  if opts.get_training_logs:
    if opts.date:
      print client.get_training_logs_by_date(opts.date)
    elif opts.year:
      logs = client.get_training_logs_by_year(opts.year)
      for log in logs:
        print client.find_sport(log["sport_id"]), log["duration_h"] + ":" + log["duration_m"]

  if opts.list_sports:
    print client.list_sports()



