from threading import ThreadError
import unittest
import yahoo_fin.stock_info  as si


try:
    amzn_stock = si.get_quote_table('9')
except Exception as error:
    print(error, 'Invalid Stock Marker')
""""
for key, value in amzn_stock.items():
    print(f'{key}: {type(value)} \n')
"""

class TestGetStockData(unittest.TestCase):
    def test_key_val(self):
        """ code to check if dict has values """
        for key, value in amzn_stock.items():
            if value:
                self.assertTrue(True)
            else:
                self.assertTrue(False)
                break
        """code to check ends here"""

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()