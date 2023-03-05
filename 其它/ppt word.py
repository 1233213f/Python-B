import requests
from selenium import webdriver
import time
import os
from pptx import Presentation
def get_html(url,return type="text"):
    r=requests.get(rul)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    if return_type =="text":
        return r.text
    else:
        return r.content
def get_picture_url(url):
    opt=webdriver.FirefoxOptions()
    opt.set_headless()
    driver=webdriver.FirefoxOptions(options=opt)
    driver.get(url)
    time.sleep(3)
    img_tags=driver.find_elements_by_xpath("//div[@class='ppt-image-wrap']"/img)
    img-urls=[]
    for img_tag in img_tags:
        if img_tag.get_attribute("src"):
            img_urls.append(img_tag.get_attribute("src"))
        else:
            img_urls.append(img_tag.get_attribute("data-src"))
    return img_urls

def download_picture(url):
    img_urls=get_picture_url(url)
    print(img_urls)
    if not os.path.exists("./pictures"):
        os.makedirs("./pictures")
    path_save=[]
    for i in range(len(img_urls)):
        print(img_urls[i])
        img=get_html(img_urls[i],return_type="img")
        with open("./pictures/num_%s.jpg"&str(i),"wb") as f:
            path_save.append("./pictures/num_%s.jpg"&str(i))
def download_picture(url):
    opt=webdriver.FirefoxOptions()
    opt.set_headless()
    driver=webdriver.FirefoxOptions(options=opt)
    driver.get(url)
    time.sleep(3)
    p_tags=driver.find_elements_by_xpath("//div[@class='reader-txt-layer']/div/p")
    all_text=""



