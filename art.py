import requests
from bs4 import BeautifulSoup
import pandas as pd
arr = []
url = 'https://artscenter.ndhu.edu.tw/p/403-1123-5125-1.php?Lang=zh-tw'
html = requests.get(url)
html.encoding = 'utf8' # ֵአutf8嘨
cl = [1,2,3,4,5]
sp = BeautifulSoup(html.text, 'lxml')
count = 0
link = [0,0,0,0,0]
t = 0
for i in sp.find_all("a"):
    if(count>20 and count <32 and count%2==0):
        link[t] = i["href"]
        #print(i["href"])
        t = t+1
    count = count + 1
    
    
    
count = 0
title = []
t = 0
for i in sp.find_all("div",class_ = "mtitle"):
    if(count>=0 and count<5):
        title.append(i.text.strip('\n').strip('\t').strip('\n').strip('\n'))
    count = count + 1

time = []
count = 0
t = 0

for i in range(5):
    print(i+1,end='')
    print(". ",end='')
    title[i] = title[i].replace("\n\t\t\t\n","\n發布時間：")
    print(title[i])
    print("公告連結: ",link[i])
    print()
