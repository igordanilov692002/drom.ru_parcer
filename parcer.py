import random
import re
import time
import fake_useragent
# import pandas
from bs4 import BeautifulSoup
import requests

class Drom_Parser:
    def __init__(self, url1):
        self.base_link = url1
        self.html = self.get_html()
        self.count_of_pages = self.get_pages()
        self.count_of_pages = self.get_cards()
    def get_html(self, params=None):
        #https://auto.drom.ru/bmw/x5/generation4/restyling0/?minprice=1900000&minyear=2021
        """ получение кода страницы """
        headers = {
            "Accept": "*/*",
            "User-Agent": fake_useragent.UserAgent().random
        }
        html = requests.get(self.base_link, headers=headers, params=params)
        self.html = html
        # Html_file = open("drom_main_page.html", "w")
        # Html_file.write(html.text)
        # print(Html_file)
        # Html_file.write(html.text)
        # Html_file.close()
        # return Html_file
        return html
    def make_link(self):
        """формирование сылки"""
        pass

    def get_cards(self, html = None):
        """ получаем автомобильные карточки """
        soup = BeautifulSoup(self.html.text, 'lxml')
        # находим кол-во страниц, иначе количество страниц равно 1
        cards = None
        try:
            # pages = soup.find('css-nlq3fc edzrckn0', {'data-marker': 'pagination-button/nextPage'}).text
            # soup.find_all('p', class_='three')
            cards = soup.find('div', class_=["css-1nvf6xk", "eojktn00"])
            cards = cards.findAll('a')
            print(cards)

        except:
            print('не удалось считать карточки')
        return cards

    # def make_link(self):

    def get_pages(self, html=None):
        """ получаем количество объявлений """
        soup = BeautifulSoup(self.html.text, 'lxml')
        # находим кол-во страниц, иначе количество страниц равно 1
        try:
            # pages = soup.find('css-nlq3fc edzrckn0', {'data-marker': 'pagination-button/nextPage'}).text
            #soup.find_all('p', class_='three')
            pages = soup.find('div', class_=['css-nlq3fc', 'edzrckn0']).text.split()
            pages = int(pages[0])
            print(pages)
        except:
            pages = 1
        print('Количество найденных страниц: ', pages)
        return pages






if __name__ == "__main__":

    url = 'https://auto.drom.ru/bmw/x5/generation4/restyling0/?minprice=1900000&minyear=2021' #https://auto.drom.ru/bmw/x5/generation4/restyling0/?minprice=1900000&minyear=2021
    # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
    a = Drom_Parser(url)




