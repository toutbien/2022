#import libraries
from email.quoprimime import quote
import requests
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup as bs
#from lxml import html
import smtplib
import time
import datetime


# connect to website for scraping
URL = 'https://www.dailyzen.com/'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0","Accept-Encoding":"gzip, deflate, br","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8","Dnt": "1","Connection":"close","Upgrade-Insecure-Requests":"1"}
page = requests.get(URL, headers=headers)
soup = bs(response.text, "lxml")
quote1 = soup.select_one('div[id^=zen--quote')
for class_ in soup:
    print class_.get_text()
#reason = bs(page.content)
quote_finder = bs.find(id="div")get.("zen--quote")
#reason('div')
#tree = html.fromstring(page.text)
#quote_2 = tree.xpath('//span[@class="zen--quote"]/text()')

#Soup1 = bs(page.content, "html.parser")
#Soup4 = bs.findAll('div', attrs={'class':'zen--quote'})
#Soup3 = bs.select('div', id="zen--quote")
#Soup2 = bs(Soup1.prettify(), "html.parser")
#pquery = pq('<html><body><div><div id="zen--quote">....</div></div></body></html>')
#pquery()

#day_quote = Soup2.find_all("div", class_="Grid-cell  v2-u-size1of2")
#day_quote = bs.find("div", {"id": "zen--quote"})

#the_quote = []
#new_quote = bs("div", class_="Grid-cell  v2-u-size1of2")
#for class_ in new_quote:
    #the_quote.append(class_.find("a").contents[0])
print(quote_finder.select(".zen--quote")[0].getText())

#print(reason)
#print(new_quote)


