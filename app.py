from flask import Flask, render_template, request, url_for, redirect, session
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
app.secret_key = 'sample_secret'
page = 1

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        global page
        page = 1
        session['keyword'] = request.form['imgkeyword']
        keyword = session['keyword']
        url = "https://pixabay.com/images/search/"+keyword+"/?pagi=1"

        imgdata = clawling(url)

        return render_template('index.html', imglist=imgdata, keyword=keyword, tmp=not None)
    else:
        return render_template('index.html')

@app.route('/nextpage', methods=['POST'])
def nextpage():
    global page
    page += 1

    keyword = session['keyword'] 
    url = "https://pixabay.com/images/search/"+keyword+"/?pagi=%d"%(page)
    imgdata = clawling(url)

    return render_template('index.html', imglist=imgdata, keyword=keyword, tmp=not None)

@app.route('/previouspage', methods=['POST'])
def previouspage():
    global page
    page -= 1
    if page == 0:
        page = 1

    keyword = session['keyword']
    url = "https://pixabay.com/images/search/"+keyword+"/?pagi=%d"%(page)
    imgdata = clawling(url)

    return render_template('index.html', imglist=imgdata, keyword=keyword, tmp=not None)

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