from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config.from_pyfile("config.py")

# Thank you for this
# https://github.com/samlawski/flask-postgres-heroku-demo#-deployment-on-heroku

# Initialize database
if os.environ.get('DATABASE_URL'):
    # Set the database URL from the environment variable if it is set.
    # The .replace() is a workaround because of a mismatch
    # between Heroku's default set up and SQLAlchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)
else:
    # Use SQLite as a fallback and locally
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)


# A basic model for Todos storing some text and the date of creation:
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Task %r>' % self.id


# Routes
@app.route('/newsletter', methods=['POST', 'GET'])
def newsletter_index():
    if request.method == 'POST':
        # The POST request is done by the form in the index.html file.
        # It creates a new todo in the database
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            # Try to write the new todo in the database:
            db.session.add(new_task)
            db.session.commit()
            return render_template('newsletter.html', page_title="Stickybeak")

        except:
            # return 'The email could not be added' 
            # the page opts for this, but for viewing purposes I will do this.
            return render_template('newsletter.html', page_title="Stickybeak")
    else:
        return render_template('newsletter.html', page_title="Stickybeak")


# PAGES
@app.route('/')
def index():
    return render_template('index.html', page_title="Stickybeak")


# @app.route('/newsletter', methods=['GET', 'POST'])
# def index_func():
#     if request.method == 'POST':
#         return render_template('newsletter.html',
#                                page_title="Stickybeak Newsletter")
#     return render_template('newsletter.html',
#                            page_title="Stickybeak Newsletter")


@app.route('/story', methods=['GET', 'POST'])
def story_func():
    if request.method == 'POST':
        return render_template('story.html',
                               page_title="Stickybeak Story")
    return render_template('story.html',
                           page_title="Stickybeak Story")


if __name__ == '__main__':
    app.run(debug=True, host='localhost')
