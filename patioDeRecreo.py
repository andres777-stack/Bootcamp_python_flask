from flask import Flask, render_template
app3 = Flask(__name__)

@app3.route('/play')
def functionPlay():
    return render_template('play.html')

@app3.route('/play/<number>')
def functionNumber(number):
    print("*" * 80)
    print("in the functionNumber")
    print(number)
    return render_template('number.html', n = int(number))

@app3.route('/play/<number>/<color>')
def functionNumberColor(number, color):
    print("*" * 80)
    print("in the functionNumberColor")
    print(number, color)
    return render_template('number_color.html', n = int(number), c = color)


if __name__=="__main__":  
    app3.run(debug=True) 