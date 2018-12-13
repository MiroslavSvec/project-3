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

Fix "index out of range" while loading statistics without finished game --- Fixed (removed last index call which was misleading )

### Tools used for testing

Visual Studio Python debuger

Postman

### Changelog

Scraped redirection to login page as I do not think that is good user experiences.
If user enters user name which already exist (as he does not have to know about it)
will use JS to handle the form check and then redirect via Python

### v1.0

<strike>Unfortunately found major bug where 2 users played the game at the same time.  
The files got overwritten and therefore I was forced to implement sessions to separate the users.</strike>

Unfortunately, I discovered the bug while playing with a friend at the same time so I misplaced it as bug related to multiplayer.

Whenever user answered wrongly the game ended `helper.py` line 133. As due to indentation this if stamen was always true on endless mode as the tries were always 0.

- Fixed bug with ending the game when user answer wrongly
- Added session
- Changed view names `get()` and `post()` to `log_in()` and `create_profile()`.
- Added log_out view
- Removed unnecessary files

### v1.1

- Redesigned statistic page base on existing theme for the template.
- Added [statistics.json](/data/riddle-game/statistics.json) for storing all finished games
- Added functionality to sort the profiles in [statistics.json](/data/riddle-game/statistics.json) based on the `correct_answers`
- Redesigned score system  

#### Fixed

- [riddle-g-setting.html](/templates/riddle-g-setting.html)
  - 500 error when user tried to create profile under user name with finished game
- [riddle-game.html](/templates/riddle-game.html)
	- error with double `alerts` id.
- [statistics.html](/templates/statistics.html)
	- game_profile links not showing in `nav`.
	- broken link to game setting in `nav`.