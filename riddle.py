# Riddle game

import os
import json
import random
from datetime import datetime
from shutil import copyfile
from flask import jsonify
# Custom .py
import helper


# Questions json for riddle game
def questions(user_name, riddle_profile_name):
    questions = f"data/profiles/{user_name}/riddle_game/{riddle_profile_name}/questions.json"
    return questions


# Profile json
def profile(user_name, riddle_profile_name):
    profile = f"data/profiles/{user_name}/riddle_game/{riddle_profile_name}/player_{riddle_profile_name}.json"
    return profile


""" Riddles Game Setting"""

def create_riddle_game(data):
    user_name = data["riddle_game_data"]["id"]
    riddle_profile_name = data["riddle_game_data"]["riddle_profile_name"]
    game_profile = create_game_profile(data, user_name, riddle_profile_name)
    questions = create_questions_file(
        game_profile, user_name, riddle_profile_name)
    game_profile["game"][0]["questions_in_total"] = len(
        questions["questions"])
    game_profile["game"][0]["remaining_questions"] = game_profile["game"][0]["questions_in_total"]
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
         'tries_in_total': int(f"{data['riddle_game_data']['tries']}"),
         'tries': int(f"{data['riddle_game_data']['tries']}"),
         'question': [],
         'answer': [],
         'result': "",
         'score': 0,
         'questions_in_total': 0,
         'remaining_questions': 0,
         'right_answers': 0,
         'wrong_answers': 0,
         'skipped_questions': 0,
         'deleted_questions': 0,
         })
    # Create Game folder
    os.makedirs(f"data/profiles/{user_name}/riddle_game/{riddle_profile_name}")
    return riddle_game_data


def create_questions_file(game_profile, user_name, riddle_profile_name):
    # Copy question file to work with fresh file
    if game_profile["game"][0]["categories"] == "all":
        copyfile("data/riddle-game/all.json",
                 helper.questions(user_name, riddle_profile_name))

    elif game_profile["game"][0]["categories"] == "general":
        copyfile("data/riddle-game/general.json",
                 helper.questions(user_name, riddle_profile_name))
    else:
        copyfile("data/riddle-game/mixed.json",
                 helper.questions(user_name, riddle_profile_name))

        # To shuffle the questions that every game is different
    questions = helper.read_json(helper.questions(user_name, riddle_profile_name))
    random.shuffle(questions["questions"])
    # Pick question from the database
    game_profile["game"][0]["question"] = pick_question(questions)
    return questions


""" Riddle Game """


def pick_question(questions):
    question = questions["questions"][0]["riddle"]
    return question


def riddle_game(user_name, riddle_profile_name, data):
    questions = helper.read_json(
        helper.questions(user_name, riddle_profile_name))
    profile = helper.read_json(helper.profile(user_name, riddle_profile_name))

    # Format both user as well as correct answer
    user_answer = string_format(data["data"])
    correct_answer = string_format(questions["questions"][0]["answer"])

    if user_answer == correct_answer:
        profile["game"][0]["right_answers"] += 1
        profile["game"][0]["remaining_questions"] -= 1
        profile["game"][0]["result"] = "Correct"
        questions["questions"].pop(0)
        if len(questions["questions"]) > 0:
            profile["game"][0]["question"] = pick_question(questions)
        else:
            profile = end_game(user_name, riddle_profile_name, profile)
        helper.write_to_json(helper.questions(
            user_name, riddle_profile_name), "w", questions)
        helper.write_to_json(helper.profile(
            user_name, riddle_profile_name), "w", profile)
        return profile
    else:
        profile["game"][0]["result"] = "Wrong"
        profile["game"][0]["wrong_answers"] += 1
        if profile["game"][0]["tries"] > 0 and profile["game"][0]["mods"] == "limited":
            profile["game"][0]["tries"] -= 1
            if profile["game"][0]["tries"] == 0:
                profile = end_game(user_name, riddle_profile_name, profile)

        helper.write_to_json(helper.profile(
            user_name, riddle_profile_name), "w", profile)
        return profile


def skip_question(user_name, riddle_profile_name):
    questions = helper.read_json(
        helper.questions(user_name, riddle_profile_name))
    profile = helper.read_json(
        helper.profile(user_name, riddle_profile_name))
    if len(questions["questions"]) == 1:
        return profile
    skipped_question = questions["questions"].pop(0)
    questions["questions"].append(skipped_question)

    profile["game"][0]["question"] = pick_question(questions)
    profile["game"][0]["skipped_questions"] += 1
    helper.write_to_json(helper.profile(
        user_name, riddle_profile_name), "w", profile)
    helper.write_to_json(helper.questions(
        user_name, riddle_profile_name), "w", questions)
    return profile


def delete_question(user_name, riddle_profile_name):
    questions = helper.read_json(
        helper.questions(user_name, riddle_profile_name))
    profile = helper.read_json(helper.profile(user_name, riddle_profile_name))
    profile["game"][0]["deleted_questions"] += 1
    questions["questions"].pop(0)
    profile["game"][0]["remaining_questions"] = len(questions["questions"])

    if len(questions["questions"]) > 0:
        profile["game"][0]["question"] = pick_question(questions)
    else:
        profile = end_game(user_name, riddle_profile_name, profile)

    helper.write_to_json(helper.profile(
            user_name, riddle_profile_name), "w", profile)
    helper.write_to_json(helper.questions(
        user_name, riddle_profile_name), "w", questions)
    return profile


def end_game(user_name, riddle_profile_name, profile):
    user_profile = helper.read_json(f"data/profiles/{user_name}/{user_name}.json")
	# Delete remaining questions first
    profile["game"][0]["question"] = ""
	# Save data to user profile
    user_profile[f"{user_name}"][0]["finished_riddles"].append(
        profile["game"][0])
    helper.write_to_json(
        f"data/profiles/{user_name}/{user_name}.json", "w", user_profile)
    new_profiles = []
    profiles = helper.read_txt(
        f"data/profiles/{user_name}/riddle_game/riddle_profiles.txt")
    riddle_profile_name = riddle_profile_name + "\n"
    for riddle_profile in profiles:
        if riddle_profile_name == riddle_profile:
            helper.write_to_txt(
                f"data/profiles/{user_name}/riddle_game/finished_riddles.txt", "a", riddle_profile_name)
        else:
            new_profiles.append(riddle_profile)
    if len(new_profiles) == 0:
        helper.write_to_txt(
            f"data/profiles/{user_name}/riddle_game/riddle_profiles.txt", "w", "")
    else:
        helper.write_to_txt(
            f"data/profiles/{user_name}/riddle_game/riddle_profiles.txt", "w", new_profiles)
	# Append finished game to statistics
    statistics = helper.read_json("data/riddle-game/statistics.json")
    statistics['profiles'].append(profile["game"][0])
    helper.write_to_json("data/riddle-game/statistics.json", "w", statistics)
    return profile


def string_format(string):
    string = string.lower()
    string = "".join(string.split())
    return string
