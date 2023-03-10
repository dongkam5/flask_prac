from flask import Flask,render_template,url_for,redirect,escape,request,session,abort

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        if request.form['username']=='admin':
            return redirect(url_for('success'))
        else:
            abort(401)
    else:
        return redirect(url_for('index'))

@app.route('/success')
def success():
    return 'Logged in Successfully'

if __name__=='__main__':
    app.run(debug=True)
