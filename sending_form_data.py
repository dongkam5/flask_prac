from flask import Flask,request,render_template

app=Flask(__name__)

@app.route('/')
def student():
    return render_template('sending_form_data.html')

@app.route('/result',methods=['POST','GET'])
def result():
        if request.method=='POST':
            result=request.form
            return render_template("sending_form_data_result.html",result=result)

if __name__=='__main__':
    app.run(debug=True)