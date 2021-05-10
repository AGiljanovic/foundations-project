

# What the heck is Stickybeak 🦜
Well, it's my SE foundations project.
A landing page for a (fictional) Fake-news Detection App. Basically, you get to see what it is, what the background / story to it is, what it offers / can do, and lastly, the newsletter, that's connected to a DB. 

# Installation Instructions 👩‍🏫
You decided that you feel like making this thing your own but you have no clue how to. No problem, I can guide you through it! 🗺

## Before you start 🎬
You should have:
- Python 3.8.x installed
- Visual Studio Code / another IDE of your choosin installed
- Github account

### Get your own one, man! ✂️📋
You got all of the things above installed? Then, you can make this project your own now:

- Fork this repository to your own GitHub account. 
-   Choose / create a working directory on your own computer and change directory into it
-   Clone  _your_  version onto your computer in that working directory.

That's pretty much it for this part, you're ready to get the project running on your own computer.

### Get Set Up for Local Development: 💻
We don't want to install packages across our entire computer, so let's keep it in a virtual environment, yeah?
- Launch a virtual environment
    > `python3.8 -m venv venv `

- Activate your virtual environment
	>`source venv/bin/activate`
- Install the requirements
    > `pip install -r requirements.txt`

Nice, nice. You're done with this part now.

# Using the repo, and how to get it to work 💪
Let's get the project going, yeah? 

## While You Develop Your Project 🛠
You have to do this every time, by the way.
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

### You like testing? 🧪
To test your app: 

> pytest --doctest-modules

To Lint your app: 
> flake8 --exclude venv 

# Deployment on Heroku 🚀
We need to do a few preparations before we get it going, but I will guide you through it.

## Setup the sqlite database locally 📊

In order to set up a database, we have to do the following steps:
- make sure you are using a virtual environment ***and*** in the correct directory, if not cd into it, otherwise errors will kick up

1.  Open the python console:  `python3` 
2.  Import the database from our project:  `from app import db`
3.  Create the database file:  `db.create_all()`
4.  Close the console:  `exit()`

Now a file should've been created, that's gonna be your database.

## Got Git? 👾
We will use the  [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)  below. It integrates nicely with git. So ideally you use git with your project to keep things easier.

You want to use git as a version control for your application, so go ahead and install it if you don't have it. Not sure if it's installed? Run  `git` in your terminal.

Here's a speed run version of how to use git:
- go into the project directory
`git init`
`git add .`
`git commit -am "initial commit"`

## Set up your project on Heroku 💡

1.  Create an account on  [Heroku](https://heroku.com/)
2.  Install the  [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli). This will allow you to manage and deploy to your Heroku app right from the command line.
3.  Now login with the CLI running:  `heroku login -i`
4.  If you haven't already, navigate to your project directory within the command line and now run  `heroku create`. This will create a project on Heroku for your app. Go to the dashboard on  [heroku.com](https://heroku.com/)  and you will see it show up there.

- once you are done creating, you will get your app name, you will need this
	- Example:  `gentle-waters-75094` 

## Preparing for deployment 🎒
I know, preparations for preparations, but I promise there's not a lot, just 2 small steps.

### STEP 1: Tell it how to run the server ❓
Create a file in the **root** of your project folder called  `Procfile`.

Add the following line to it:  `web: gunicorn --chdir stickybeak app:app`
- since our app isn't in the root dir, we're gonna have to move ourselves to that folder with the handy little `--chdir`. 
- If you decide to shove app.py into the same folder as `Procfile`, leave that bit out

That's it. This file tells Heroku to use  [gunicorn](https://gunicorn.org/)  (the package we installed earlier) as a web server for our application.

### STEP 2: Set up our Postgres database on Heroku ⚙️
As a database we use Postgres. In Heroku, databases are added to your project as so called "addons". Heroku offers a free version of Postgres which we will use.

To add the Postgres addon to your project simply replace "your-app-name-123" with your application name and run the following command:

 `heroku addons:create heroku-postgresql:hobby-dev --app your-app-name-123 `
 
*(Remember that funky looking name you got from the CLI earlier? That's the app name. It probably looks something like this: `gentle-waters-75094.`)*

Sweet Heroku will now create a database for us.

## Deployment (finally!) moon🚀✨
This is the bit that you worked for. Now that the application is set up, you can deploy to Heorku!
Heroku CLI uses the git workflow, so you can use this handy dandy command:
`git push heroku main`

_or if you're using  `master`  you run  `git push heroku master`_

### Just a second, you're not done ✋
Don't forget to initialise the database! Don't be like me, seriously. It will save you unnecessary debugging time.

The very first time you delpoy your app you have to initialize your database again the same way you did it locally before. On Heorku you do it with the following commands:
`heroku run python`


Now you are in the python console but on the Heroku server. 
- Since our app.py is in a different folder (if you haven't relocated anything), we're going to have to move ourselves around bit
- It works the same as it does on the terminal, just with slightly different commands:
	-	` import os` 
	- `os.system("ls")`
	- `os.chdir('..') `
- We're looking for the folder that contains the app.py, so "stickybeak". Move into it.

- Once we're in the correct folder run:
`from app import db`
`db.create_all()`
`exit()`
> Getting errors that it cannot find app? You're in the wrong folder, fix this with the steps above.

*(The database part is done. Unlucky for you, you have to do this **every single time** you change something about your database set up. At least it's quick to do?🤷‍♀️)*

---
### **And that's it! You are done! Your app is live on Heroku!** 🎉
The CLI will return a URL like this one https://gentle-waters-75094.herokuapp.com which is the URL of your application. You can click it and should see your application live. 
> don't copy paste the link that ends with .git. That's just the repo location, and shows an error when pasted in the browser. 
