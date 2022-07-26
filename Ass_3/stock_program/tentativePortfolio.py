import pickle

class tentative_Portfolio:
    def __init__(self):
        self.portfolio = {}

    def buildPortfolio(self, symbol, basicData, backTestResults):
        self.portfolio[symbol] = {}
        self.portfolio[symbol]['basic data'] = basicData
        self.portfolio[symbol]['backtesting results'] = backTestResults

    def savePortfolio(self, filename: str = None) -> bool:
        """

        :return:
        """
        if filename:
            save_file = f"{filename}.pickle"
        else:
            save_file = "portfolio1.pickle"
        try:
            with open(save_file, 'wb') as file_dump:
                pickle.dump(self.portfolio, file_dump,
                            protocol=pickle.HIGHEST_PROTOCOL)
            return True
        except Exception as e:
            print(f"File Save Exception {e}")
            return False

    def loadPortfolio(self, filename: str = None) -> bool:
        """

        :return:
        """
        if filename:
            save_file = f"{filename}.pickle"
        else:
            save_file = "blackjack_players.pickle"
        try:
            with open(save_file, 'rb') as file_loader:
                self.portfolio = pickle.load(file_loader)
            return True
        except pickle.UnpicklingError as error:
            print(f"file load error: {error}")
            return False
        except Exception as e:
            print(f"Unknown Upload Error: {e}")
            return False
