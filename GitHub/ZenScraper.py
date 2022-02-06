#import libraries

from bs4 import BeautifulSoup as bs
import requests
import urllib.request
#import these libraries later
#import time
#import datetime
#import smtplib

url = 'https://www.dailyzen.com/'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0","Accept-Encoding":"gzip, deflate, br","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8","Dnt": "1","Connection":"close","Upgrade-Insecure-Requests":"1"}
html = urllib.request.urlopen(url)

#identify the get request and variable
def getdata(url):
    r = requests.get(url)
    return r.text

#parse the html
htmldata = getdata("https://www.dailyzen.com/")
soup = bs(htmldata, 'html.parser')
data = ''

#just scraping for text value in the section of html called "blockquote"
for data in soup.find_all("blockquote"):
    print(data.get_text())





