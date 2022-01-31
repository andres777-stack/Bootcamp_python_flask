from flask import Flask, render_template  # Importar Flask para que permita crear nuestra aplicación
app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

@app.route('/')          # El decorador "@" asocia la ruta con la función siguiente
def hello_world():
    return render_template('index.html', phrase = "hello", times = 5)  # Retorna la cadena 'Hello World!' como respuesta


# declaraciones de importacia, tal vez algunas otras rutas
@app.route('/success')
def success():
    return "success"

@app.route('/hello/<name>') # para una ruta '/hello/____' cualquier cosa despues de '/hello/' se pasa como una variable 'name'
def hello(name):
    print("*" * 80)
    print("in the hello function")
    print(name)
    return f"Hello {name}"


@app.route('/users/<username>/<id>') # para una ruta '/users/____/____', dos parámetros en la url se pasan como nombre de usuario e id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

@app.route('/lista')
def listaDeObjetos():
    estudiantes = [
        {'name' : 'Michael', 'age' : 35},
        {'name' : 'John', 'age' : 30 },
        {'name' : 'Mark', 'age' : 25},
        {'name' : 'KB', 'age' : 27}
    ]
    return render_template('lists.html', random_numbers = [3, 1, 5], estudiantes = estudiantes)

if __name__=="__main__":   # Asegúrese de que este archivo se ejecute directamente y no desde un módulo dif<erente
    app.run(debug=True)    # ejecuta la aplicación en modo depuración