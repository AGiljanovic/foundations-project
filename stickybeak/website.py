from flask import Flask
from flask import render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

# configure Flask using environment variables
app.config.from_pyfile("config.py")


@app.route('/')
def index():
    return render_template('index.html', page_title="Stickybeak")


@app.route('/newsletter', methods=['GET', 'POST'])
def index_func():
    if request.method == 'POST':
        return redirect(url_for('newsletter'))
    return render_template('newsletter.html')


@app.route('/story', methods=['GET', 'POST'])
def story_func():
    if request.method == 'POST':
        return redirect(url_for('story'))
    return render_template('story.html')


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)

# ================== Database connections ==================

db = yaml.load(open('app.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASS'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        email = userDetails['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (email) VALUES (%s)", [email])
        mysql.connection.commit()
        cur.close()
        return redirect('/newsletter')
    return render_template('newsletter.html')


@app.route('/newsletter')
def users():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM users")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('newsletter.html', userDetails=userDetails)


if __name__ == '__main__':
    app.run(debug=True, host='localhost')
