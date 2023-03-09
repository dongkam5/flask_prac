from flask import Flask

app=Flask(__name__)

@app.route('/blog/<int:postID>')
def show_blog(postID):
    return 'Blog number is {}'.format(postID)

@app.route('/rev/<float:revNO>')
def revision(revNO):
    return 'Revision number is {}'.format(revNO)

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)