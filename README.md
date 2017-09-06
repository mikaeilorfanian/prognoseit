# Intro
There's a guide for both backend and frontend development below. But, first please read this intro carefully.   


## Heroku
We've chosen to deploy on Heroku because it's free. We will probably change that in near future. Choosing Heroku has some consequences for the way you will develop this application. The most important consequences are:   
- Database: we'll use sqlite3 because it's free on Heroku. We can use Postgres, but that would make the server slow(free Heroku servers are already slow). Plus, if we want to seriously use Heroku + Postgres we'll have to pay for it. That's why **we should not consider the data saved to Heroku as persistent** right now. That's okay for now because we're not going to have real users in the near future.
- Free Heroku servers are slow. If the server is not used for some, it goes to "standby" mode. When you make a request to the sever in "standby" mode, there's a delay(10-20 seconds) until you get a response. So, the first call will be slow. But, the later calls will be faster.    


# Backend Development Guide

## Installing the Required Tools
*If you get stuck following the below commands, take a look at [this article](https://devcenter.heroku.com/articles/deploying-python).   *
First, [install heroku cli](https://devcenter.heroku.com/articles/heroku-cli). You will use this tool to develop locally.   
Then, fork this repo using your GitHub account.   
Then, download the repo(the one in your account) using this command: `git clone <repo_address>`.  
Go to the root directory of the project.   
Create a Python `virtualenv` and install the required packages: `pip install -r requirements.txt`.

## Running the App Locally
Run db migrations:   
`python manage.py migrate`   
Create a superuser. Don't forget the username and password you set here. You can change them later.   
`python manage.py createsuperuser`    
Run this command: `heroku local web`.    
Visit this page: `http://localhost:5000/users`. This is DRF's browsable API.   
This page shows the available URLs for user auth.

## Making Changes
*Leave the server running, and use another terminal to make changes to the application and the code. Heroku cli will automatically reload the server when you make changes.   *
Make changes to your own repo. Make sure you set the original repo as the upstream for the cloned repo.   
Then, using GitHub, create pull requests. Other devs will review the changes and after two thumbs up(two devs approving the change), someone will merge your changes to the main repo.  

# Frontend Development Guide
TODO
