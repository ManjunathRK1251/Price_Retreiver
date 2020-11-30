import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import time,random

#to send email
import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("pythontest1251@gmail.com", "python100*")
message = '''Hey price of Realme 6 pro has come down,
check this url:'https://www.flipkart.com/realme-6-pro-lightning-blue-64-gb/p/itm19b1945c12aee?pid=MOBFPCX76F3BYQDH&lid=LSTMOBFPCX76F3BYQDHGAICT2&fm=neo%2Fmerchandising&iid=M_47d16c2e-d412-42cb-bcb7-b9bf3368a69f_8.YFEZBF8WTO9G&ssid=3vy19nb3v40000001595303953677&otracker=hp_omu_Best%2BBattery%2BPhones_7_8.dealCard.OMU_Best%2BBattery%2BPhones_YFEZBF8WTO9G_5&otracker1=hp_omu_WHITELISTED_neo%2Fmerchandising_Best%2BBattery%2BPhones_NA_dealCard_cc_7_NA_view-all_5&cid=YFEZBF8WTO9G'''

def check():
#Parsing prices
    url = 'https://www.flipkart.com/realme-6-pro-lightning-blue-64-gb/p/itm19b1945c12aee?pid=MOBFPCX76F3BYQDH&lid=LSTMOBFPCX76F3BYQDHGAICT2&fm=neo%2Fmerchandising&iid=M_47d16c2e-d412-42cb-bcb7-b9bf3368a69f_8.YFEZBF8WTO9G&ssid=3vy19nb3v40000001595303953677&otracker=hp_omu_Best%2BBattery%2BPhones_7_8.dealCard.OMU_Best%2BBattery%2BPhones_YFEZBF8WTO9G_5&otracker1=hp_omu_WHITELISTED_neo%2Fmerchandising_Best%2BBattery%2BPhones_NA_dealCard_cc_7_NA_view-all_5&cid=YFEZBF8WTO9G'
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html,'html.parser')
    price = soup.find("div",{"class": "_1vC4OE _3qQ9m1"}).get_text().replace(',','')
    print(price[1:])
    while True:
        if int(price[1:]) < 20000:
            server.sendmail('pythontest1251@gmail.com','rkmanjunath10000@gmail.com',message)
            print(price[1:])
            #exit()

while True:
    check()
    time.sleep(5)