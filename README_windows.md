# WINDOWS

## This file to be used only by WINDOWS USERS

1.  Signup for a free heroku account here - https://signup.heroku.com/
    Choose primary development language as Python while signing up.
    Don't forget the user name and  password. You will need it
    throughout this assignment.

2.   We have to install heroku CLI(Command Line Interface).
     As CLI is part of toolkit we will now install toolkit.
     from this link below. Choose your windows version and install it,
     https://devcenter.heroku.com/articles/getting-started-with-python#set-up
     Follow the regular installation procedure, by clicking on 'Next/Continue'.

3. Open Powershell on windows.
    [Click on Windows button on your keyboard. Search for powershell. Open powershell by
    double-clicking it]
    Following commands to be run on powershell.
4. Goto a folder where you have downloaded your a-b-testing folder.

    cd a-b-testing

    heroku login

 Use the email/password you used for signing up in step 1 above.

7. Following commands to be run on powershell.
    heroku create
  This should output something similar to this.
  Creating app... done, ⬢ <randomappname>
  https://<randomappname>.herokuapp.com/ | https://git.heroku.com/<randomappname>.git

8.  Following commands to be run on powershell.
 To update the changes you make each time to A.html or B.html, please use
   the following commands one by one.

    git commit -am "<Commit message>"
    git push heroku master

  For the first time, pushing might take some time.
  Subsequent runs would be little faster.
  At the very end, it would output a heroku app link,
  which can be opened in a browser.

    For the first time, you will just create app with stencil
    code provided in Step 4.
    For the purpose of A/B testing assignment, we want you to
    modify A.html and B.html in
    'templates' folder of stencil code and we want you to
    run commands from this step(step 8), to push/host your
    changes.


10. Following commands to be run on powershell.
    heroku open
  This should open the sample app in chrome automatically.
  If it does not open, you can
  try opening the link manually.

  For any doubts or to debug issues about heroku, you can read more here..
  https://devcenter.heroku.com/articles/getting-started-with-python#deploy-the-app
