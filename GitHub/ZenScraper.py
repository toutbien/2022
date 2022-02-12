#import libraries

from email import message
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from http import server
from bs4 import BeautifulSoup as bs
import requests
import urllib.request
#import these libraries later
import os
import time
import smtplib
#import libraries which you can add attachments with
from email.mime.text import MIMEText
from email.header import Header
from email.mime.base import MIMEBase
#from email_config import gmail_pass, user, host, port


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
    dailymsg = print(data.get_text(), file=open('dailyquote.txt', "a"))
    #emailmsg =(data.get_text())
    
print(dailymsg, file=open('quote2.txt', "a"))

#create a timer (86400 is one day)
#while(True):
time.sleep(3)

def send_email_w_attachment(to, subject, body, filename):
    to = "lisa_stanley77@yahoo.com"
    subject = "WTF This took 234903 hours"
    body = "This is some bullshit\nDo you agree?"
    filename = (r"C:\Users\toutb\pythosoft\dailyquote.txt")
    
    message = MIMEMultipart()
    message['From'] = Header(sender_address)
    message['To'] = Header(receiver_address)
    message['MSG'] = Header(subject)
    message.attach(MIMEText(body, 'plain'))
    message.attach(att)

filename = "dailyquote.txt" 
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    part = MIMEBase("application", "txt")
    part.set_payload(attachment.read())
    
message.attach(part)
text = message.as_string()
#Sender and receiver information goes here
sender_address = 'citycritik@gmail.com'
sender_pass = 'BuddhaBew122!'
receiver_address = ['lisa_stanley77@yahoo.com'] #who are you sending it to -michelleleeham@gmail.com

att_name = os.path.basename(r"C:\Users\toutb\pythosoft\dailyquote.txt")
_f = open(r"C:\Users\toutb\pythosoft\dailyquote.txt", 'rb')
att = MIMEApplication(_f.read(), _subtype="txt")
_f.close()
att.add_header('Content-Disposition', 'attachment', filename=att_name)
subject = "Fuck"
body = "Fuck me"
message=f"Subject:{subject}\n\n{body}"
server = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
server.starttls() #enable security
server.login(sender_address, sender_pass) #login with mail_id and password
server.sendmail(sender_address, receiver_address, text)
server.quit()
#payload = base64.b64decode(fp.read()).decode('ascii')
#attach.set_payload(payload)
#attach['Content-Transfer-Encoding'] = 'base64'
#fp.close()
#attach.add_header('Content-Disposition', 'attachment', filename = 'dailyquote.txt')
#message.attach(MIMEText(body, 'plain', 'utf-8'))

#Create SMTP session for attaching and sending the mail

#session.sendmail(sender_address, receiver_address, message)
#session.quit()

print(' Your Quote Was Sent')
