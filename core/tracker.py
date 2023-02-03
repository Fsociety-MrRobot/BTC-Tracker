import requests
from bs4 import BeautifulSoup


class Scraper:
    def __init__(
        self, coin):
        self.coin = coin
        self.url = f'https://coinmarketcap.com/currencies/{self.coin}/'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0'}


    def scraper(
        self):
        self.r = requests.get(self.url, self.headers)
        self.soup = BeautifulSoup(self.r.content, "html.parser")

        self.tag = self.soup.find('small', 'nameSymbol').text
        self.price = self.soup.find('div', 'priceValue').text\
            .replace("$", "")\
            .replace(",", "")

        return f"{self.tag}@{self.price}"


    def dump(
        self, data, file):
        with open(file, 'a') as output:
            output.write(f"{data}\n")


    def return_data(
        self, tag, price):
        return tag, price        
