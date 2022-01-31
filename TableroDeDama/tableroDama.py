from flask import Flask, render_template
app4 = Flask(__name__)
@app4.route('/')
def function8por8():
    return render_template('damaOchoPorOcho.html')

@app4.route('/4')
def function8por4():
    return render_template('damaOchoporCuatro.html')

@app4.route('/<num>/<number>')
def functionNumPorNum(num, number):
    return render_template('damaNumPorNum.html', numero1 = int(num), numero2 = int(number))

if __name__=="__main__": 
    app4.run(debug=True) 