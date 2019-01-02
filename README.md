
## **Table of Contents**

- [**Riddle Game**](#riddle-game)
	- [**CI Brief**](#ci-brief)
	- [**UX**](#ux)
		- [General Design](#general-design)
		- [Requirements](#requirements)
		- [Wireframes](#wireframes)
		- [Template](#template)
	- [**Features**](#features)
		- [Existing features](#existing-features)
		- [Features left to implement](#features-left-to-implement)
	- [**Technologies used**](#technologies-used)
		- [Front End](#front-end)
		- [Back End](#back-end)
	- [**Testing**](#testing)
		- [Tools used for testing](#tools-used-for-testing)
	- [**Changelog and Fixes**](#changelog-and-fixes)
		- [Before v1.0](#before-v10)
		- [v1.0](#v10)
		- [v1.1](#v11)
		- [v1.2](#v12)
		- [v1.3](#v13)
		- [v1.4](#v14)
		- [v1.5](#v15)
	- [**Deployment**](#deployment)
	- [**How to run the project locally?**](#how-to-run-the-project-locally)
	- [**What could be done better?**](#what-could-be-done-better)
	- [**Credits**](#credits)
		- [Special thanks to](#special-thanks-to)
		- [Questions](#questions)
		- [Bootstrap template](#bootstrap-template)

<hr />

# **Riddle Game**

Hello there,  
and welcome to my third [Code Institute (CI)](https://courses.codeinstitute.net/) school project.  
In this project I should be able to show that I can work with Jinja, Python and Flask (a python framework) as well as create responsive design which works on commonly used devices.

I decided to follow the given example from CI for this project.

<hr />

## **CI Brief**

- **CREATE A 'RIDDLE-ME-THIS' GUESSING GAME**
  - Build a web application game that asks players to guess the answer to a pictorial or text-based riddle.
  - The player is presented with an image or text that contains the riddle. Players enter their answer into a text area and submit their answer using a form.
  - If a player guesses correctly, they are redirected to the next riddle.
  - If a player guesses incorrectly, their incorrect guess is stored and printed below the riddle. The text area is cleared so they can guess again.
  - Multiple players can play an instance of the game at the same time, each in their own browser. Users are identified by a unique username but note that no authentication features such as a password are required for this project.
  - Create a leader board that ranks top scores for all (at least recent) users.

- **CREATE YOUR OWN PROJECT**
  - If you choose to create your project outside the brief, the scope should be similar to that of the example brief above. If you want some ideas, please ask your mentor for advice and direction.

<hr />

## **UX**

### General Design

Design | Importance
--- | ---
Functionality | 6
User experiences | 6
HTML / CSS | 3

**The project general idea is for entertainment purpose only.**

- create an application which feels good for the user
  - achieve this using more JS with user inputs instead of Python
  - create responsive design for the project or use a template
- do not limit the user (1 user can have as many game profiles as he wishes)

### Requirements

- **Welcome page**
  - create account / log-in
- **Any other page**
  - show riddle profiles
  - link to statistics page
  - friends list (optional)
  - chat window (optional)
- **Game setting page**
  - Brief how to play the game
  - Let user create a profile
- **Riddle game page**
  - Show riddle to user
  - Show game score
  - User actions
    - submit answer
    - skip question
    - delete question
    - give user appropriate feedback depends on result from the action
- **Statistics page**
  - show score for user and his profiles
  - show overall or top 10 score
- **Database**
  - *At time I started this project I knew very little about Flask session or Heroku file system.  Therefore I choose to create app which works with files such as `.txt` and `.json`.*
    - create separate files for each user / profile
    - user should be able to access only his own data

### Wireframes

Base on the above I created basic mock-up using [Balsamiq](https://balsamiq.com/) which can be find [here](https://github.com/MiroslavSvec/project-3/blob/master/assets/mockup.pdf). 

### Template

As this was my first Python project I decided to fully focus on Python and Flask. Therefore, I wanted to speed up the development and try to find a template/s which I could use for this project.

At the end I was able to find [this](https://blackrockdigital.github.io/startbootstrap-sb-admin/index.html) template which suits my project almost perfectly. I choose the above template mainly because of the `side-nav` and the chat window in main `nav`.

Also with the above template and friends list I wanted to create a small social page with more minigames then just the Riddle game.  
This is why the game profile list starts with "Games" instead of "Riddles".

*Please read the [***Credits***](#Credits) section to see what I kept and changed.*

[**To top**](#Table-of-Contents)

<hr />

## **Features**

### Existing features

- [**index.html**](https://github.com/MiroslavSvec/project-3/blob/master/templates/index.html)
  - **Create Account / Login form**
    - allow user to create an account
    - allow user to log-in to existing account
    - "Easter egg" show user how many user accounts has been created to test the app
- **Any other page**
  - **Navigation**
    - **Side Navbar**
      - show user name of current user logged in
      - **Games**
        - **Riddles**
          - "New Game" allow user to access Riddle game setting and start new game
          - show game profiles (if exists) for logged user
      - **Statistics**
        - allow user to access statistics page
      - **Log-out**
        - allow user to log out from current session (via modal)
- [**riddle-g-setting.html**](https://github.com/MiroslavSvec/project-3/blob/master/templates/riddle-g-setting.html)
  - **Game rules**
    - brief the user about game rules and how to play the Riddle game
  - **Please choose how to play**
    - allow user to create new Riddle game profile
      - **"Profile name"**
        - *as mentioned above I did not want to limit the user or forced him to create new account for every new game.  
        Therefore the user can have as many Riddle game profiles as he wish as long as the profile name is unique.*
      - **Question Category**
        - allow user to choose from 3 Question categories
          - [All questions](https://github.com/MiroslavSvec/project-3/blob/master/data/riddle-game/all.json)
          - [General](https://github.com/MiroslavSvec/project-3/blob/master/data/riddle-game/general.json)
          - [Mixed](https://github.com/MiroslavSvec/project-3/blob/master/data/riddle-game/mixed.json)
      - **Game Mods**
        - allow user to choose from 2 different Riddle game modes
          - **Endless**
            - user can answer wrongly as many times as he wishes  
            *Wrong answers are recorded; however, they have no impact on overall score.*
          - **Limited**
            - user has limited tries (wrong answers) depends on the number of tries he choose  
            *The game will end if tries are equal to 0 and this mod is selected*
- [**riddle-game.html**](https://github.com/MiroslavSvec/project-3/blob/master/templates/riddle-game.html)
  - **Navigation**
    - **Top Navbar**
      - allow user to see current score of the game
        - **Questions left** - show number of questions left to answer
        - **Tries left** - show number of tries left (if limited mod is selected)
        - **Correct answers** - show number of correct questions answered
        - **Wrong answers** - show number of wrongly answered question
        - **Skipped questions** - show number of skipped questions
        - **Deleted questions** - show number of deleted questions
    - **Side Navbar**
      - show Riddle profile name
  - **Main**
    - show current question with user actions
    - **User actions**
      - **Submit answer**
        - allow user to submit his answer to current question depends on the input field in `form`
      - **Skip Question**
        - allow user to skip current question. The skipped question will be appended to end of the list and can be answered again. Also, last question cannot be skipped. If the user does not know the correct answer to the last question, he must delete the question to finish the game.
      - **Delete Question**
        - allow user to delete question from the game if he does not know the answer. The question will be permanently deleted from the game and cannot be answered again. Also, this will affect the overall score of the user profile.
    - **Game end**
      - *Whenever there are no questions left to answer the game will ends. The score will be calculated and displayed to user. After 10 seconds the user will be automatically transferred to "Statistic" page.*
- [**statistics.html**](https://github.com/MiroslavSvec/project-3/blob/master/templates/statistics.html)
  - **Score for current user logged in**
    - allow user to see his score for each (finished) game profile (if any)
    - if there are not any finished game profiles user can access New game setting instead
  - **Top 10**
    - allow user to see the "Top 10" table of Riddle game profiles sorted by amount of **correctly answered** questions.
- [**helper.py**](https://github.com/MiroslavSvec/project-3/blob/master/helper/helper.py)
  - *As the project works constantly with reading / writing to `.txt` and `. json` files I decided to create a separate `helper.py` with general functions for reading and writing those files.*  
  *However, this makes the code hard to read sometimes as I am constantly passing functions to function.*  
  *Maybe better approach will be to assign those functions to variables for better readability as suggested by my mentor.*
- [**riddle.py**](https://github.com/MiroslavSvec/project-3/blob/master/riddles/riddle.py)
  - *I decided to create separate file for the game itself as I did not want to keep it in main app as well as this supposed to be a small social page with many additional games as mentioned before.*

### Features left to implement

- [**index.html**](https://github.com/MiroslavSvec/project-3/blob/master/templates/index.html)
  - Create Account / Login form
    - check user password (not required for this project)
- **Any other page**
  - **Navigation**
    - **Top Navbar**
      - **Chat window**
        - allow user to view new / old messages from other users
        - allow user to write a message to another user
    - **Side Navbar**
      - show users friend list (if any)
      - let the user search for other users and add them to their friend list
- [**riddle-game.html**](https://github.com/MiroslavSvec/project-3/blob/master/templates/riddle-game.html)
  - **Skip Question**
    - create functionality where skipped questions will affect the overall score
    - remove "Skip question" button if this is the last question to answer
- [**statistics.html**](https://github.com/MiroslavSvec/project-3/blob/master/templates/statistics.html)
  - The overall score which is displayed at the end of the game has no actual affect in the "Statistics" page. The table is sorted by most answered questions which can be misleading as the overall score can be different. This should be changed and let the app to sort the game profiles based on the score. However, this will require some work:
    - send another request to server via JS to update the user profile score at the end of the game
    - let Python to calculate and update the profile score at the end of the game and just send the final figure back to front end (better approach)
- **Database**
  - allow users to delete profiles
    - I gave this functionality less importance as there is not too many questions and / or mods varieties.
  - automatically delete current game profile after the game finish
    - profile data are no longer used after the game finish, so they should be removed from the server
  
[**To top**](#Table-of-Contents)

<hr />

## **Technologies used**

### Front End

- [Bootstrap 4.0.0](https://getbootstrap.com/docs/4.0/getting-started/introduction/)
  - The project uses **Bootstrap** to speed up the development.
- [Font Awesome 4.7.0](https://fontawesome.com/)
  - The project uses **Font Awesome** for icons.
- [jQuery v3.3.1](https://blog.jquery.com/2018/01/20/jquery-3-3-1-fixed-dependencies-in-release-tag/)
  - The project uses **jQuery** for better user experiences as well as sending requests to server.
    - [jQuery Easing](https://cdnjs.com/libraries/jquery-easing) - used for "back to top button"

### Back End

- [Flask 1.0.2](http://flask.pocoo.org/docs/1.0/) a micro web Python framework
  - **Flask** was used to build the application as well as to speed up the development process.

[**To top**](#Table-of-Contents)

<hr />

## **Testing**

The project has been tested on commonly used devices and browsers such as:

- Desktop PC
  - Chrome 70 (fully compatible)
  - Opera 57 (fully compatible)
  - Firefox 63 (fully compatible)
  - Internet Explorer 11 (not compatible)
    - the application cannot pass the create account or log-in on `index.html`
  - Microsoft Edge 42 (fully compatible)

- Tablets
  - Nexus 7 - Chrome 69 (fully compatible)
  - iPad air - Safari (not compatible)
    - due to `onclick` events not firing up

- Mobiles
  - Samsung Galaxy - Chrome 69/70 (fully compatible)
  - Samsung Galaxy - Samsung Internet 8.2 (fully compatible)
  - iPhone - Safari (fully compatible)

### Tools used for testing

- **Front End**
  - [W3C Markup Validation Service](https://validator.w3.org/) (All pages)
    - Document checking completed. No errors or warnings to show.

  - [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) (All pages)  
    *Below errors and warnings has not been resolved yet. They all come from the Bootstrap theme.*
    - Sorry! We found the following errors (29)
    - Warnings (1003)

  - [JSHint](https://jshint.com/) (Report of all custom JS functions)
    - **Metrics**
      - There are 41 functions in this file.

      - Function with the largest signature take 6 arguments, while the median is 1.

      - Largest function has 11 statements in it, while the median is 3.

      - The most complex function has a cyclomatic complexity value of 6 while the median is 1.
    - **Seven unused variables** (as the below functions are called form templates)
      - create_profile
      - check_login_details
      - hide_alerts
      - create_riddle_game
      - riddle_game_answer
      - skip_question
      - delete_question
- **Back End**
  - [Jupyter Notebook](https://jupyter.org/index.html)
    - *Most of the functions has been pre-written and tested in **Jupyter Notebook**.*

  - [Visual Studio Python debugger](https://code.visualstudio.com/docs/python/debugging)
    - *Mostly used after **Jupyter Notebook** testing.*

  - [Postman](https://www.getpostman.com/)
    - To send fake requests to server  
    *I was very new to **Postman** at the time I started to build this application and therefore **Postman** wasn't used as much as the two above.*

[**To top**](#Table-of-Contents)

<hr />

## **Changelog and Fixes**

*[Git](https://git-scm.com/) has been used for version control.*

- There are 7 different branches:

  - [master branch](https://github.com/MiroslavSvec/project-3/tree/master) Used in production.  
    - *The application is built from this branch on **Heroku***

  - *6 other branches has been created for development purpose only. Where each branch represent different version of the application.*

### Before v1.0

**Not a branch!**

*Represent main development process before I started to use different branches for each version.*

- **Changelog**  
  *Unfortunately this version of the application was never really documented, however the applications as well as 99% of features was built in this version.  
  Commit `0c0f5b896f4cc48285cf52dfb50c37cd3566103c` is the last commit of this version.*
- **Fixes**
  - <strike>Need to update localStorage when swapping between profiles</strike>
    - localStorage no longer in use

  - Need to redirect if riddle game data already exists
    - Fixed with if statement on load

  - Check values of the profile

  - Check if profile already exist

  - Fix bug when all-profiles.txt exist without data (redirect)
    - Fixed with checking if the len(profiles) is > 0

  - Fixed bug with injecting nav links (multiple click adds to link)

  - Fixed bug with game profiles not showing while playing the game

  - Fix "index out of range" while loading statistics without finished game
    - Fixed (removed last index call which was misleading) 

### [v1.0](https://github.com/MiroslavSvec/project-3/tree/v1.0)

- **Changelog**
  - Added session
  - Changed view names `get()` and `post()` to `log_in()` and `create_profile()`.
  - Added logout view
  - Removed unnecessary files
- **Fixes**
  - Found major bug `helper.py` line 133
    - whenever user answered wrongly the game ended. As due to indentation this if statement was always true on endless mode as the tries were always 0.  
    *Unfortunately, I discovered the bug while playing with a friend at the same time, so I misplaced it as bug related to multiplayer and decided to add Flask sessions.*  
    *After debugging the code in Visual Studio I found the core of the problem.*  

### [v1.1](https://github.com/MiroslavSvec/project-3/tree/v1.1)

- **Changelog**
  - Redesigned statistic page base on existing theme for the template.
  - Added [statistics.json](/data/riddle-game/statistics.json) for storing all finished games
  - Added functionality to sort the profiles in [statistics.json](/data/riddle-game/statistics.json) based on the `correct_answers`
  - Redesigned score system
- **Fixes**  
  - [riddle-g-setting.html](/templates/riddle-g-setting.html)
    - 500 error when user tried to create profile under user name with finished game
  - [riddle-game.html](/templates/riddle-game.html)
    - error with double `alerts` id.
  - [statistics.html](/templates/statistics.html)
    - game profile links not showing in `nav`.
    - broken link to game setting in `nav`.

### [v1.2](https://github.com/MiroslavSvec/project-3/tree/1.2)

- **Changelog**
  - Added [404.html](/templates/404.html)
  - Added [500.html](/templates/500.html)
  - Added [error-log.txt](/data/system/error-log.txt) to store errors
- **Fixes**
  - [riddle-g-setting.html](/templates/riddle-g-setting.html) and [riddle-game.html](/templates/riddle-game.html)
  - added statement to prevent users to access other user’s data and games

### [v1.3](https://github.com/MiroslavSvec/project-3/tree/v1.3)

- **Changelog**
  - Redesigned `side-nav` score and added more styles to it
  - Separated JS to different files
  - [riddle-game.html](/templates/riddle-game.html)
    - Added more styles to game itself
    - Added JS validation to answer input field
    - Confirmation buttons are now disabled on click to prevent user to send multiple requests to server
  - [riddle-g-setting.html](/templates/riddle-g-setting.html)
    - Number of tries are hidden if endless mode is selected
    - Added more styles to profile creation form
- **Fixes**
  - Moved alerts to the top as sometimes prevent user to click buttons
  - [riddle-game.html](/templates/riddle-game.html)
    - Delete and Skip buttons where submitting the form
  - [statistics.html](/templates/statistics.html)
    - added sessions to prevent users to view other users’ profiles

### [v1.4](https://github.com/MiroslavSvec/project-3/tree/v1.4)

- **Changelog**
  - Validated each page
    - many CSS errors and warnings due to the Bootstrap 4 bundle. There should be no errors with using CDN, however I kept it as it came with the theme
  - Removed unnecessary files 

### [v1.5](https://github.com/MiroslavSvec/project-3/tree/v1.5)

- **Changelog**
  - Writing `README.md`
  - Moved `helper.py` to separate folder
  - Moved `riddle.py` to separate folder
  - Removed background image from `index.html` for better readbility
- **Fixes**
  - [index.html](/templates/index.html)
  - error 500 passing data but can’t write them when used "USER" and "user"

[**To top**](#Table-of-Contents)

<hr />

## **Deployment**

- [Python 3.6.3](https://www.python.org/downloads/release/python-363/) and [Flask 1.0.2](http://flask.pocoo.org/docs/1.0/) was used to build the application.
  - created [requirements.txt](https://github.com/MiroslavSvec/project-3/blob/master/requirements.txt) that **Heroku** knows which packages are required for the application to run and install them.
  - created [Procfile](https://github.com/MiroslavSvec/project-3/blob/master/Procfile) that **Heroku**  knows what kind of application is this.

- [Heroku](https://www.heroku.com/home)  
*Free cloud hosting platform which simplify the deployment process.*

  - **Settings**
    - Added **Config Vars**
      - IP `0.0.0.0`
      - PORT `5000`
      - SECRET_KEY
    - **Deploy**
      - Connected the app to **GitHub** project
      - Enabled automatic deploys from  master branch
      - Deployed the branch manually
        - **Last Build log**
          - Python app detected
          - Installing requirements with pip
          - Discovering process types
            - Procfile declares types -> web
          - Compressing... 
            - Done: 45.1M
          - Launching...
            - Released v27 https://project-3-riddle-game.herokuapp.com/ deployed to Heroku

[**To top**](#Table-of-Contents)

<hr />

## **How to run the project locally?**

1. Download and install [Python 3](https://www.python.org/downloads/)
2. Clone or download the project  
*Please note that if you downloaded the project manually you must unpack it after*
3. Open your **Command line (CLI)** inside the project root or navigate to it
4. [Create virtual environment (venv)](https://docs.python.org/3/tutorial/venv.html) (optional)
   - Activate venv `source venv/bin/activate` where "venv" is the name of your virtual environment
5. Install required packages via **CLI**
   - `pip install -r requirements.txt`
6. Set **venv** variables
   - IP `0.0.0.0`
   - PORT `5000`
   - SECRET_KEY `my_secret_key`
   - DEVELOPMENT (optional)
7. Run the application
   - `python app.py`
8. The application should now run on your `localhost:5000`

[**To top**](#Table-of-Contents)

<hr />

## **What could be done better?**

- **Error handling**
  - right now minimum to none  
  *At least I should put all the read / write functions to `try` blocks and check if the file exists and / or the application is able to make actions to those files. If not raise a 500 error and give the user appropriate feedback.*
- **Readability of Python code**
  - *As mentioned before many times I am passing functions to function which can make the code hard to read and understand sometimes.*
  - *Instead of the current approach I could assign all the read functions to variables and just pass those variables to a function for better readability. Also with this approach I will not need to reaped myself over and over again as I do now.*
- **Code comments**
  - *Unfortunately not enough comments in both JS and Python and / or the code is commented very badly.*
- **Test the application on different versions of Python**
  - *Unfortunately the application was tested only on **Python 3.6.3***

[**To top**](#Table-of-Contents)

<hr />

## **Credits**

### Special thanks to

- **everyone for finding few minutes to test the project!**

  *All of you gave me constructive feedback which made the project better 😊*

### Questions

- [Mixed](https://github.com/inuits/hubot-scripts/blob/master/riddles.json)
- [General](https://github.com/azeemigi/riddle-server/blob/master/modules/core/src/main/resources/riddles.json)

### [Bootstrap template](https://blackrockdigital.github.io/startbootstrap-sb-admin/index.html)

*As this template suits almost perfectly for my project the overall layout and styles has been kept for [base.html](https://github.com/MiroslavSvec/project-3/blob/master/templates/base.html). I heavily striped the theme down and changed to work with **Flask** and **Jinja2***
- `nav`
  - kept the skeleton only and redesigned it to suits to the project
  - in [**riddle-game.html**](https://github.com/MiroslavSvec/project-3/blob/master/templates/riddle-game.html) added live score for the user
- `footer`
  - kept the skeleton only
- **modals**
  - kept the skeleton only

[**To top**](#Table-of-Contents)