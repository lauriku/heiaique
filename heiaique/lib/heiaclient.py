import oauth2 as oauth

from ConfigParser import SafeConfigParser
from urllib       import urlencode

class HeiaClient:
  
  def __init__(self):
    pass

  def list_sports(self, page=None):
    if page:
      params = {'page': page}

    return self.__api_request(self.config.get("heiaheia", "sports_url"), page)

  def find_sport_by_id(self, id):
    pass

  def get_training_logs_by_date(self, date):
    pass

  def get_training_logs_by_year(self, year):
    pass

  def __api_request(self, url, params=None):
    self.token    = oauth.Token(key=self.config.get('oauth', 'token'), secret=self.config.get('oauth', 'token_secret'))
    self.consumer = oauth.Consumer(key=self.config.get('oauth', 'consumer_key'), secret=self.config.get('oauth', 'consumer_secret'))
    
    if params:
      parameters = urlencode(params)
      url = url + "?" + parameters

    client = oauth.Client(self.consumer, self.token)
    response, content = client.request(url, method='GET')

    return content
  
  def read_config(self, config_file):
    self.config   = SafeConfigParser()
    if self.config.read(config_file):
      return True
    else:
      return False
