import requests
import sys
from bs4 import BeautifulSoup
r = requests.get('https://www.flipkart.com/samsung-galaxy-s10-lite-prism-white-128-gb/p/itmb6f6f7cc402e7?pid=MOBFZ8HTSDNVQGPG&lid=LSTMOBFZ8HTSDNVQGPGWWMUEH&fm=neo%2Fmerchandising&iid=M_24de92c8-f7b7-4588-80ea-4db1a3d44299_7.O1KLOOZRTYV2&ppt=clp&ppn=mobile-phones-store&ssid=litxr7ynps0000001590491482577&otracker=clp_omu_Latest%2BLaunches_1_7.dealCard.OMU_Latest%2BLaunches_mobile-phones-store_O1KLOOZRTYV2_5&otracker1=clp_omu_PINNED_neo%2Fmerchandising_Latest%2BLaunches_NA_dealCard_cc_1_NA_view-all_5&cid=O1KLOOZRTYV2')
content = r.content.decode(encoding='UTF-8')
soup = BeautifulSoup(r.content.decode(encoding='UTF-8'), "lxml")
Name = soup.find_all('div', {"class": "_29OxBi"})
Price= soup.find_all('div',{"class":"_1vC4OE _3qQ9m1"})
print(Name)
print(Price)