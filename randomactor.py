import requests
from flask import Flask
import multiprocessing
import random
import multiprocessing.dummy

app = Flask(__name__)

lista_actores = []

p = multiprocessing.dummy.Pool(multiprocessing.cpu_count())


@app.route('/')
def hello_world():
    global lista_actores
    lista_urls = []
    for x in range(50):
        lista_urls.append("https://api.themoviedb.org/3/person/popular?api_key=6571f3c9bf9f6be28a99b58842d35298&language=en-EN&page="+str(x))
    print(multiprocessing.cpu_count())
    lista_actores = []
    lista = get_peoples_id(1)
    p.map(get_peoples_id, lista_urls)
    return random.choice(lista_actores)


def get_peoples_id(URL):
    listita = []
    try:
        r = requests.get(URL)
        if r.ok:
            print("okey!")
            d = r.json()
            print(d['total_pages'])
            lista_actores.append(d["results"][0]["id"])
            for actor in d['results']:
                try:
                    val = int(actor['name'])
                    pass
                except:
                    lista_actores.append(actor['name'])


            # return render_template('index.html', output=listita)
    except:
        pass


if __name__ == '__main__':
    app.run()
