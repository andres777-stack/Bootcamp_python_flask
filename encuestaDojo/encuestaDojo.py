from flask import Flask, render_template, request, redirect
app7 = Flask(__name__)

@app7.route('/')
def encuestaDojoFun():
    return render_template('index2.html')

@app7.route('/procesar', methods=['POST'])
def procesarEncuesta():
    nombre_desde_form = request.form['nombre']
    email_desde_form = request.form['email']
    pais_desde_form = request.form['pais']
    lenguaje_desde_form = request.form['lenguaje']
    return render_template('show2.html', nom = nombre_desde_form, em = email_desde_form, pa = pais_desde_form, len = lenguaje_desde_form)


if __name__ == '__main__':
    app7.run(debug=True)