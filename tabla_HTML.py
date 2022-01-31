from flask import Flask, render_template
app6 = Flask(__name__)
@app6.route('/')
def tableFunction():
    users = [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    return render_template('tablaHTML.html', usuarios = users)

if __name__=="__main__":  
    app6.run(debug=True) 

