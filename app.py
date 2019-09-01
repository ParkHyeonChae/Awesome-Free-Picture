from flask import Flask, render_template, request, url_for, redirect
from bs4 import BeautifulSoup
import requests

app = Flask(__name__) 

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        keyword = request.form['keyword']
        #total_page = 10
    #for page in range(total_page):
        #url = "https://pixabay.com/images/search/"+keyword+"/?pagi=%d"%(page+1)
        url = "https://pixabay.com/images/search/"+keyword

        res = requests.post(url)
        html = res.content
        soup = BeautifulSoup(html, "html.parser")
        
        #img_names = soup.find_all('img')
        img_names = soup.find_all("div", class_ = "item")

        count = 0
        imgdata = []
        for img in img_names:
            if(img.find('img')['src'][0]=='h'):
                imgdata.append(img.find('a').find('img')['src'])
            # count+=1
            # if count == 16: break
            else:
                imgdata.append(img.find('a').find('img')['data-lazy'])

        return render_template('index.html', imglist=imgdata)
    else:
        return render_template('index.html')

# def imgsave(imgurl):
#     imgurllist = []
#     imgurllist.append(imgurl)
#     return imgurllist

if __name__ == "__main__":
    app.run(debug=True)