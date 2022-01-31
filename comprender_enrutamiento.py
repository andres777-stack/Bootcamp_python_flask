from flask import Flask

app2 = Flask(__name__)
@app2.route('/')
def myFunction():
    return "Hola mundo!"

@app2.route('/Dojo')
def mySecondFun():
    print("*" * 80)
    print("in my second function")
    return "Dojo!"

@app2.route('/say/<name>')
def myThirdFunction(name):
    print("*" * 80)
    print("in my third function")
    print(name)
    return f"Hello {name}"

@app2.route('/repeat/<number>/<word>')
def myFourthFun(number, word):
    print("*" * 80)
    print("in my fourth function")
    print(number, word)
    return f"{word} " * int(number)

if __name__ == '__main__':
    app2.run(debug=True)