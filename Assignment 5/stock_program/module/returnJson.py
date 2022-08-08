import jsonpickle

class convertToJson:
    def __init__(self):
        self.portfolio = {}
        self.jsonFile = {}

    def converter(self, p):
        self.portfolio = p
        self.jsonFile = jsonpickle.encode(self.portfolio)
