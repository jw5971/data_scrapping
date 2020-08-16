# -*- coding: utf-8 -*-
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


NVAX_CA = pd.DataFrame(columns = ['num', 'dates', 'links', 'details'])
#total_pages = 18
total_pages = 7
for page in range(0,total_pages+1):
    ua = UserAgent()
    headers ={"User-Agent": ua.random}
    url = 'https://ir.novavax.com/press-releases?page={}'
    #{}通配符
    r = requests.get(url=url.format(page), headers=headers)
    '''
    r.encoding = r.apparent_encoding
    '''
    dom = etree.HTML(r.text)
    
    # 'http://www.ylq.com/neidi/xingyufei/'
    
    News_dates = dom.xpath('//div[@class="nir-widget--field nir-widget--news--date-time"]/text()')
    #[News_date.split('\n')[-2][-12:] for News_date in News_dates]
    #[News_date.split('\n      ')[-2] for News_date in News_dates]
    #News_dates = dom.xpath('normalize-space(//div[@class="nir-widget--field nir-widget--news--date-time"]/text())')
    News_dates = [News_date.strip() for News_date in News_dates]
    
    
    News_headlines = dom.xpath('//div[@class="nir-widget--field nir-widget--news--headline"]/a/@href')
    News_headlines = ['https://ir.novavax.com'+News_headline.strip() for News_headline in News_headlines]
    
    #News_details = dom.xpath('//div[@class="nir-widget--field nir-widget--news--teaser"]/text()')
    #/p
    #News_details = dom.xpath('//*[@id="block-nir-pid165-content"]/article/div/div/div/div/div/div/div/div/div/div/div[2]/article/div[3]/div/*/text()')
    #dom.xpath('//*[@id="block-nir-pid165-content"]/article/div/div/div/div/div/div/div/div/div/div/div[2]/article/div[3]/*/text()')
    #注意这个通配符
    News_details = dom.xpath('//*[@id="block-nir-pid165-content"]/article/div/div/div/div/div/div/div/div/div/div/div[2]/article/div[3]/*/text()')
#    News_details = [News_detail.strip() for News_detail in News_details]
    
    print(page, len(News_dates), len(News_headlines), len(News_details))
    
    for i in range(len(News_dates)):
        NVAX_CA = NVAX_CA.append({'num':int((page)*10+i+1), 'dates': News_dates[i],
                                                        'links':News_headlines[i], 'details': News_details[i]},ignore_index=True)

print("Done!")


#star_ids = [star_url.split('/')[-2] for star_url in star_urls]
#star_names = dom.xpath('//div[@class="fContent"]/ul/li/a/h2/text()')
#star_images = dom.xpath('//div[@class="fContent"]/ul/li/a/img/@src')

#print(page, len(star_urls), len(star_ids), len(star_images), len(star_names))
#https://ir.novavax.com+