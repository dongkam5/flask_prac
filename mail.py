from flask import *
from flask_mail import Mail,Message

app = Flask(__name__)
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']='465'
app.config['MAIL_USERNAME']='MyEmail'
app.config['MAIL_PASSWORD']='Mypassword!'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
mail=Mail(app)

@app.route('/')
def index():
    msg = Message('Hello', sender='MyEmail', recipients='recipients@naver.com')
    msg.body='Hello Flask message sent from Flask-Mail'
    mail.send(msg)
    return 'SENT'

if __name__=='__main__':
    app.run(debug=True)