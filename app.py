import os
import json
from datetime import datetime
from random import shuffle 
from flask import Flask, redirect, request, render_template, jsonify

## Custom .py
import helper
import riddle

app = Flask(__name__)


""" Data Sample """

## {"test": [{"name": "test", "login": "true", "created": "00:40:13"}]}

""" Rest API """


@app.route('/<user_name>/data', methods=["GET"])
def get(user_name):
	profiles = helper.read_txt("data/profiles/all-profiles.txt")
	profile = user_name + "\n"
	print(profile, user_name)
	if profile in profiles:
		return jsonify(helper.read_json(f"data/profiles/{user_name}/{user_name}.json"))
	else:
		return jsonify("no profile")
	


@app.route('/<user_name>/data', methods=["POST"])
def post(user_name):
	return helper.create_profile_data(user_name)
		
@app.route('/app_data')
def get_app_data():
	app_data = helper.read_json('data/app_data.json')
	return jsonify(app_data)

	



""" Create profile page """


@app.route('/')
def index():
	app_data = helper.read_json('data/system/app_data.json')
	app_data = app_data['1.1'][0]["members"] - 1984
	## Render index.html by default
	return render_template("index.html", members=app_data)



""" Chat in separate page """

@app.route('/chat')
def chat():
	return render_template("chat.html")

""" Profile page """

@app.route('/user/<user_name>')
def profile_page(user_name):
	## Get profile data
	profiles_data = helper.read_txt("data/profiles/all-profiles.txt")
	## Check if there is more then one profile
	if len(profiles_data) > 0:
		return render_template("profile.html",
                         user_name=user_name, page_title=f"{user_name}" + " profile", profiles=profiles_data)
	## Render default template
	return render_template("profile.html",
                        user_name=user_name, page_title=f"{user_name}" + " profile")


""" Riddles Game  Setting """
@app.route('/<user_name>/riddle-g-setting')
def riddle_setting(user_name):
	return riddle.riddle_g_setting(user_name)
	

## JSON requests to create save
@app.route('/postjson/<user_name>/riddle_g_setting', methods=["POST", "GET"])
def parse_setting(user_name):
	# Create new game
	if request.method == "POST":
		data = request.get_json(force=True)
		riddle.create_riddle_game(data)
		return jsonify(data)
	data = helper.read_json(helper.profile(user_name))
	return jsonify(data)
	

""" Riddles Game """

@app.route('/user/<user_name>/riddle-game', methods=["GET"])
def get_results(user_name):
	## Render riddle-game template by default
	return render_template("riddle-game.html",
                        user_name=user_name, page_title="Riddle Game")

## JSON POST to play the game
@app.route('/postjson/<user_name>/riddle-game', methods=["POST", "GET"])
def parse_answer(user_name):
	## Main POST request for riddle-game
	if request.method == "POST":
		data = riddle.riddle_game(user_name)		
		return jsonify(data)
	data = helper.read_json(helper.profile(user_name))
	return jsonify(data)








if __name__ == '__main__':
    app.run(host=os.getenv('IP'),
            port=os.getenv('PORT'),
            debug=True)

""" Create 404 page and 500 error """
""" Create members page """
""" Categories for questions """
""" Score """
""" Come up with some sort of search engine to get more questions injected from web """
""" Limit wrong answers """
""" Add multiple saves """
""" Add riddle """
""" Passwords """
""" View Friends """
""" Chat / Password / Send Invitaiton / """
""" Inject graphs to mini statistcs in riddle-game.html """

