import requests
from flask import Flask

app = Flask(__name__)
lista_actores = []

@app.route('/')
def hello_world():
    global lista_actores
    lista_actores = []
    lista = get_peoples_id(1)
    return " ".join([x for x in lista])


def get_peoples_id(page):
    actual_page = page

    listita = []
    URL = "https://api.themoviedb.org/3/person/popular?api_key=6571f3c9bf9f6be28a99b58842d35298&language=en-EN&page=" + str(actual_page)
    try:
        r = requests.get(URL)
        if r.ok:
            print("okey!")
            d = r.json()
            print(d['total_pages'])
            lista_actores.append(d["results"][0]["id"])
            for actor in d['results']:
                lista_actores.append(actor['name'])


            if actual_page < 50:
                actual_page += 1
                get_peoples_id(actual_page)
            # return render_template('index.html', output=listita)
    except:
        pass
    return print(lista_actores)


if __name__ == '__main__':
    app.run()
