from flask import Flask, render_template, request, url_for, redirect, session
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
app.secret_key = 'sample_secret'
nowpage = 1
a = 0
b = 9
imgdata = []
viewdata = imgdata[a:b]

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/imgCrawling', methods=['POST'])
def imgCrawling():
    if request.method == 'POST':
        global imgdata, nowpage
        imgdata = []
        nowpage = 1
        for page in range(1,5):
            session['keyword'] = request.form['imgkeyword']
            keyword = session['keyword']
            url = "https://pixabay.com/images/search/"+keyword+"/?pagi=%d"%(page)
            imgdata.extend(clawling(url))
        
        viewlist()
        
        return render_template('imglist.html', imglist=viewdata, keyword=keyword, tmp=not None, pagenum=nowpage)
    else:
        return render_template('imglist.html')

@app.route('/iconCrawling', methods=['GET', 'POST'])
def iconCrawling():
    if request.method == 'POST':
        session['keyword'] = request.form['imgkeyword']
        keyword = session['keyword']
        url = "https://iconmonstr.com/?s="+keyword
        res = requests.post(url)
        html = res.content
        soup = BeautifulSoup(html, "html.parser")

        img_names = soup.find_all('img', class_ = "preload")

        imgdata = []
        for img in img_names:
            imgdata.append(img['src'])

        return render_template('iconlist.html', imglist=imgdata, keyword=keyword, tmp=not None)
    else:
        return render_template('iconlist.html')

@app.route('/imgCrawling/nextpage', methods=['GET','POST'])
def nextpage():
    keyword = session['keyword']    
    global nowpage
    nowpage += 1

    viewlist()

    return render_template('imglist.html', imglist=viewdata, keyword=keyword, tmp=not None, pagenum=nowpage)

@app.route('/imgCrawling/backpage', methods=['POST','GET'])
def backpage():
    keyword = session['keyword'] 
    global nowpage
    nowpage -= 1
    if nowpage < 1:nowpage = 1

    viewlist()

    return render_template('imglist.html', imglist=viewdata, keyword=keyword, tmp=not None, pagenum=nowpage)

@app.route('/imgCrawling/pagemove', methods=['POST'])
def pagemove():
    keyword = session['keyword'] 
    global nowpage
    nowpage = int(request.form['nowpagenum'])
    viewlist()

    return render_template('imglist.html', imglist=viewdata, keyword=keyword, tmp=not None, pagenum=nowpage) 

def clawling(url):
    res = requests.post(url)
    html = res.content
    soup = BeautifulSoup(html, "html.parser")
    img_names = soup.find_all("div", class_ = "item")

    imgdata = []
    for img in img_names:
        if(img.find('img')['src'][0]=='h'):
            imgdata.append(img.find('a').find('img')['src'])
        else:
            imgdata.append(img.find('a').find('img')['data-lazy'])
        
    return imgdata

def viewlist():
    global a, b, nowpage, viewdata, imgdata

    a = (int(nowpage)-1) * 9 
    b = int(nowpage) * 9
    viewdata = imgdata[a:b]
    
    return viewdata

if __name__ == "__main__":
    app.run(debug=True)