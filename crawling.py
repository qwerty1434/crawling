# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import requests

driver = webdriver.Chrome("<웹드라이버>")
driver.implicitly_wait(3)
driver.get("<주소>")

driver.find_element_by_name('authUser').send_keys('<아이디>')
driver.find_element_by_name('authPass').send_keys('<비밀번호>')
driver.find_element_by_css_selector('.uxd-btn').click() #버튼클릭

driver.get("<리뷰주소>")
driver.find_element_by_css_selector('#regNothanksLink').click() #버튼클릭
text_file = open("Output.csv", "w")

for i in range(0,100000):#게시물 
    k = "<리뷰주소>" + str(i)
    driver.get(k)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    #notices = soup.select('p.vproductlist')
    notices = soup.select('span.vproductListItem')
    if "reviews/review/view" in requests.request("GET",k).url:
        for j in range(len(notices)):
            text_file.write(notices[j].text.strip())
        text_file.write("{0}\n".format(i))
        
    else:
        pass
text_file.close()
