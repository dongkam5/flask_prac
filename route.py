from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello'

@app.route('/hello')
def helloworld():
    return 'Helloworld'

@app.route('/hello/<name>')
def helloname(name):
    return 'Hello  {}'.format(str(name))

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)