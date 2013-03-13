import oauth2 as oauth

from urllib       import urlencode
from parser       import Parser
from config       import Config

class HeiaClient:

  def __init__(self):
    self.parser = Parser()
    self.config = Config()

  def get_sports(self, page):
    params = { 'page': page }
    xml = self.__api_request(self.config.get("heiaheia", "sports_url"), params)
    return self.parser.parse_sport_list(xml)

  def get_sport(self, id):
    '''Silly API, can't pass the id as an actual http parameter.'''
    url = self.config.get("heiaheia", "sports_url") + id
    xml = self.__api_request(url)
    return self.parser.parse_single_sport(xml)

  def get_training_logs(self):
    xml = self.__api_request(self.config.get("heiaheia", "training_logs_url"))
    return self.parser.parse_training_logs(xml)

  def get_training_logs_by_date(self, date):
    params = {'date': date}
    print params
    xml = self.__api_request(self.config.get("heiaheia", "training_logs_url"), params)
    return self.parser.parse_training_logs(xml)

  def get_training_logs_by_year(self, year):
    params = {'year': year}
    xml = self.__api_request(self.config.get("heiaheia", "training_logs_url"), params)
    return self.parser.parse_training_logs(xml)

  def post_training_logs(self, params = {}):
    method = "POST"
    return self.__api_request(self.config.get("heiaheia", "training_logs_url"), params, method)

  def __api_request(self, url, params=None, method="GET"):
    token    = oauth.Token(key=self.config.get('oauth', 'token'), secret=self.config.get('oauth', 'token_secret'))
    consumer = oauth.Consumer(key=self.config.get('oauth', 'consumer_key'), secret=self.config.get('oauth', 'consumer_secret'))

    if params:
      parameters = urlencode(params)
      url = url + "?" + parameters

    client = oauth.Client(consumer, token)
    response, content = client.request(url, method)

    return content


