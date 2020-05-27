from selectorlib import Extractor
import requests
import json
import time 

e= Extractor.from_yaml_file('selector.yml')

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
    return
def main(url):
    url= "https://www.amazon.in/Dell-Wired-Keyboard-Mouse-Combo/dp/B009DIX5QQ/ref=pd_rhf_gw_p_img_3?_encoding=UTF8&psc=1&refRID=RJVKQYPSM0JNA0ECSXEQ"
    data = scrape_(url)
    Time=time()
    
    if data:
        data['time']=Time
        save_data(data)
    