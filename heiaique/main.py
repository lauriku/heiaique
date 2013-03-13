import os
import sys
import pprint

from lib import HeiaClient
from lib import Options
from lib import Sports

if __name__ == '__main__':
  options = Options()
  opts, args = options.parse(sys.argv[1:])

  client = HeiaClient()
  sports = Sports()

  if opts.get_training_logs:
    if opts.date:
      print client.get_training_logs_by_date(opts.date)
    elif opts.year:
      logs = client.get_training_logs_by_year(opts.year)
      for log in logs:
        print sports.find(log["sport_id"]), log["duration_h"] + ":" + log["duration_m"]

  if opts.list_sports:
    sports_list = sports.list()
    for id in sports_list:
      print sports_list[id]