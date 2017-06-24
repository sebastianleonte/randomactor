import requests
from flask import Flask, render_template
import multiprocessing
import random
import multiprocessing.dummy
import time


from actor import actor

app = Flask(__name__)

lista_actores = []
def get_peoples_id(URL):
    time.sleep(3)
    print('dentro-get_peoples_id')
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
                    print("val: " + val)
                    pass
                except:
                    lista_peliculas = []
                    for x in actores['known_for']:
                        lista_peliculas.append(x['title'])
                    print(actores['name'])
                    lista_actores.append(actor(actores['name'], "http://image.tmdb.org/t/p/w500/" + actores['profile_path'], lista_peliculas))


            # return render_template('index.html', output=listita)
    except:
        pass

#p = multiprocessing.dummy.Pool(multiprocessing.cpu_count())
p = multiprocessing.dummy.Pool(8)
lista_urls = []
for x in range(100):
    lista_urls.append("https://api.themoviedb.org/3/person/popular?api_key=6571f3c9bf9f6be28a99b58842d35298&language=en-EN&page="+str(x))
print(lista_urls)
print(multiprocessing.cpu_count())
#lista = get_peoples_id(1)
p.map(get_peoples_id, lista_urls)
print(len(lista_actores))


@app.route('/')
def hello_world():
    start_time = time.time()

    global lista_actores

    actor = random.choice(lista_actores)
    print("--- %s seconds ---" % (time.time() - start_time))

    return render_template("index.html",
                           output=[actor.name, actor.link_image, actor.lista_peliculas, len(lista_actores)])






if __name__ == '__main__':
    app.run()
