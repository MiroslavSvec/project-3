
// Render the Game

$(document).ready(function () {
	show_riddle_game();
})


// Riddle Game

function Data(id, data) {
	this.id = id;
	this.data = data;
}

function show_riddle_game() {
	let user = $("#user_name").text();
	let riddle_profile = $("#riddle_profile").text();

	$.get(`/postjson/${user}/${riddle_profile}/riddle-game`, function (data) {
		console.log(data);
		let riddle_game_data = data.game[0];
		if (riddle_game_data.remaining_questions == 0) {
			riddle_score(riddle_game_data);
			riddle_nav(riddle_game_data)
			setTimeout(function () {
				riddle_end();
			}, 10000)
		} else {
			riddle_nav(riddle_game_data)
		}

		console.log(riddle_game_data);
	}).fail(function (xhr, status, error) {
		console.log(xhr);
		console.log(status);
		console.log(error);
	});
	$("#riddle-game").fadeIn(5000);
}

function riddle_game_answer(form) {
	let user = $("#user_name").text();
	let riddle_profile = $("#riddle_profile").text();
	let answer = new Data("answer", form.answer.value);
	console.log(answer);

	$("#alerts").slideDown(500);
	setTimeout(function () {
		$(form).trigger("reset");
	}, 500);

	$.post(
		`/postjson/${user}/${riddle_profile}/riddle-game`,
		JSON.stringify(answer),
		function (data) {
			let riddle_game_data = data.game[0];
			if (riddle_game_data.result == "Correct") {
				if (riddle_game_data.remaining_questions == 0) {
					riddle_score(riddle_game_data);
				} else {
					riddle_messages(
						answer.data,
						"Correct",
						"text-green",
						"Next question?",
						"hide_alerts",
						"Next question"
					);
				}
			} else if (
				riddle_game_data.mods == "limited" &&
				riddle_game_data.tries == 0
			) {
				riddle_score(riddle_game_data);
				setTimeout(function () {
					riddle_end()
				}, 10000)
			} else {
				riddle_messages(
					answer.data,
					"Wrong",
					"text-red",
					"Would you like to try again?",
					"hide_alerts",
					"Try again"
				);
			}
			setTimeout(function () {
				show_riddle_game();
			}, 500);
		}
	).fail(function (xhr, status, error) {
		console.log(xhr);
		console.log(status);
		console.log(error);
	});
	return false;
}

function skip_question() {
	let user = $("#user_name").text();
	let riddle_profile = $("#riddle_profile").text();
	let post_data = new Data("skip_question", "");
	$.post(
		`/postjson/${user}/${riddle_profile}/riddle-game`,
		JSON.stringify(post_data),
		function (data) {
			let riddle_game_data = data.game[0];
			if (riddle_game_data.remaining_questions == 1) {
				confirm_messages(
					"This is the last question <br> therefore you can not skip it!",
					"text-red",
					"Delete the question if you can not find the answer",
					"delete_question",
					"danger",
					"Delete Question?"
				);
			} else {
				show_riddle_game();
				setTimeout(function () {
					$("#alerts").slideUp(500);
				}, 500);
			}
			console.log(riddle_game_data);
		}
	).fail(function (xhr, status, error) {
		console.log(xhr);
		console.log(status);
		console.log(error);
	});
}
function delete_question() {
	let user = $("#user_name").text();
	let riddle_profile = $("#riddle_profile").text();
	let post_data = new Data("delete_question", "");
	$.post(
		`/postjson/${user}/${riddle_profile}/riddle-game`,
		JSON.stringify(post_data),
		function (data) {
			let riddle_game_data = data.game[0];
			console.log(riddle_game_data);
			if (riddle_game_data.remaining_questions == 0) {
				riddle_score(riddle_game_data);
				show_riddle_game();
				return;
			}
			show_riddle_game();
			setTimeout(function () {
				$("#alerts").slideUp(500);
			}, 500);
		}
	).fail(function (xhr, status, error) {
		console.log(xhr);
		console.log(status);
		console.log(error);
	});
}


