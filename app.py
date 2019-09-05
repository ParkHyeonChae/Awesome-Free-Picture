from flask import Flask, render_template, request, url_for, redirect, session
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
app.secret_key = 'sample_secret'
_page = 1
a = 0
b = 9
imgdata = []
viewdata = imgdata[a:b]
@app.route('/')
def index():
    return render_template('main.html')

@app.route('/imgCrawling', methods=['GET', 'POST'])
def imgCrawling():
    if request.method == 'POST':
        # global page
        # page = 1
        # imgdata = []
        global imgdata, _page
        imgdata = []
        _page = 1
        for page in range(1,5):
            session['keyword'] = request.form['imgkeyword']
            keyword = session['keyword']
            url = "https://pixabay.com/images/search/"+keyword+"/?pagi=%d"%(page)
        
            imgdata.extend(clawling(url))
        
        viewdata = imgdata[a:b]
        
        return render_template('imglist.html', imglist=viewdata, keyword=keyword, tmp=not None, pagenum=_page, nowpage=1)
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

@app.route('/imgCrawling/page/<pagenum>', methods=['GET','POST'])
def page(pagenum):
    # global page
    # page += 1

    keyword = session['keyword'] 
    # url = "https://pixabay.com/images/search/"+keyword+"/?pagi=%d"%(page)
    # imgdata = clawling(url)

    # return render_template('imglist.html', imglist=imgdata, keyword=keyword, tmp=not None)
    
    global a, b, imgdata, _page, viewdata
    _page = _page + 1
    a = (int(pagenum)-1) * 9 
    b = int(pagenum) * 9
    
    viewdata = imgdata[a:b]
    return render_template('imglist.html', imglist=viewdata, keyword=keyword, tmp=not None, pagenum=_page, nowpage=_page)

@app.route('/imgCrawling/back/<pagenum>', methods=['POST','GET'])
def back(pagenum):
    keyword = session['keyword'] 
    global a, b, imgdata, _page, viewdata
    _page = _page - 1
    a = (int(pagenum)-1) * 9 
    b = int(pagenum) * 9
    
    viewdata = imgdata[a:b]
    return render_template('imglist.html', imglist=viewdata, keyword=keyword, tmp=not None, pagenum=_page, nowpage=_page)

@app.route('/imgCrawling/pagemove', methods=['POST','GET'])
def pagemove():
    keyword = session['keyword'] 
    pagenum = request.form['nowpagenum']
    _page = pagenum
    global a, b, imgdata, viewdata

    a = (int(pagenum)-1) * 9 
    b = int(pagenum) * 9
    
    viewdata = imgdata[a:b]
    return render_template('imglist.html', imglist=viewdata, keyword=keyword, tmp=not None, pagenum=_page) 


@app.route('/nextpage', methods=['POST'])
def nextpage():
    # global page
    # page += 1

    keyword = session['keyword'] 
    # url = "https://pixabay.com/images/search/"+keyword+"/?pagi=%d"%(page)
    # imgdata = clawling(url)

    # return render_template('imglist.html', imglist=imgdata, keyword=keyword, tmp=not None)
    
    global a, b, imgdata, _page
    a += 9
    b += 9
    _page += 1
    viewdata = imgdata[a:b]
    return render_template('imglist.html', imglist=viewdata, keyword=keyword, tmp=not None)

@app.route('/previouspage', methods=['POST'])
def previouspage():
    # global page
    # page -= 1
    # if page == 0:
    #     page = 1

    keyword = session['keyword']
    # url = "https://pixabay.com/images/search/"+keyword+"/?pagi=%d"%(page)
    # imgdata = clawling(url)
    global a, b, imgdata, page

    if a > 0:
        a -= 9
        b -= 9
        page -= 1
    else:
        a = 0
        b = 9
    viewdata = imgdata[a:b]
    return render_template('imglist.html', imglist=viewdata, keyword=keyword, tmp=not None)

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

if __name__ == "__main__":
    app.run(debug=True)