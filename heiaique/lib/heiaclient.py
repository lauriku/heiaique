import oauth2 as oauth

from ConfigParser import SafeConfigParser
from urllib       import urlencode

class HeiaClient:
  
  def __init__(self):
    pass

  def list_sports(self):
    return self.__api_request(self.config.get("heiaheia", "sports_url"))

  def find_sport(self, id):
    '''Silly API, can't pass the id as an actual http parameter.'''
    url = self.config.get("heiaheia", "sports_url") + id
    return self.__api_request(url)

  def get_training_logs(self):
    return self.__api_request(self.config.get("heiaheia", "training_logs_url"))

  def get_training_logs_by_date(self, date):
    params = {'date': date}
    return self.__api_request(self.config.get("heiaheia", "training_logs_url"), params)

  def get_training_logs_by_year(self, year):
    params = {'year': year}
    return self.__api_request(self.config.get("heiaheia", "training_logs_url"), params)

  def read_config(self, config_file):
    self.config = SafeConfigParser()
    if self.config.read(config_file):
      return True
    else:
      return False

  def __api_request(self, url, method="GET", params=None):
    token    = oauth.Token(key=self.config.get('oauth', 'token'), secret=self.config.get('oauth', 'token_secret'))
    consumer = oauth.Consumer(key=self.config.get('oauth', 'consumer_key'), secret=self.config.get('oauth', 'consumer_secret'))
    
    if params:
      parameters = urlencode(params)
      url = url + "?" + parameters

    client = oauth.Client(consumer, token)
    response, content = client.request(url, method)

    return content
  

