from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "seguridad3"

@app.route('/')
def index():
    if len(session) == 0:
        session['registerGoldEarn'] = []
        session['registerActivity'] = []
        session['sumGold'] = 0
        return render_template('index.html')
    else:
        return render_template('index2.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    if request.form['building'] == 'farm':
        temp = random.randint(10, 12)
        session['sumGold'] += temp
        session['registerGoldEarn'].append(temp)
        session['registerActivity'].append('Has ganado: ')
        return render_template('index2.html')
    elif request.form['building'] == 'cave':
        temp = random.randint(5, 10)
        session['sumGold'] += temp
        session['registerGoldEarn'].append(temp)
        session['registerActivity'].append('Has ganado: ')
        return render_template('index2.html')
    elif request.form['building'] == 'house':
        temp = random.randint(2, 5)
        session['sumGold'] += temp
        session['registerGoldEarn'].append(temp)
        session['registerActivity'].append('Has ganado: ')
        return render_template('index2.html')
    else:
        temp = random.randint(-50, 50)
        if temp < 0:
            session['sumGold'] -= abs(temp)
            session['registerGoldEarn'].append(temp)
        else:
            session['sumGold'] += temp
            session['registerGoldEarn'].append(temp)
        if temp < 0:
            session['registerActivity'].append('Has perdido: ')
        else:
            session['registerActivity'].append('Has ganado: ')
        return render_template('index2.html')

if __name__=="__main__": 
    app.run(debug=True) 