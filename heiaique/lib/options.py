from optparse import OptionParser

class Options:

    def __init__(self):
        self._init_parser()

    def _init_parser(self):
        usage = 'bin/heaique'
        self.parser = OptionParser(usage=usage)
        self.parser.add_option("-l", "--list", action="store_true", dest="sport_list", help="List sports", default=False)

    def parse(self, args = None):
        return self.parser.parse_args(args)
