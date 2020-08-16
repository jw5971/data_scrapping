
"""
Created on Fri Aug 14 21:09:27 2020

@author: JIWU5
"""
import time
import random
import requests
from lxml import etree
import pandas as pd
from fake_useragent import UserAgent


NVAX_Rew = pd.DataFrame(columns = ['nums','background','pros', 'cons'])
total_pages = 8

for page in range(1,total_pages+1):
    ua = UserAgent()
    headers ={"User-Agent": ua.random}
    url = 'https://www.glassdoor.com/Reviews/Novavax-Reviews-E5710_P{}.htm'

    r = requests.get(url=url.format(page), headers=headers)
    dom = etree.HTML(r.text)
    
    pros = dom.xpath('//*[@id]/div/div[2]/div[2]/div[4]/p[2]/span/text()')
    cons = dom.xpath('//*[@id]/div/div[2]/div[2]/div[5]/p[2]/span/text()')
    background = dom.xpath("//*[@id]/div/div[2]/div[2]/p/text()")
    print(len(pros),len(cons))

    for i in range(10):
        try:
            NVAX_Rew = NVAX_Rew.append({'nums':int((page-1)*10+i+1),'background':background[i],'pros':pros[i],'cons':cons[i]},ignore_index = True)

        except Exception as e:
            print(e)
            pass
        continue

print("done!")

