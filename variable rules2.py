from flask import Flask

# 뒤에 / 있는 것과 없는 것 차이
app=Flask(__name__)
@app.route('/flask')
def hello_flask():
    return 'Hello Flask'

@app.route('/python/') 
def hello_python():
    return 'Hello Python'

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)