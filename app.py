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

if __name__ == "__main__":
    app.run(debug=True)



# from bs4 import BeautifulSoup
# import requests

# keyword = input("검색 이미지 : ")
# url = "https://pixabay.com/images/search/"+keyword

# res = requests.post(url)
# html = res.content
# soup = BeautifulSoup(html, "html.parser")

# img_names = soup.find_all('img')

# for img in img_names:
#     imgdata = img['src']
#     print (imgdata)


# from bs4 import BeautifulSoup
# import requests

# keyword = input("검색 이미지 : ")
# url = "https://pixabay.com/images/search/"+keyword

# res = requests.post(url)
# html = res.content
# soup = BeautifulSoup(html, "html.parser")

# img_names = soup.find_all('img')

# imgdata = []
# for img in img_names:
#     imgdata.append(img['src'])


# print (imgdata)


# from flask import Flask, render_template, request, url_for, redirect
# from bs4 import BeautifulSoup
# import requests

# app = Flask(__name__) 

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         keyword = request.form['keyword']
#         url = "https://unsplash.com/search/photos/"+keyword
        
#         res = requests.post(url)
#         html = res.content
#         soup = BeautifulSoup(html, "html.parser")

#         divtag = soup.find('div',{'class' : 'IEpfq'})
#         #img_names = divtag.find('img')

#         # imgdata = []
#         # for img in img_names:
#         #     imgdata.append(img['src'])

#         return render_template('index.html', imglist=divtag)
#     else:
#         return render_template('index.html')

# if __name__ == "__main__":
#     app.run(debug=True)