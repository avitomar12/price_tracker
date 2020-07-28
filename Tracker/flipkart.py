import requests
import sys
from bs4 import BeautifulSoup
import time
import random
Name_selector_class="_35KyD6"
MRP_selector_class="_3auQ3N _1POkHg"
Review_selector_class="_1i0wk8"
Price_selector_class="_1vC4OE _3qQ9m1"

def main(url):
    #r = requests.get('https://www.flipkart.com/oppo-a5s-black-32-gb/p/itmffhgzsqaczrn4?pid=MOBFH3XMSZHGY6ZP&lid=LSTMOBFH3XMSZHGY6ZP5JMJUG&marketplace=FLIPKART&fm=neo%2Fmerchandising&iid=M_da6b7b9a-10a5-4feb-bc2e-92767b6f4439_1_JQ348E9X4M_MC.MOBFH3XMSZHGY6ZP&ppt=clp&ppn=oppo-mobile-phones-store&ssid=2miaesb9lc0000001590569959520&otracker=clp_pmu_v2_Oppo%2BMobiles%2Bunder%2B%25E2%2582%25B910K_1_1.productCard.PMU_V2_Oppo%2BMobiles%2Bunder%2B%25E2%2582%25B910K_oppo-mobile-phones-store_MOBFH3XMSZHGY6ZP_neo%2Fmerchandising_0&otracker1=clp_pmu_v2_PINNED_neo%2Fmerchandising_Oppo%2BMobiles%2Bunder%2B%25E2%2582%25B910K_LIST_productCard_cc_1_NA_view-all&cid=MOBFH3XMSZHGY6ZP')
    r=requests.get(url)
    content = r.content.decode(encoding='UTF-8')
    soup = BeautifulSoup(r.content.decode(encoding='UTF-8'), "lxml")
    Name = soup.find_all('span', {"class": Name_selector_class})
    MRP= soup.find_all('div',{"class":MRP_selector_class})
    Review= soup.find_all('div',{"class":Review_selector_class})

    Price= soup.findAll('div',{"class":Price_selector_class})
    
    name_=Name[0].get_text().encode('ascii','ignore')
    time_=time.time()
    mrp=(MRP[0].get_text()).encode('ascii','ignore')
    price=(Price[0].get_text()).encode('ascii','ignore')
    review_=(Review[0].get_text()).encode('ascii','ignore')
    data={'Name': name_, 'time':time_,'MRP':mrp , 'price' : price,'Review' : review_}
    return data
#while True:
#    main()
#    time.sleep(random.randint(5,20))

