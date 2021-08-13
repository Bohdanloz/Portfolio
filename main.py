import requests
from bs4 import BeautifulSoup
import pandas as pd
from PyPDF2 import PdfFileReader
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from datetime import date
import logging
import threading

class ForbesScraper():

    def __init__(self):
        self.info_gathered = {'Link':[],'Heading':[],'Description':[]}


    def scrape(self, src):
        source = requests.get(src).text
        soup = BeautifulSoup(source, 'lxml')

        for article in soup.find_all('article'):
            headline = article.h3.a.text
            self.info_gathered['Heading'].append(headline)
            summary = article.find('div', class_='stream-item__description').text
            self.info_gathered['Description'].append(summary)
            link = article.h3.a
            url = link.get('href')
            self.info_gathered['Link'].append(url)
        return self.info_gathered

    def linkformer(self, q, startdate='today', type='score'):
        return f'https://www.forbes.com/search/?q={q}&startdate={startdate}&sort={type}&sh=25f4a72c279f'

    def pdf_former(self, dataframe, site_name):
        today = date.today()
        fig, ax =plt.subplots(figsize=(12,4))
        ax.axis('tight')
        ax.axis('off')
        the_table = ax.table(cellText=dataframe.values,colLabels=dataframe.columns,loc='center')
        d3 = str(today.strftime("%b-%d-%Y"))
        pp = PdfPages(site_name + "_" + d3 + ".pdf")
        pp.savefig(fig, bbox_inches='tight')
        pp.close()

    def execution(self, ):
        search_types = ['Cryptocurrencies','Stock','Shares']
        names = ['Heading','Description','Link']
        links = [self.linkformer(k) for k in search_types]

        for j in links:
            my_thread = threading.Thread(target=self.scrape,args=(j,))
            my_thread.start()
            my_thread.join()

        #df = pd.DataFrame(self.info_gathered)
        #self.pdf_former(df, 'forbes')
        print(self.info_gathered)




if __name__ == '__main__':
    A = ForbesScraper()
    A.execution()






