from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return "Pierwsza aplikacja wwww!"

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
