from flask import Flask
from flask import request
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        return request.form['username']
    else:
        return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

if __name__ == "__main__":
    app.debug=false
    app.run(host='0.0.0.0')