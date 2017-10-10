# Mac

## This file to be used only by Mac/Linux USERS

1. Signup for a free heroku account here - https://signup.heroku.com/
    Choose primary development language as Python while signing up.
    Don't forget the user name and  password. You will need it
    throughout this assignment.

2.   We have to install heroku CLI(Command Line Interface).
     As CLI is part of toolkit, we will now install toolkit.

      Run the following on iterm/terminal.[Only if brew is not
      installed on your Mac already]

     /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

     Brew takes atleast 5-10minutes to install for the first time.

     Once brew is installed,
     run the following on iterm/terminal to install heroku toolkit.
     CLI is part of toolkit.

      brew install heroku-toolbelt

3. Open a terminal on Mac.

4. Goto a folder where you have to download your a-b-testing folder.

5. Type in the following commands one after another.

        cd a-b-testing
        heroku login

    Use the email/password you used for signing up in step 1 above.

7. Type in the following commands.

        heroku create
  This should output something similar to this.

  Creating app... done, ⬢ <randomappname>
  https://<randomappname>.herokuapp.com/ | https://git.heroku.com/<randomappname>.git

8.  To update the changes you make each time to A.html or B.html, please use
   the following commands one by one.
        
        git add .  
        git commit -am "Commit message"
        git push heroku master
        
    For the first time, pushing might take some time.
    Subsequent runs would be little faster.
    At the very end, it would output a heroku app link,
    which can be opened in a browser.

    For the first time, you will just create app with stencil
    code provided in Step 4.
    For the purpose of A/B testing assignment, we want you to
    modify A.html and B.html in
    'templates' folder of stencil code and we want you to run
    commands from this step(step 8), to push/host your
    changes.

10. Type in the following commands.
    heroku open
    
    This should open the sample app in chrome automatically.
    If it does not open, you can
    try opening the link manually.

For any doubts or to debug issues about heroku, you can read more here..
https://devcenter.heroku.com/articles/getting-started-with-python#deploy-the-app
