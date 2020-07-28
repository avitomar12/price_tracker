from selectorlib import Extractor
import requests
import json
import time 
import csv
e= Extractor.from_yaml_file('/home/avi/Documents/work/price_tracker/Tracker/selector.yml')

def scrape_(url):
    headers={
          'authority': 'www.amazon.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }
    print("Downloading  ", url)
    r=requests.get(url,headers=headers)
    if r.status_code >500:
        if "To discuss automated access to Amazon data please contact" in r.text:
            print("Page %s was blocked by Amazon. Please try using better proxies\n"%url)
        else:
            print("Page %s must have been blocked by Amazon as the status code was %d"%(url,r.status_code))
        return None
    return e.extract(r.text)
def save_data(data):
    csv_columns=['Name','Selling_price','MRP','Review','time']
    csv_file = "amazon.csv"
    try:
        with open(csv_file, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            #writer.writeheader()
            writer.writerow(data)
    except IOError:
        print("I/O error")
def main(url):
    #url= "https://www.amazon.in/Dell-Wired-Keyboard-Mouse-Combo/dp/B009DIX5QQ/ref=pd_rhf_gw_p_img_3?_encoding=UTF8&psc=1&refRID=RJVKQYPSM0JNA0ECSXEQ"
    data = scrape_(url)
    Time=time.time()
    #print(data)
    if data['Name']:
        data['time']=Time
        #save_data(data)
    return data
#import random
#while True:
#    main()
#    time.sleep(random.randint(5,10))