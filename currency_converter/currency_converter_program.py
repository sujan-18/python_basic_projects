"""
 only for limited data
import currency_converter
from currency_converter import CurrencyConverter

c= CurrencyConverter()
print(c.currencies)

# print(c.convert(100,'EUR','NPR'))
"""

import requests

class Currency_converter:

    def __init__(self, amount, convert_from, convert_to):
        self.amount = amount
        self.convert_from = convert_from
        self.convert_to = convert_to

    def convert_currency(self):
        url = f"https://api.frankfurter.app/latest?amount={self.amount}&from={self.convert_from}&to={self.convert_to}"
        response = requests.get(url).json() 
        # print(response)  
        return response["rates"][self.convert_to]

    def result(self):
        converted_value = self.convert_currency()  
        # print(converted_value)
        print(f"After converting {self.amount} {self.convert_from} into {self.convert_to}, it became {converted_value}")

currency_obj = Currency_converter(1500, 'USD', 'INR')
currency_obj.result()


