from optparse import OptionParser

class Options:

    def __init__(self):
        self._init_parser()

    def _init_parser(self):
        usage = 'bin/heaique'
        self.parser = OptionParser(usage=usage)
        self.parser.add_option("-l", "--list", action="store_true", dest="list_sports", help="List sports", default=False)
        self.parser.add_option("-g", "--get-training-logs", action="store_true", dest="get_training_logs", help="Get training logs", default=False)
        self.parser.add_option("-d", "--date", dest="date", help="Date, format YYYY-MM-DD")
        self.parser.add_option("-y", "--year", dest="year", help="Year, format YYYY")

    def parse(self, args = None):
        return self.parser.parse_args(args)