function riddle_nav(d) {
	$("#question").html(d.question);
	$("#remaining-questions").html(
		"Questions left: " + d.remaining_questions
	);
	$("#right-answers").html(
		"Correct answers: " + d.right_answers
	);
	$("#wrong-answers").html(
		"Wrong answers: " + d.wrong_answers
	);
	$("#skipped-questions").html(
		"Skipped questions: " + d.skipped_questions
	);
	$("#deleted-questions").html(
		"Deleted questions: " + d.deleted_questions
	);
	if (d.tries > 0) {
		$("#tries").html("Tries left: " + d.tries);
	}
}
function riddle_messages(
	answer,
	results,
	css_class,
	message,
	btn_function,
	button_name
) {
	$("#result").html(`
		<div class="card-body">
			<h3>Your answer: ${answer}</h3>
			<h6>is</h6>
			<h3 class="${css_class}">${results}</h3>
			<p class="card-text">${message}</p>
			<button type="submit" onclick="${btn_function}()" class="btn btn-success">${button_name}</button>
			<br>
		</div>`);
	if (results == "Wrong") {
		$("#result .card-body").append(`
			<a onclick="confirm_messages('This question will be', 'text-yellow', 'appended to end of 		all questions', 'skip_question', 'warning','Are you sure?')"
				 class="btn btn-warning">Skip Question</a>
			<a onclick="confirm_messages('This question will be', 'text-red', ' removed from the game', 	'delete_question', 'danger', 'Are you sure?')"
				 class="btn btn-danger">Delete Question</a>`);
	}
}

function confirm_messages(
	first_message,
	css_class,
	action,
	btn_function,
	color,
	last_message
) {
	$("#result").html(`
		<div class="card-body container">
			<h3 class="pt-5">${first_message}</h3>
			<h3 class="py-5 ${css_class}">${action}</h3>
			<div class="row justify-content-center">
				<p class="pb-5 card-text">${last_message}</p>
			</div>
			<div class="row justify-content-around">
				<button type="submit" onclick="${btn_function}()" class="btn btn-success">Yes</button>
				<button type="submit" onclick="hide_alerts()" class="btn btn-${color}">No</button>
			</div>
		</div>`);
	$("#alerts").slideDown(500);
}

/* 
Game Score
*/


function riddle_score(data) {
	let questions_in_total = data.questions_in_total;
	let right_answers = data.right_answers;
	let score = right_answers - data.deleted_questions;
	if (questions_in_total - data.deleted_questions == 0) {
		riddle_end_message("text-red", right_answers, "You deleted all questions :P");
	} else if (score == questions_in_total) {
		riddle_end_message("text-green", score, "You answered correctly every single question which is amazing :)");
	} else if (score > parseInt(questions_in_total / 2)) {
		riddle_end_message("text-green", score, "Which is Great :) ");
	} else if (score == parseInt(questions_in_total / 2)) {
		riddle_end_message("text-yellow", score, "Which is Good :)");
	} else if (score > parseInt(questions_in_total / 2 / 2)) {
		riddle_end_message("text-yellow", score, "Which is So so :P");
	} else {
		riddle_end_message("text-red", score, "Which is Bad :P");
	}
	$("#alerts").slideDown(500);
}

function riddle_end_message(css_class, score, message) {
	$("#result").html(`
		<div class="card-body">
			<h3 class="${css_class}">Congratulation</h3>
			<h6>your score is</h6>
			<h3 class="${css_class}">${score}</h3>
			<p class="card-text ${css_class}">${message}</p>
			<a onclick="riddle_end()" class="btn btn-default"><span class="text-green">Statistics</span></a>
			<br>
		</div>`);
}

/* 
End game and redirect to statistics
*/

function riddle_end() {
	let user = $("#user_name").text();
	window.location.replace(`/${user}/statistics`);
}