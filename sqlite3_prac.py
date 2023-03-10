from flask import *
import sqlite3 as sql
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/enternew')
def new_student():
    return render_template('student.html')

@app.route('/addrec',methods=['POST','GET'])
def addrec():
    if request.method =='POST':
        con=sql.connect('database.db')
        try:
            nm = request.form['nm']
            addr=request.form['add']
            city=request.form['city']
            pin = request.form['pin']
            cur = con.cursor()
            cur.execute('INSERT INTO STUDENTS (NAME,ADDR,CITY,PIN) VALUES (?,?,?,?)', (nm,addr,city,pin))
            con.commit()
            msg='Record successfully added'
        except:
            con.rollback()
            msg='Error in insert operation'
        finally:
            con.close()
            return render_template('result.html',msg=msg)
            
    return ''

@app.route('/list')
def list():
    con=sql.connect('database.db')
    con.row_factory=sql.Row

    cur=con.cursor()
    cur.execute('SELECT * FROM STUDENTS')
    rows= cur.fetchall()
    return render_template('list.html',rows=rows)

if __name__=='__main__':
    app.run(debug=True)