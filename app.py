from flask import Flask, render_template, request, url_for, redirect, session
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
app.secret_key = 'sample_secret'
nowpage = 1
a = 0
b = 9
data = []
viewdata = data[a:b]
viewtype = ''

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/imgCrawling', methods=['POST'])
def imgCrawling():
    if request.method == 'POST':
        global data, nowpage, viewtype
        viewtype = 'img'
        data = []
        nowpage = 1

        for page in range(1,3):
            keyword = keyword_()
            url = 'https://pixabay.com/images/search/'+keyword+'/?pagi=%d'%(page)
            soup = crawling(url)

            img_names = soup.find_all('div', class_ = 'item')
            for img in img_names:
                if(img.find('img')['src'][0:4]=='http' and img.find('img')['src'][-3:]=='jpg'):
                    data.append(img.find('a').find('img')['src'][:-8]+'1280.jpg')

                elif(img.find('img')['src'][0:4]=='http' and img.find('img')['src'][-3:]=='png'):
                    data.append(img.find('a').find('img')['src'][:-8]+'1280.png')

                else:
                    if(img.find('img')['data-lazy'][-3:]=='jpg'):
                        data.append(img.find('a').find('img')['data-lazy'][:-8]+'1280.jpg')
                    else:
                        data.append(img.find('a').find('img')['data-lazy'][:-8]+'1280.png')
        
        viewlist()
        
        return render_template('imglist.html', viewlist=viewdata, keyword=keyword, tmp=not None, pagenum=nowpage)
    else:
        return render_template('imglist.html')

@app.route('/iconCrawling', methods=['GET', 'POST'])
def iconCrawling():
    if request.method == 'POST':
        global viewtype
        viewtype = 'img'
        data = []
        keyword = keyword_()
        url = 'https://iconmonstr.com/?s='+keyword
        soup = crawling(url)

        img_names = soup.find_all('img', class_ = 'preload')
        for img in img_names:
            data.append(img['src'])

        if not data: 
            return render_template('error.html')
        else:
            return render_template('iconlist.html', viewlist=data, keyword=keyword, tmp=not None)
    else:
        return render_template('iconlist.html')

@app.route('/videoCrawling', methods=['GET', 'POST'])
def videoCrawling():
    if request.method == 'POST':
        global data, nowpage, viewtype
        viewtype = 'video'
        data = []
        nowpage = 1
        keyword = keyword_()
        url = 'https://pixabay.com/ko/videos/search/'+keyword
        soup = crawling(url)

        img_names = soup.find_all('div', class_ = 'item')
        for img in img_names:
            data.append(img.find('div', class_ = 'media')['data-mp4'])
        
        viewlist()

        return render_template('videolist.html', viewlist=viewdata, keyword=keyword, tmp=not None, pagenum=nowpage)
    else:
        return render_template('videolist.html')

@app.route('/nextpage', methods=['GET','POST'])
def nextpage():
    keyword = session['keyword']    
    global nowpage, viewtype
    
    nowpage += 1

    viewlist()

    if viewtype == 'img':
        return render_template('imglist.html', viewlist=viewdata, keyword=keyword, tmp=not None, pagenum=nowpage)
    elif viewtype == 'video':
        return render_template('videolist.html', viewlist=viewdata, keyword=keyword, tmp=not None, pagenum=nowpage)

@app.route('/backpage', methods=['POST','GET'])
def backpage():
    keyword = session['keyword'] 
    global nowpage, viewtype

    nowpage -= 1
    if nowpage < 1:nowpage = 1

    viewlist()

    if viewtype == 'img':
        return render_template('imglist.html', viewlist=viewdata, keyword=keyword, tmp=not None, pagenum=nowpage)
    elif viewtype == 'video':
        return render_template('videolist.html', viewlist=viewdata, keyword=keyword, tmp=not None, pagenum=nowpage)

@app.route('/pagemove', methods=['POST'])
def pagemove():
    keyword = session['keyword'] 
    global nowpage, viewtype
    nowpage = int(request.form['nowpagenum'])
    viewlist()

    if viewtype == 'img':
        return render_template('imglist.html', viewlist=viewdata, keyword=keyword, tmp=not None, pagenum=nowpage)
    elif viewtype == 'video':
        return render_template('videolist.html', viewlist=viewdata, keyword=keyword, tmp=not None, pagenum=nowpage)

def crawling(url):
    res = requests.post(url)
    html = res.content
    soup = BeautifulSoup(html, 'html.parser') 
    return soup

def keyword_():
    session['keyword'] = request.form['imgkeyword']
    keyword = session['keyword']
    return keyword

def viewlist():
    global a, b, nowpage, viewdata, data
    a = (int(nowpage)-1) * 9 
    b = int(nowpage) * 9
    viewdata = data[a:b]
    return viewdata

if __name__ == '__main__':
    app.run(debug=True)