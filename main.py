from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

rovers_src = {
    'Perseverance': 'https://www.ridus.ru/images/2021/4/22/1259190/in_article_391a9d0039.jpeg',
    'Curiosity': 'https://argumenti.ru/images/arhnews/453984.jpg',
    }


@app.route("/", methods=['POST','GET'])
def mars_photos():
    marsohod = 'Perseverance'
    if request.args.get('rover') == 'Perseverance' or request.args.get('') == '':
        marsohod = 'Perseverance'
    elif request.args.get('rover') == 'Curiosity':
        marsohod = 'Curiosity'

    r = requests.get('https://api.nasa.gov/mars-photos/api/v1/rovers/' + marsohod + '/latest_photos?api_key=DEMO_KEY')
    jsondata = json.loads(r.text)
    # with open('latest_photos.json') as f:   # скачиваем экземпляр json данных в файл для тестирования
    #     jsondata = json.load(f)
    photos = jsondata['latest_photos']
    date_list = photos[0]['earth_date'].split('-')
    date_list.reverse()
    date = '.'.join(date_list)
    return render_template('index.html', photos=photos, date=date, marsohod=marsohod, rovers_src=rovers_src)


app.run()