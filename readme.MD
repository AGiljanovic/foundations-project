
# Foundations project: Stickybeak
A landing page for a Fake-news Detection App. Overview of what it is, what the background to it is, what it offers, and lastly, the newsletter, that's connected to a (broken) DB.

## Every Time You Develop on Your Project
- Activate your virtual environment for this project: 
   
    macOS/Linux: `source venv/bin/activate`
    
    Windows: `venv\Scripts\activate.bat`

- Point Flask to your application: 

    macOS/Linux:  `export FLASK_APP=main.py`
    
    Windows: `set FLASK_APP=main.py`
- Enable hot reloading, debug mode, and other useful features for local development:  

     macOS/Linux: `export FLASK_ENV=development`

    Windows: `set FLASK_ENV=development`
- run your flask application: 

    `flask run`

## While You're Developing... 

Whenever you deploy your code, it will be automatically testing and linted by the GitHub Action. To have a quicker feedback loop and to make sure there are as few surprises as possible, run the same commands locally, too:

To test your app: 

> pytest --doctest-modules

To Lint your app: 
> flake8 --exclude venv 


# Installation Instructions
You should have:
- Python 3.8.x installed on your computer 
- Visual Studio Code (or another IDE of your choosing) installed on your computer 

### Get Set Up for Local Development:
- Launch a virtual environment
    > python3.8 -m venv venv 

- Activate your virtual environment
- Install the requirements

    > pip install -r requirements.txt

- Run the local development server and make sure it all works. Instructions can be found at the top of this readme for using Flask's built in development server. Alternatively (only on macOS or Linux), you can use the command `uwsgi` to start your development server: 

> uwsgi --http-socket 127.0.0.1:5000 --wsgi-file great_project/website.py --callable app --processes 4 --threads 2 --stats 127.0.0.1:8181 -H venv/

You should be able to run the website locally and see it in your local browser! 

# Big final note
The website itself is not running perfectly, as the code for database connection is broken.  This happens while signing up for the newsletter.
It bypasses the POST request, and defaults to the JSON file that gives out an error.

If you want to see the where it leads add a /newsletter to the end of the page.
