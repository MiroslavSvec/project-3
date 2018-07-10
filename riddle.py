# Riddle game

import os
import json
import random
from datetime import datetime
from shutil import copyfile
from flask import Flask, redirect, request, render_template, jsonify

## Custom .py
import helper


app = Flask(__name__)


""" Data Sample """

## {"riddle_game_data":{"id":"test","categories":"all","mods":"none","tries":"1"}}
## {answer: "test answer"}

## {
##	"game": [
##		{
##			"id": "test",
##			"player_name": "test",
##			"game_started": "00:43:17",
##			"categories": "all",
##			"mods": "none",
##			"tries": "1",
##			"result": "",
##			"right_answers": 0,
##			"wrong_answers": 0,
##			"skipped_questions": 0
##		}
##	]
##}



""" Riddles Game Setting"""

def create_riddle_game(data):
    user_name = data["riddle_game_data"]["id"]
    riddle_profile_name = data["riddle_game_data"]["riddle_profile_name"]
    game_profile = create_game_profile(data, user_name, riddle_profile_name)
    questions = create_questions_file(
        game_profile, user_name, riddle_profile_name)
	# Write data
    helper.write_to_txt(f"data/riddle-game/all-players.txt",
                        "a", f"{riddle_profile_name}" + '\n')
    helper.write_to_txt(f"data/profiles/{user_name}/riddle_game/riddle_profiles.txt",
                        "a", f"{riddle_profile_name}" + '\n')
    helper.write_to_json(helper.profile(
        user_name, riddle_profile_name), "w", game_profile)
    helper.write_to_json(helper.questions(
        user_name, riddle_profile_name), "w", questions)
    return jsonify(game_profile)


def create_game_profile(data, user_name, riddle_profile_name):
	# Profile data
    game_created = datetime.now().strftime("%H:%M:%S")
    riddle_game_data = {}
    riddle_game_data["game"] = []
    riddle_game_data["game"].append(
        {'id': f'{user_name}',
         'player_name': f'{riddle_profile_name}',
         'game_started': f'{game_created}',
         'categories': f"{data['riddle_game_data']['categories']}",
         'mods': f"{data['riddle_game_data']['mods']}",
         'tries': f"{data['riddle_game_data']['tries']}",
         'question': [],
         'answer': [],
         'result': "",
         'score': 0,
         'right_answers': 0,
         'wrong_answers': 0,
         'skipped_questions': 0,
         })
	# Create Game folder
    os.makedirs(f"data/profiles/{user_name}/riddle_game/{riddle_profile_name}")
    return riddle_game_data


def create_questions_file(game_profile, user_name, riddle_profile_name):
	# Copy question file to work with fresh file
    if game_profile["game"][0]["categories"] == "all":
        copyfile("data/riddle-game/all.json", helper.questions(user_name, riddle_profile_name))
		
    elif game_profile["game"][0]["categories"] == "general":
        copyfile("data/riddle-game/general.json",
                 helper.questions(user_name, riddle_profile_name))
    else:
        copyfile("data/riddle-game/mixed.json",
                 helper.questions(user_name, riddle_profile_name))

	## To shuffle the questions that every game is different
    questions = helper.read_json(
        helper.questions(user_name, riddle_profile_name))
    random.shuffle(questions["questions"])
	# Pick question from the database
    game_profile["game"][0]["question"] = pick_question(questions)
    return questions


""" Riddle Game """


def pick_question(questions):
	question = questions["questions"][0]["riddle"]	
	return question


def riddle_game(user_name, riddle_profile_name):
	questions = helper.read_json(helper.questions(user_name, riddle_profile_name))
	profile = helper.read_json(helper.profile(user_name, riddle_profile_name))
	data = request.get_json(force=True)
	## Format both user as well as correct answer
	user_answer = string_format(data["answer"])
	correct_answer = string_format(questions["questions"][0]["answer"])
	
	if user_answer == correct_answer:
		profile["game"][0]["right_answers"] += 1
		profile["game"][0]["result"] = "Correct"
		helper.write_to_json(helper.profile(
		    user_name, riddle_profile_name), "w", profile)
		return profile
	else:
		profile["game"][0]["wrong_answers"] += 1
		profile["game"][0]["result"] = "Wrong"
		helper.write_to_json(helper.profile(
		    user_name, riddle_profile_name), "w", profile)
		return profile
	print(correct_answer)
	print(user_answer)
	print(profile)


	return correct_answer


def string_format(string):	
	string = string.lower()
	string = "".join(string.split())
	return string
