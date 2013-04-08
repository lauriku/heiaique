import os
import sys
import pprint

from datetime import datetime

from lib import HeiaClient
from lib import Options
from lib import Sports
from lib import UserInput

if __name__ == '__main__':
  options = Options()
  opts, args = options.parse(sys.argv[1:])
  user_input = UserInput()

  client = HeiaClient()
  sports = Sports()

  if opts.get_training_logs:
    if opts.date:
      print client.get_training_logs_by_date(opts.date)
    elif opts.year:
      logs = client.get_training_logs_by_year(opts.year)
      for log in logs:
        print log["date"]
        print sports.find(log["sport_id"])
        print "Duration: ", log["duration"]

  if opts.list_sports:
    sports_list = sports.list()
    for id in sports_list:
      print sports_list[id]

  if opts.post_log:
    user_input("")