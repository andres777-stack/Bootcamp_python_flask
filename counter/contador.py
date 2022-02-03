from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "seguridad2"

@app.route('/')
def contador():
    if len(session) == 0:
        session['contador'] = 1
    else: 
        session['contador'] += 1
    return render_template('conta.html')

@app.route('/destroy')
def destroy():
    session.pop('contador')
    return redirect('/')

if __name__=="__main__": 
    app.run(debug=True) 