# A/B Testing

## Overview

A/B testing is a user research technique, which is used to test
which among the A or B version is better design.

For a commercial marketplace the success metric could be
calculated based on "conversion rate".

## What does this project do?

This project does simple A/B testing, of 2 versions of a website.

The metrics collected could then be used to see which version 
among the baseline or variant 
performed better.

# Running the flask server

## Running locally

### Method 1:
 export FLASK_APP=app.py
 flask run

### Method 2:
 python app.py


#Hosting on Heroku
 In order to host this on heroku, follow the following steps.

## Ensure heroku CLI is installed

  STEPS:
  Run the following on iterm/terminal.
  1. Install brew if not installed - 
  /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

  2. Install heroku toolkit. CLI is part of toolkit. 
  brew install heroku-toolbelt

## Following are must.
### Procfile - this is the file heroku looks in your home directory
 It should contain the command to start your web app.

 For example, if you run your web app locally as
 'python app.py'
 this file should contain 
 web: python app.py

 The initial command 'web' is specific to heroku.
 Otherwise it does not know that it should follow
 http protocol for your app.

### requirements.txt
 Heroku looks for this in home directory.
 Add all dependencies here.

## Full details at https://devcenter.heroku.com/articles/deploying-python

## Sample Output while testing locally:

Creates output file of the following format.

Aarthis-iMac:a-b-testing aarthi$ cat ab_testing.csv
Version,pageLoadTime,clickTime
B,2017-09-06 19:50:05.202000,2017-09-06 19:50:06.484000
A,2017-09-06 19:50:08.579000,2017-09-06 19:50:09.284000

