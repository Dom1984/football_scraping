import scrapy
from scrapy.crawler import CrawlerProcess
from os import path
import os
from bs4 import BeautifulSoup
from datetime import date
import pandas as pd
import string
result = string.punctuation
import re

page = 1

class FootballSpider(scrapy.Spider):
    name = "football"
    
    def start_requests(self):
        urls = [
        "https://www.football365.com/",
        "https://www.theguardian.com/football",
        "https://www.skysports.com/football",
        "https://www.irishtimes.com/sport/soccer",
  #      "https://www.mirror.co.uk/sport/football",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse) #, dont_filter = False         
       
    def parse(self, response):
        today = date.today()
        page = re.search(r'https://www.(.*?).co', response.url).group(1)
    #      filename = f'quotes-{page}.html'
        filename = f'{page}-{today}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
    
if __name__ == "__main__":
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    process.crawl(FootballSpider)
    process.start() # the script will block here until the crawling is finished
        
#       myfile = pd.read_html(filename)

# s = "https://www.mirror.co.uk/sport/football"
# today = date.today()
# page = re.search(r'https://www.(.*?).co', s).group(1)
# filename = f'{page}-{today}.html'

# print(filename)
        
