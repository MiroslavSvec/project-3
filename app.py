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

@app.route('/<user_name>')
def profile_page(user_name):
	riddle_profiles = helper.read_txt(f'data/profiles/{user_name}/riddle_game/riddle_profiles.txt')
	## Render default template
	return render_template("profile.html",
                        user_name=user_name, riddle_profiles=riddle_profiles, page_title=f"{user_name}" + " profile")


""" Riddles Game  Setting """


@app.route('/<user_name>/riddle-g-setting')
def riddle_setting(user_name):
	riddle_profiles = helper.read_txt(
		f"data/profiles/{user_name}/riddle_game/riddle_profiles.txt")
	return render_template("riddle-g-setting.html",
                        user_name=user_name, riddle_profiles=riddle_profiles, page_title="Riddle Game Setting")
	

## JSON requests to create save

@app.route('/postjson/<user_name>/riddle-g-setting', methods=["POST"])
def parse_setting(user_name):
	# Create new game
	data = request.get_json(force=True)
	riddle.create_riddle_game(data)
	return jsonify(data)


""" Riddles Game """


@app.route('/<user_name>/<riddle_profile>/riddle-game', methods=["GET"])
def get_results(user_name, riddle_profile):
	riddle_profiles = helper.read_txt(
		f"data/profiles/{user_name}/riddle_game/riddle_profiles.txt")
	profile = helper.read_json(helper.profile(user_name, riddle_profile))
	profile = profile["game"][0]
	## Render riddle-game template by default
	return render_template("riddle-game.html",
                        user_name=user_name, 
                        riddle_profiles=riddle_profiles,
                        riddle_profile=riddle_profile,
						page_title="Riddle Game")

## JSON POST to play the game


@app.route('/postjson/<user_name>/<riddle_profile>/riddle-game', methods=["POST", "GET"])
def parse_answer(user_name, riddle_profile):
	## Main POST request for riddle-game
	if request.method == "POST":
		post_data = request.get_json(force=True)
		if post_data["id"] == "answer":
			data = riddle.riddle_game(user_name, riddle_profile, post_data)
			return jsonify(data)
		elif post_data["id"] == "skip_question":
			data = riddle.skip_question(user_name, riddle_profile)
			return jsonify(data)
		else:
			pass
	data = helper.read_json(helper.profile(user_name, riddle_profile))
	return jsonify(data)








if __name__ == '__main__':
    app.run(host=os.getenv('IP'),
            port=os.getenv('PORT'),
            debug=True)

""" Create 404 page and 500 error """
""" Score """
""" Stats """
""" Add confirmation messages when clicking / submiting in the game """
""" Hide skip question button if it is the last question """
""" Come up with some sort of search engine to get more questions injected from web """
""" Limit wrong answers """
""" View Friends """
""" Chat / Password / Send Invitaiton / """
""" Inject graphs to mini statistcs in riddle-game.html """

