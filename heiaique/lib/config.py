import os
import sys

from ConfigParser import SafeConfigParser

class Config:

  def __init__(self):
    self.config_file_name = "config.cfg"
    self.config = SafeConfigParser()
    self.__read_config()

  def get(self, section, value):
    return self.config.get(section, value)

  def __read_config(self):
    main_path = os.path.dirname(os.path.abspath(sys.modules['__main__'].__file__))
    config_file = os.path.join(main_path, self.config_file_name)
    self.config.read(config_file)
