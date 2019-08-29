from flask import Flask, render_template, request, url_for, redirect
from bs4 import BeautifulSoup
import requests

app = Flask(__name__) 

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        keyword = request.form['keyword']
        url = "https://pixabay.com/images/search/"+keyword

        res = requests.post(url)
        html = res.content
        soup = BeautifulSoup(html, "html.parser")
        
        img_names = soup.find_all('img')

        count = 0
        imgdata = []
        for img in img_names:
            imgdata.append(img['src'])
            count+=1
            if count == 16: break

        return render_template('index.html', imglist=imgdata)
    else:
        return render_template('index.html')

# def imgsave(imgurl):
#     imgurllist = []
#     imgurllist.append(imgurl)
#     return imgurllist

if __name__ == "__main__":
    app.run(debug=True)