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

## **Table of Contents**

- [***UX***](#UX)
  - [General Design](#General-Design)
  - [Requirements](#Requirements)
  - [Wireframes](#Wireframes)
  - [Template](#Template)
- [***Features***](#Features)
  - [Existing features](#Existing-features)
  - [Features left to implement](#Features-left-to-implement)
- [***Credits***](#Credits)

<hr />

## **UX**

### **General Design**

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

### **Requirements**

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

### **Wireframes**

Base on the above I created basic mock-up using [Balsamiq](https://balsamiq.com/) which can be find [here](https://github.com/MiroslavSvec/project-3/blob/master/assets/mockup.pdf). 

### **Template**

As this was my first Python project I decided to fully focus on Python and Flask. Therefore I wanted to speed up the development and try to find a template/s which I could use for this project.

At the end I was able to find [this](https://blackrockdigital.github.io/startbootstrap-sb-admin/index.html) template which suits my project almost perfectly. I choose the above template mainly because of the `side-nav` and the chat window in main `nav`.

Also with the above template and friends list I wanted to create a small social page with more minigames then just the Riddle game.  
This is why the game profile list starts with "Games" instead of "Riddles".

*Please read the [***Credits***](#Credits) section to see what I kept and changed.*

[**To top**](#Table-of-Contents)

<hr />

## **Features**

### **Existing features**

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

### **Features left to implement**

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
  - The overall score which is displayed at the end of the game has no actual effect in the "Statistics" page. The table is sorted by most answered questions which can be misleading as the overall score can be different. This should be changed and let the app to sort the game profiles based on the score. However, this will require some work:
  - send another request to server via JS to update the user profile score at the end of the game
  - let Python to calculate and update the profile score at the end and just send the final figure back to front end (better approach)
- **Database**
  - allow users to delete profiles
    - I gave this functionality less importance as there is not too many questions and / or mods varieties.
  - delete profile after the game finish
    - profile data are no longer used after the game finish, so they should be removed from the server


[**To top**](#Table-of-Contents)

<hr />

## **Bugs and Testing**

@app.route('/')
err 500 passing data but can’t write them when used "USER" and "user" already exist
another internal err when folder with data missing but user exist in all-users.txt

Need to update localStorage when swapping between profiles --- LS no longer in use
Need to redirect if riddle game data already exists --- Fixed with if statement on load
Need to add all long links under variables --- Added

Check values of the profile --- Added

Check if profile already exist --- Added

Fix bug when all-profiles.txt exist without data (redirect) -- Fixed with checking if the len(profiles) is > 0

Fix "View all messages" in window button (bad redirecting)

Fix bug with injecting nav links (multiple click adds to link) --- Fixed

Fix Chat window working in profile page only --- Fixed

Fix bug with game profiles not showing while playing the game --- Fixed

Fix "index out of range" while loading statistics without finished game --- Fixed (removed last index call which was misleading)

### Tools used for testing

Visual Studio Python debugger

Postman

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

<hr />

## **Changelog**

Scraped redirection to login page as I do not think that is good user experiences.
If user enters user name which already exist (as he does not have to know about it)
will use JS to handle the form check and then redirect via Python

### v1.0

<strike>Unfortunately found major bug where 2 users played the game at the same time.  
The files got overwritten and therefore I was forced to implement sessions to separate the users. </strike>

Unfortunately, I discovered the bug while playing with a friend at the same time, so I misplaced it as bug related to multiplayer.

Whenever user answered wrongly the game ended `helper.py` line 133. As due to indentation this if statement was always true on endless mode as the tries were always 0.

- Fixed bug with ending the game when user answer wrongly
- Added session
- Changed view names `get()` and `post()` to `log_in()` and `create_profile()`.
- Added logout view
- Removed unnecessary files

### v1.1

- Redesigned statistic page base on existing theme for the template.
- Added [statistics.json](/data/riddle-game/statistics.json) for storing all finished games
- Added functionality to sort the profiles in [statistics.json](/data/riddle-game/statistics.json) based on the `correct_answers`
- Redesigned score system  

#### Fixes in v1.1

- [riddle-g-setting.html](/templates/riddle-g-setting.html)
  - 500 error when user tried to create profile under user name with finished game
- [riddle-game.html](/templates/riddle-game.html)
  - error with double `alerts` id.
- [statistics.html](/templates/statistics.html)
  - game profile links not showing in `nav`.
  - broken link to game setting in `nav`.

### v1.2

- Added [404.html](/templates/404.html)
- Added [500.html](/templates/500.html)
- Added [error-log.txt](/data/system/error-log.txt) to store errors

#### Fixes in v1.2

- [riddle-g-setting.html](/templates/riddle-g-setting.html) and [riddle-game.html](/templates/riddle-game.html)
  - added statement to prevent users to access other user’s data and games

### v1.3

- Redesigned `side-nav` score and added more styles to it
- Separated JS to different files
- [riddle-game.html](/templates/riddle-game.html)
  - Added more styles to game itself
  - Added JS validation to answer input field
  - Confirmation buttons are now disabled on click to prevent user to send multiple requests to server
- [riddle-g-setting.html](/templates/riddle-g-setting.html)
  - Number of tries are hidden if endless mode is selected
  - Added more styles to profile creation form

#### Fixes in v1.3

- Moved alerts to the top as sometimes prevent user to click buttons
- [riddle-game.html](/templates/riddle-game.html)
  - Delete and Skip buttons where submitting the form
- [statistics.html](/templates/statistics.html)
  - added sessions to prevent users to view other users’ profiles

### v1.4

- Validated each page
  - many CSS errors and warnings due to the Bootstrap 4 bundle. There should be no errors with using cdn, however I kept it as it came with the theme
- Removed unnecessary files

### v1.5

- Writing `README.md`
- Moved `helper.py` to separate folder
- Moved `riddle.py` to separate folder

<hr />

## **Credits**

### Bootstrap template

https://blackrockdigital.github.io/startbootstrap-sb-admin/index.html

### Databases

Mixed

https://github.com/inuits/hubot-scripts/blob/master/riddles.json

General

https://github.com/azeemigi/riddle-server/blob/master/modules/core/src/main/resources/riddles.json


