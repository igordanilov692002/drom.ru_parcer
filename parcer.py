import random
import re
import time
import fake_useragent
# import pandas
# from bs4 import BeautifulSoup
import requests

class Drom_Parser:
    base_link = 'https://auto.drom.ru'
    def __int__(self):
        pass
    def get_html(self, url = 'https://auto.drom.ru', params=None):
        """ получение кода страницы """
        # headers = {
        #     "Accept": "*/*",
        #     "User-Agent": fake_useragent.UserAgent().random
        # }
        # html = requests.get(url, headers=headers, params=params)
        Html_file = open("drom_main_page.html", "w")
        # Html_file.write(html.text)
        print(Html_file)
        # Html_file.write(html.text)
        # Html_file.close()
        return Html_file



if __name__ == "__main__":
    url = 'https://auto.drom.ru'
    # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
    a = Drom_Parser()
    print(a.get_html(a.base_link))



