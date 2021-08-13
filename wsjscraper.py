import requests
from bs4 import BeautifulSoup
import pandas as pd
from PyPDF2 import PdfFileReader
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from datetime import date
import logging
import threading

class MarketWatch_scraper():

    def __init__(self):
        self.info_gathered = {'Link':[],'Heading':[],'Description':[]}
        self.today = date.today()
        self.df = pd.DataFrame()


    def scrape(self, src):
        headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
        source = requests.get(src, headers=headers).text
        soup = BeautifulSoup(source, 'lxml')
        d1 = self.today.strftime("%B %d, %Y")

        for article in soup.find_all('article'):
            date = article.find('p', class_='WSJTheme--timestamp--22sfkNDv').text
            print(date)
            if not date:
                continue

            if date == d1:
                headline = article.h2.a.span.text
                self.info_gathered['Heading'].append(headline)
                summary = article.find('span', class_='WSJTheme--summaryText--2LRaCWgJ').text
                self.info_gathered['Description'].append(summary)
                link = article.h2.a
                url = link.get('href')
                self.info_gathered['Link'].append(url)

        return self.info_gathered

    def linkformer(self, q):
        return f'https://www.wsj.com/news/markets/{q}'

    def execution(self,):
        search_types = ['stocks','oil-gold-commodities-futures']
        names = ['Heading', 'Description', 'Link']
        links = [self.linkformer(k) for k in search_types]

        for j in links:
            my_thread = threading.Thread(target=self.scrape,args=(j,))
            my_thread.start()
            my_thread.join()

        self.df = pd.DataFrame(self.info_gathered)

        print(self.info_gathered)




if __name__ == '__main__':
    A = MarketWatch_scraper()
    A.execution()






