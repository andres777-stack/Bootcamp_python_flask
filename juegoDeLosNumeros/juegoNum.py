from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "seguridad"

@app.route('/')
def juegoNum():
    session['numeroAleatorio'] = random.randint(1, 100)
    return render_template('index.html')

@app.route('/userNum', methods=['POST'])
def userNumber():
    session['numeroUsuario'] = int(request.form['numeroUser'])
    return redirect('/result')

@app.route('/result')
def mostrarResultado():
    if session['numeroUsuario'] > session['numeroAleatorio']:
        cadena = "Muy Alto!"
        color = "red"
    elif session['numeroUsuario'] < session['numeroAleatorio']:
        cadena = "Muy Bajo!"
        color = "red"
    else:
        cadena = "Haz adivinado!"
        color = "green"
    return render_template('resultado.html', texto = cadena, color = color)

if __name__=="__main__": 
    app.run(debug=True) 

    #crear numero aleatorio
    #asignar el numero aleatorio a session['numeroAleatorio']
    #recibir el numero del usuario, que debe venir con el formulario, no en la ruta (no olvidar que viene como string)
    #if son iguales: elif el numero de usuario es mayor que el asignado aleatoriamente = "muy alto" (en var)
    #else al mismo nivel de elif: en var muy bajo. 
    #es la misma variable la que tiene que escribir los resultados de los if. En cada juego, esa misma variable se 
    #sobreescribe. 
    #En definitiva son tres variables. Una que es generada random, otra por el usuario y la tercera es el string que 
    #se genera por la lógica del if-elif-else. (mayor, menor, igual)
    #luego estas se deben pasar como parámetros, menos la session. 
    #hay que generar una session con el numero random, luego una variable con el numero de usuario -en otra ruta-.
    #hay que generar una tercera ruta get, donde se expone los resultados del juego. Las rutas: 2 get y 1 post. 


