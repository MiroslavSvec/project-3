# Riddle Game

Simple Python riddle game

## Credits

### Boostrap template

https://blackrockdigital.github.io/startbootstrap-sb-admin/index.html

### Databases

Mixed

https://github.com/inuits/hubot-scripts/blob/master/riddles.json

General

https://github.com/azeemigi/riddle-server/blob/master/modules/core/src/main/resources/riddles.json


## Bugs and Testing

@app.route('/')
err 500 passing data but can not write them when used "USER" and "user" already exist
another internal err when folder with data missing but user exist in all-users.txt


Need to updata localStorage when swaping between profiles --- LS no longer in use
Need to redirect if riddle game data already exists --- Fixed with if statment on load
Need to add all long links under variables --- Added

Check values of the profile --- Added

Check if profile already exist --- Added

Fix bug when all-profiles.txt exist without data (redirect) --  Fixed with checking if the len(profiles) is > 0

Fix "Wiev all messages" in window button (bad redirecting)

Fix bug with injecting nav links (multiple click add to link) --- Fixed

Fix Chat window working in profile page only --- Fixed

Fix bug with game profiles not showing while playing the game --- Fixed

### Tools used for testing

Visual Studio Python debuger

Postman


## Changelog

Scraped redirection to login page as I do not think that is good user experiences.
If user enters user name wich already exist (as he does not have to know about it)
will use JS to handle the form check and and then redirect via Python

Created rest API for profile data

v 1.0 : Finished general idea for profiles and API
v 1.1 : Added game section (list) to app_data as well as added section in the data for Riddle game.
 Added geme data creation
