import requests
from flask import Flask, render_template
import multiprocessing
import random
import multiprocessing.dummy
import time


from actor import actor

app = Flask(__name__)

lista_actores = []

p = multiprocessing.dummy.Pool(multiprocessing.cpu_count())



@app.route('/')
def hello_world():
    start_time = time.time()

    global lista_actores
    lista_urls = []
    for x in range(50):
        lista_urls.append("https://api.themoviedb.org/3/person/popular?api_key=6571f3c9bf9f6be28a99b58842d35298&language=en-EN&page="+str(x))
    print(lista_urls)
    print(multiprocessing.cpu_count())
    lista_actores = []
    lista = get_peoples_id(1)
    p.map(get_peoples_id, lista_urls)
    print("".join([x.name for x in lista_actores]))
    actor = random.choice(lista_actores)
    print("--- %s seconds ---" % (time.time() - start_time))
    return render_template("index.html",
                           output=[actor.name, actor.link_image])



def get_peoples_id(URL):
    print("mirar esto")
    print(URL)
    try:
        r = requests.get(URL)
        if r.ok:
            print("okey!")
            d = r.json()
            print(d['total_pages'])
            for actores in d['results']:
                try:
                    val = int(actores['name'])
                    pass
                except:
                    lista_peliculas = []
                    for x in actores['known_for']:
                        lista_peliculas.append(x['original_title'])
                    lista_actores.append(actor(actores['name'], "http://image.tmdb.org/t/p/w500/" + actores['profile_path'], lista_peliculas))


            # return render_template('index.html', output=listita)
    except:
        pass


if __name__ == '__main__':
    app.run()
