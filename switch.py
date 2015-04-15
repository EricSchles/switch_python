class switch:
    def __init__(self,cases=[]):
        self.cases = {}
        for case in cases:
            self.cases[case] = case
    def __iter__(self):
        yield self.match
        raise StopIteration
    def match(self,case):
        try:
            case = self.cases[case]
            return case
        except KeyError:
            print "Default case reached, value not in switch statement"

