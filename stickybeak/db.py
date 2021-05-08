import os
import pymysql

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


def add_emails(email):
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute('INSERT INTO emails (emails) VALUES(%s)',
                       (email["email"]))
    conn.commit()
    conn.close()

# create table emails(
# emails_id INT NOT NULL AUTO_INCREMENT,
# email VARCHAR(255),
# PRIMARY KEY(emails_id)
# );