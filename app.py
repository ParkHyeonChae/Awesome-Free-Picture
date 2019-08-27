from flask import Flask, render_template, request, url_for, redirect
from bs4 import BeautifulSoup
import lxml

app = Flask(__name__) 

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        url = 'https://unsplash.com/search/photos/'

        params = {
            'query': request.form['keyword'],
            'where': 'post',
        }
        response = request.get(url, params=params)
        html = response.text

        soup = BeautifulSoup(html, 'html.parser')

        imagelist = soup.select()
        # form = GoogleCrawling(request.POST)
        #     url = 'https://www.google.co.uk/search?hl=en&tbm=isch&q='+form.cleaned_data['keyword']
        #     html_doc = requests.get(url)
        #     html = BeautifulSoup(html_doc.text, 'lxml')
        #     img_tag = html.find_all('img')
        #     crawling_img = []
        #     for i in img_tag:
        #         if 'Image result for' in i.get('alt'):
        #             crawling_img.append(i.get('src'))
        # test = request.form['keyword']

        return render_template('index.html', imglist=test)
            
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)