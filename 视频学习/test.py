from selenium import webdriver
import time
#https://wenku.baidu.com/view/7c004a4dfbb069dc5022aaea998fcc22bdd14374.html?fr=sezrch-1-wk_sea-income3
base_url=input("网址")
#t=input("网址")
s=webdriver.Chrome()
s.maximize_window()
#time.sleep(3)
s.get(base_url)
#time.sleep(3)
s.get(base_url)
time.sleep(3)