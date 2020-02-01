from django.shortcuts import render
from django.http import HttpResponse
from .models import ImageModel
from django.core.files.storage import FileSystemStorage
from PIL import Image
from django.core.files import File
import requests
from bs4 import BeautifulSoup
import smtplib
import time
from lxml import html
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from datetime import datetime
# Create your views here.


class Client(QWebEnginePage): 
    def __init__(self, url): 
        self.app = QApplication(sys.argv) 
        QWebEnginePage.__init__(self) 
        self.html = '' 
        self.loadFinished.connect(self._on_load_finished) 
        self.load(QUrl(url)) 
        self.app.exec_() 
    def _on_load_finished(self): 
        self.html = self.toHtml(self.Callable) 
    def Callable(self, html_str): 
        self.html = html_str 
        self.app.quit() 


def get_date(name):
    flag = 1
    
    #print("*********************************************************************")
    client_response = Client(name)
    source = client_response.html
    soup = BeautifulSoup(source, 'html.parser')
    dates = []
    for i in soup.find_all('span', class_ = 'f'):
        le = len(i.text)
        flag1 = 0
        p_date = ''
        for j in i.text:
            if ord(j) >= 65 and ord(j) <=90:
                flag1=1
            if flag1 == 1:
                if j != '-':
                    p_date+=j
                else:
                    break
        dates.append(p_date)
    print(dates)
    ll = len(dates)
    linkss = []
    for i in soup.find_all('div', class_ = 'r'):
        children = i.find('a')['href']
        linkss.append(children)
        print(children)

    
    lll = len(linkss)
    ll = lll-ll
    links = linkss[ll::]
    finalarr = []
    for i in range(0,len(links)):
        if dates[i]:
            finalarr.append((links[i],dates[i].strip()))
    print(finalarr)
    finalarr.sort(key = lambda tup : datetime.strptime(tup[1], '%b %d, %Y'))
    print(finalarr)
    a = finalarr[0][0]
    b= finalarr[0][1]
    
    lis = []
    lis.append(a)
    lis.append(b)
    return lis
    # driver = webdriver.Firefox()
    # driver.get(finalarr[0])


def index_view(request):
    res = ["",""]
    if request.method == 'POST':
        fil = request.FILES.get('up_image')
        p = ImageModel.objects.create(image=fil)
        if fil != None:
                fs = FileSystemStorage()
                filename = fs.save(fil.name, fil)
                uploaded_file_url = fs.url(filename)

        # k = "http://127.0.0.1:8000/" + str(uploaded_file_url)



        # replace the below k by above k at the time of deployment and http://127.0.0.1:8000/ by the site url
        # replace the below k by above k at the time of deployment and http://127.0.0.1:8000/ by the site url
        # replace the below k by above k at the time of deployment and http://127.0.0.1:8000/ by the site url
        # replace the below k by above k at the time of deployment and http://127.0.0.1:8000/ by the site url
        # replace the below k by above k at the time of deployment and http://127.0.0.1:8000/ by the site url
        # replace the below k by above k at the time of deployment and http://127.0.0.1:8000/ by the site url
        # replace the below k by above k at the time of deployment and http://127.0.0.1:8000/ by the site url





        k = "http://images.google.com/searchbyimage?image_url=https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRpbv0vwfx1ag7HWpOn7Gw6EullXtz4dh61gyeLI28mmbgcWQbz"
        res = get_date(k)
        
    return render(request,'index.html',{'date':res[1],'url':res[0]})

