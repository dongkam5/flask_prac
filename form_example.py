from flask import Flask,render_template,request,flash,url_for,redirect
from forms import ContactForm

app=Flask(__name__)
app.config['SECRET_KEY']='super-secret-random-key'

@app.route('/contact', methods=['GET','POST'])
def contact():
    form = ContactForm()
    if request.method =='POST':
        print(form.name)
        print(form.validate)
        if not form.validate():
            flash('All fields are required')
            return render_template('contact.html',form=form)
        else:
            return render_template('success.html')  
    elif request.method=='GET':
        return render_template('contact.html',form=form)

if __name__=='__main__':
    app.run(debug=True)
