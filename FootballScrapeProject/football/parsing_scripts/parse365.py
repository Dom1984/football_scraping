import bs4, sys
import pandas as pd
from datetime import date
import requests
import pprint as pp
import fnmatch
import os

today = date.today()
st = "football365-"

for file in os.listdir('.'):        # For all files in the current directory
    if fnmatch.fnmatch(file, f'{st}{today}.html'):  # If it's F365 and todays date
        with open(file, 'r') as f:
            webpage = f.read()

#Parse data
soup = bs4.BeautifulSoup(webpage, 'html.parser')

#Main headlines (h2)
main_headline_dict = {}
head = soup.find('figure', attrs={'class': 'hero__figure'})
link = head.find(href=True)                                                         # extract the hyperlink that will lead to the article content
main_headline = [headline.get_text() for headline in head.findChildren("h2")]     # extract the h2 headline
mylist = [main_headline, link['href']]                                              # merge the two strings into a list
main_headline_dict['main_headline'] = mylist                                        # create a dict to store this data


# Main headline link
main_headline_content = requests.get(main_headline_dict['main_headline'][1]).text
soup = bs4.BeautifulSoup(main_headline_content, 'html.parser')
#author
author_text = soup.find("header", attrs={'class': 'article__header'})
author = author_text.find(href=True)
author = author.get_text()
#content
content = soup.find("section", attrs={'class': 'article__body'})
#em first
article = [em.get_text() for em in content.find_all("em")]
article2 = [p.get_text() for p in content.find_all("p")]
final = article + article2
mylist = [main_headline, link['href'], author, final]

main_headline_dict['main_headline'] = mylist[0][0]
main_headline_dict['link'] = mylist[1]
main_headline_dict['author'] = mylist[2]
main_headline_dict['article'] = mylist[3]

pp.pprint(main_headline_dict)

#Secondary headlines (h3)

secondary = soup.find('ul', attrs={'class': 'hero__list'})
li_tags = {}
counter = 1
for li in secondary.find_all("li"):
    heading = [text.get_text() for text in li.findChildren("h3")]
    link = li.find(href=True)
    mylist = [heading[0], link["href"]]
    li_tags[counter] = mylist
    counter += 1

# Access the content of the articles within the links

# Main headline link
final = []
def parse_main():
    main_headline_content = requests.get(main_headline_dict['main_headline'][1]).text
    soup = bs4.BeautifulSoup(main_headline_content, 'html.parser')
    #author
    author_text = soup.find("header", attrs={'class': 'article__header'})
    author = author_text.find(href=True)
    author.get_text()
    #content
    content = soup.find("section", attrs={'class': 'article__body'})
    #em first
    article = [em.get_text() for em in content.find_all("em")]
    article2 = [p.get_text() for p in content.find_all("p")]
    final = article + article2

#secondary headline links
for link in li_tags.values():
    article = requests.get(link[1]).text
    soup = bs4.BeautifulSoup(article, 'html.parser')
    author_text = soup.find("header", attrs={'class': 'article__header'})
    author = author_text.find(href=True)
    content = soup.find("section", attrs={'class': 'article__body'})
    #em first
    article = [em.get_text() for em in content.find_all("em")]
    article2 = [p.get_text() for p in content.find_all("p")]
    sec = article + article2








 

