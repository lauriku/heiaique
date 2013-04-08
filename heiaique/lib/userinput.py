import time

class UserInput:

  def __init__(self):
    pass

  def get(self, message):
    return raw_input(message)

  def valid_date(self, date):
    try:
      valid_date = time.strptime(date, "%Y-%m-%d")
    except ValueError:
      return False


