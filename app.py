import os
import json
from datetime import datetime
from random import shuffle
from flask import Flask, session, redirect, url_for, request, render_template, jsonify

# Custom .py
import helper
import riddle

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")


@app.route('/')
def index():
    app_data = helper.read_json('data/system/app_data.json')
    app_data = app_data['1.1'][0]["members"] - 1984
    # Render index.html by default
    return render_template("index.html", members=app_data)


""" Create profile """

@app.route('/<user_name>/create_profile', methods=["POST"])
def create_profile(user_name):
	return helper.create_profile_data(user_name)

""" Log in """


@app.route('/<user_name>/log_in', methods=["GET"])
def log_in(user_name):
    profiles = helper.read_txt("data/profiles/all-profiles.txt")
    profile = user_name + "\n"
    if profile in profiles:
        session['user'] = {'user_name': user_name}
        return jsonify(helper.read_json(f"data/profiles/{user_name}/{user_name}.json"))
    else:
        return jsonify("no profile")

""" Log out """

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect(url_for('index'))

""" Riddles Game  Setting """

# BUG 500 when user trying to create profile with same name as finished profile
@app.route('/<user_name>/riddle-g-setting')
def riddle_setting(user_name):
    riddle_profiles = helper.read_txt(
        f"data/profiles/{user_name}/riddle_game/riddle_profiles.txt")
    return render_template("riddle-g-setting.html",
                           user_name=user_name, riddle_profiles=riddle_profiles, page_title="Riddle Game Setting")


# JSON requests to create save

@app.route('/postjson/<user_name>/riddle-g-setting', methods=["POST"])
def parse_setting(user_name):
    data = request.get_json(force=True)
    profiles = helper.read_txt(
        f"data/profiles/{user_name}/riddle_game/riddle_profiles.txt")
    profile = data["riddle_game_data"]["riddle_profile_name"] + "\n"
    if profile in profiles:
        return jsonify(profile)
    # Create new game
    riddle.create_riddle_game(data)
    return jsonify(data)


""" Riddles Game """


@app.route('/<user_name>/<riddle_profile>/riddle-game', methods=["GET"])
def get_results(user_name, riddle_profile):
    riddle_profiles = helper.read_txt(
        f"data/profiles/{user_name}/riddle_game/riddle_profiles.txt")
    profile = helper.read_json(helper.profile(user_name, riddle_profile))
    profile = profile["game"][0]
    if profile["mods"] == "limited":
        return render_template("riddle-game.html",
                               user_name=user_name,
                               riddle_profiles=riddle_profiles,
                               riddle_profile=riddle_profile,
                               tries=int(profile["tries"]),
                               page_title="Riddle Game")
    # Render riddle-game template by default
    return render_template("riddle-game.html",
                           user_name=user_name,
                           riddle_profiles=riddle_profiles,
                           riddle_profile=riddle_profile,
                           tries=int(0),
                           page_title="Riddle Game")

# JSON POST to play the game


@app.route('/postjson/<user_name>/<riddle_profile>/riddle-game', methods=["POST", "GET"])
def parse_answer(user_name, riddle_profile):
    # Main POST request for riddle-game
    if request.method == "POST":
        post_data = request.get_json(force=True)
        if post_data["id"] == "answer":
            data = riddle.riddle_game(user_name, riddle_profile, post_data)
            return jsonify(data)
        elif post_data["id"] == "skip_question":
            data = riddle.skip_question(user_name, riddle_profile)
            return jsonify(data)
        else:
            data = riddle.delete_question(user_name, riddle_profile)
            return jsonify(data)
    data = helper.read_json(helper.profile(user_name, riddle_profile))
    return jsonify(data)


# Statistics for Ridddle game

@app.route('/<user_name>/statistics', methods=["GET"])
def show_statistics(user_name):
    riddle_profiles = helper.read_txt(
        f"data/profiles/{user_name}/riddle_game/riddle_profiles.txt")
    user_profile = helper.read_json(
        f"data/profiles/{user_name}/{user_name}.json")
    user_profile = user_profile[f"{user_name}"][0]["finished_riddles"]
    finished_games = helper.read_txt(
        f"data/profiles/{user_name}/riddle_game/finished_riddles.txt")
    print(finished_games)
    return render_template("statistics.html",
                           user_name=user_name,
                           user_profile=user_profile,
                           riddle_profiles=riddle_profiles,
                           finished_games=finished_games,
                           page_title="Statistics")


""" App data """


@app.route('/app_data')
def get_app_data():
    app_data = helper.read_json('data/app_data.json')
    return jsonify(app_data)


if __name__ == '__main__':
    app.run(host=os.getenv('IP'),
            port=os.getenv('PORT'),
            debug=True)
""" Need to disable buttons on clicking as rappidly clicks send multiple requests """
""" Create 404 page and 500 error """
""" Stats """
""" Add confirmation messages when clicking / submiting in the game """
""" Hide number of tries when endless mode is selected"""
""" Hide skip question button if it is the last question """
""" Come up with some sort of search engine to get more questions injected from web """
""" Limit wrong answers """
""" View Friends """
""" Chat / Password / Send Invitaiton / """
""" Clear chat history """
""" Inject graphs to mini statistics in riddle-game.html """
