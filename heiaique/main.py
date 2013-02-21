from lib import HeiaClient
from lib import XMLParser

if __name__ == '__main__':
  client = HeiaClient()

  if client.read_config():
    print client.list_sports()
  else:
    print "Config file not found!"


