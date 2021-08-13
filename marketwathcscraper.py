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


    def scrape(self, src):
        source = requests.get(src).text
        soup = BeautifulSoup(source, 'lxml')
        d1 = self.today.strftime("%Y-%m-%d")
        for article in soup.find_all('div', class_='article__content'):
                date = article.find("span", class_="article__timestamp")
                if not date:
                    continue
                date = date['data-est'][:10]
                if date == d1:
                    headline = article.h3.a.text
                    self.info_gathered['Heading'].append(headline.strip())
                    summary = ' '
                    # summary = article.find('div', class_='stream-item__description').text
                    self.info_gathered['Description'].append(summary)
                    link = article.h3.a
                    url = link.get('href')
                    self.info_gathered['Link'].append(url)
                else:
                    continue

        return self.info_gathered

    def linkformer(self, q):
        return f'https://www.marketwatch.com/investing/{q}?mod=side_nav'

    def execution(self,):
        search_types = ['cryptocurrency', 'stocks', 'mutual-funds']
        names = ['Heading', 'Description', 'Link']
        links = [self.linkformer(k) for k in search_types]

        for j in links:
            my_thread = threading.Thread(target=self.scrape,args=(j,))
            my_thread.start()
            my_thread.join()

        df = pd.DataFrame(self.info_gathered)

        print(df)




if __name__ == '__main__':
    A = MarketWatch_scraper()
    A.execution()







