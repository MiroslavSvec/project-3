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
    app_data = app_data['1.4'][0]["members"]
    # Render index.html by default
    return render_template("index.html", members=app_data, page_title="Riddle Game")


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


@app.route('/<user_name>/riddle-g-setting')
def riddle_setting(user_name):
    if 'user' in session:
        if user_name == session['user']['user_name']:
            riddle_profiles = helper.read_txt(
                f"data/profiles/{user_name}/riddle_game/riddle_profiles.txt")
        else:
            return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))
    return render_template("riddle-g-setting.html",
                           user_name=user_name, riddle_profiles=riddle_profiles, page_title="Riddle Game Setting")


# JSON requests to create save

@app.route('/postjson/<user_name>/riddle-g-setting', methods=["POST"])
def parse_setting(user_name):
    data = request.get_json(force=True)
    profiles = helper.read_txt(
        f"data/profiles/{user_name}/riddle_game/riddle_profiles.txt")
    profile = data["riddle_game_data"]["riddle_profile_name"] + "\n"
    finished_games = helper.read_txt(
        f"data/profiles/{user_name}/riddle_game/finished_riddles.txt")
    if profile in profiles or profile in finished_games:
        return jsonify(profile)
    # Create new game
    riddle.create_riddle_game(data)
    return jsonify(data)


""" Riddles Game """


@app.route('/<user_name>/<riddle_profile>/riddle-game', methods=["GET"])
def get_results(user_name, riddle_profile):
    if 'user' in session:
        if user_name == session['user']['user_name']:
            riddle_profiles = helper.read_txt(
                f"data/profiles/{user_name}/riddle_game/riddle_profiles.txt")
            profile = helper.read_json(
                helper.profile(user_name, riddle_profile))
            profile = profile["game"][0]
            if profile["mods"] == "limited":
                return render_template("riddle-game.html",
                                       user_name=user_name,
                                       riddle_profiles=riddle_profiles,
                                       riddle_profile=riddle_profile,
                                       tries=int(profile["tries"]),
                                       page_title="Riddle Game")
            else:
                # Render riddle-game template by default
                return render_template("riddle-game.html",
                                       user_name=user_name,
                                       riddle_profiles=riddle_profiles,
                                       riddle_profile=riddle_profile,
                                       tries=int(0),
                                       page_title="Riddle Game")
    return redirect(url_for('index'))

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
    if 'user' in session:
        if user_name == session['user']['user_name']:
            user_profile = helper.read_json(
                f"data/profiles/{user_name}/{user_name}.json")
            finished_games = user_profile[f"{user_name}"][0]["finished_riddles"]
            riddle_profiles = helper.read_txt(
                f"data/profiles/{user_name}/riddle_game/riddle_profiles.txt")
            statistics = helper.read_json("data/riddle-game/statistics.json")
            statistics = sorted(statistics['profiles'],
                                key=lambda k: k['right_answers'], reverse=True)
            return render_template("statistics.html",
                                   finished_games=finished_games,
                                   riddle_profiles=riddle_profiles,
                                   user_name=user_name,
                                   statistics=statistics[:10],
                                   page_title="Statistics")
    return redirect(url_for('index'))


""" Errors """

# 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# 500


@app.errorhandler(500)
def internal_server_error(e):
    helper.write_to_txt("data/system/error-log.txt", "a", f"{e}" + '\n')
    return render_template('500.html'), 500

""" App data """


@app.route('/app_data')
def get_app_data():
    app_data = helper.read_json('data/app_data.json')
    return jsonify(app_data)


if __name__ == '__main__':
    app.run(host=os.getenv('IP'),
            port=os.getenv('PORT'),
            debug=os.environ.get("DEVELOPMENT"))