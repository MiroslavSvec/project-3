import os
import json
from datetime import datetime
from flask import Flask, redirect, request, render_template, jsonify


""" Helper functions """

def write_to_txt(filename, write_mode, data):
    with open(filename, f"{write_mode}") as file:
        file.writelines(data)


def write_to_json(filename, write_mode, data):
    with open(f'{filename}', f'{write_mode}') as outfile:
   		json.dump(data, outfile)


def read_txt(filename):
	with open(f'{filename}', "r") as file:
		data = file.readlines()
		return data


def read_json(filename):
	with open(f'{filename}', "r") as file:
		data = json.load(file)
		return data


## Questions json for riddle game
def questions(user_name, riddle_profile_name):
	questions = f"data/profiles/{user_name}/riddle_game/{riddle_profile_name}/questions.json"
	return questions


## Profile json
def profile(user_name, riddle_profile_name):
	profile = f"data/profiles/{user_name}/riddle_game/{riddle_profile_name}/player_{riddle_profile_name}.json"
	return profile


def get_profile_data(user_name):
	all_profiles = read_txt('data/profiles/all-profiles.txt')
	for profile in all_profiles:
		if profile.strip('\n') == user_name:
			profile = read_json(f"data/profiles/{user_name}/{user_name}.json")
			return jsonify(profile)


def create_profile_data(user_name):
	profile = get_profile_data(user_name)
	if profile:
		return jsonify(user_name)
	else:
		## Profile data
		profile_created = datetime.now().strftime("%H:%M:%S")
		profiles = {}
		profiles[f'{user_name}'] = []
		profiles[f'{user_name}'].append(
                    {'name': f'{user_name}',
                     'created': f'{profile_created}',
					'finished_riddles': [],
                     })		
		## Write data
		os.makedirs(f"data/profiles/{user_name}")
		write_to_json(f"data/profiles/{user_name}/{user_name}.json", "w", profiles)
		write_to_txt(f"data/profiles/all-profiles.txt",
                    "a", f"{user_name}" + '\n')
		## App data
		app_data = read_json('data/system/app_data.json')
		members_count = app_data['1.1'][0]["members"]
		app_data['1.1'][0]["members"] = members_count + 1
		write_to_json("data/system/app_data.json", "w", app_data)
		## Create game folder
		os.makedirs(f"data/profiles/{user_name}/riddle_game")
		write_to_txt(f"data/profiles/{user_name}/riddle_game/riddle_profiles.txt", "w", "")
		write_to_txt(f"data/profiles/{user_name}/riddle_game/finished_riddles.txt", "w", "")

		return jsonify({'status': "success"}, {'profile': f"{user_name}"})



