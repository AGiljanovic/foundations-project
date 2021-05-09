from flask import Flask
from flask import render_template, request, redirect, url_for, jsonify
import os
import pymysql

app = Flask(__name__)

# configure Flask using environment variables
app.config.from_pyfile("config.py")


db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')


def open_connection():
    unix_socket = '/cloudsql/{}'.format(db_connection_name)
    try:
        if os.environ.get('GAE_ENV') == 'standard':
            conn = pymysql.connect(user=db_user, password=db_password,
                                   unix_socket=unix_socket, db=db_name,
                                   cursorclass=pymysql.cursors.DictCursor
                                   )
    except pymysql.MySQLError as e:
        print(e)

    return conn

# adding to the db
def add_emails(email):
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute('INSERT INTO userdetails (email) VALUES(%s)',
                       (email["email"]))
    conn.commit()
    conn.close()


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


@app.route('/', methods=['POST', 'GET'])
def emails():
    if request.method == 'POST':
        if not request.is_json:
            #  return jsonify({"msg": "Missing JSON in request"}), 400  
            # sadly, I had to use this sad workaround, it is not connecting to
            # the database as I hoped.
            return render_template('newsletter.html')

        add_emails(request.get_json())
        return render_template('newsletter.html')

    return render_template('newsletter.html')


if __name__ == '__main__':
    app.run(debug=True, host='localhost')

