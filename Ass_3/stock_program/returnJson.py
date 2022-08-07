import jsonpickle

class convertToJson:
    def __init__(self):
        self.portfolio = {}

    def converter(self, p):
        self.portfolio = p
        jsonFile = jsonpickle.encode(self.portfolio)
        print(jsonFile)
