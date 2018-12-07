// Need to separate it to diferent files

/*
Alert modal
*/

function alerts_box(message, seconds) {
	$("#message-box").html(message);
	$("#alerts").slideDown(500);

	setTimeout(function() {
		$("#alerts").slideUp(1000);
	}, seconds);
}

function hide_alerts() {
	$("#alerts").slideUp(500);
}

/*
Valid form
*/
function valid_form() {
	let form_values = $("form input");
	for (var i = 0; i < form_values.length; i++) {
		if (form_values[i].value == null || form_values[i].value == "") {
			message = "Please fill all fields ...";
			alerts_box(message, 5000);
			return false;
		}
	}
	return true;
}

/*
Profile (index.hmtl) form requests
*/

function create_profile() {
	if (valid_form()) {
		let user_name = $("[name=username]").val();
		$.post(`${user_name}/create_profile`, function(data, status) {
			if (data == user_name) {
				let message = "Profile " + `<span class="text-red">${data}</span>` + " already exist...<br>Please try to log in instead.";
				alerts_box(message, 10000);
			} else if (data[0].status == status) {
				window.location.replace(`/${user_name}/riddle-g-setting`);
			} else {
				let message = "Sorry. There seems to be a problem ...";
				alerts_box(message, 10000);
			}
		}).fail(function(xhr, status, error) {
			console.log(xhr);
			console.log(status);
			console.log(error);
		});
		return false;
	}
}

function check_login_details() {
	if (valid_form()) {
		let user_name = $("[name=username]").val();
		$.get(`${user_name}/log_in`, function(data) {
			if (data == "no profile") {
				let message = "Profile " + `<span class="text-red">${user_name}</span>` + " does not exist...<br> Create new profile instead";
				alerts_box(message, 10000);
			} else {
				window.location.replace(`/${user_name}/riddle-g-setting`);
			}
		}).fail(function(xhr, status, error) {
			console.log(xhr);
			console.log(status);
			console.log(error);
		});
		return false;
	}
}	



/*
Create Game (riddle.hmtl) 
*/

function create_riddle_game(form_data) {
	let user_name = $("#user_name").text();
	const riddle_game_data = new Game(user_name, form_data);

	function Game(user_name, form_data) {
		this.id = user_name;
		this.riddle_profile_name = form_data.riddle_profile.value;
		this.categories = form_data.categories.value;
		this.mods = form_data.mods.value;
		this.tries = form_data.tries.value;
	}
	console.log(riddle_game_data);
	if (riddle_game_data.mods == "limited" && riddle_game_data.tries == 0) {
		alerts_box(
			"You must selecet how many tries you whish to have with this mode!",
			5000
		);
		return false;
	} else {
		$.post(
			`/postjson/${user_name}/riddle-g-setting`,
			JSON.stringify({ riddle_game_data: riddle_game_data }),
			function(data) {
				if (data == riddle_game_data.riddle_profile_name + "\n") {
					alerts_box(
						"Profile " +
							`<span class="text-red">${data}</span>` +
							" already exist...<br>Please choose unique name",
						5000
					);
				} else {
					window.location.replace(
						`/${user_name}/${form_data.riddle_profile.value}/riddle-game`
					);
				}
			}
		).fail(function(xhr, status, error) {
			console.log(xhr);
			console.log(status);
			console.log(error);
		});
	}

	return false;
}

// Riddle Game

function Data(id, data) {
	this.id = id;
	this.data = data;
}

function show_riddle_game() {
	let user = $("#user_name").text();
	let riddle_profile = $("#riddle_profile").text();

	$.get(`/postjson/${user}/${riddle_profile}/riddle-game`, function(data) {
		console.log(data);
		let riddle_game_data = data.game[0];
		if (riddle_game_data.remaining_questions == 0) {
			riddle_score(riddle_game_data);
			riddle_nav(riddle_game_data)
			setTimeout(function() {
				riddle_end();
			}, 10000)
		} else {
			riddle_nav(riddle_game_data)
		}

		console.log(riddle_game_data);
	}).fail(function(xhr, status, error) {
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
	setTimeout(function() {
		$(form).trigger("reset");
	}, 500);

	$.post(
		`/postjson/${user}/${riddle_profile}/riddle-game`,
		JSON.stringify(answer),
		function(data) {
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
			}else {
				riddle_messages(
					answer.data,
					"Wrong",
					"text-red",
					"Would you like to try again?",
					"hide_alerts",
					"Try again"
				);
			}
			setTimeout(function() {
				show_riddle_game();
			}, 500);
		}
	).fail(function(xhr, status, error) {
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
		function(data) {
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
				setTimeout(function() {
					$("#alerts").slideUp(500);
				}, 500);
			}
			console.log(riddle_game_data);
		}
	).fail(function(xhr, status, error) {
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
		function(data) {
			let riddle_game_data = data.game[0];
			console.log(riddle_game_data);
			if (riddle_game_data.remaining_questions == 0) {
				riddle_score(riddle_game_data);
				show_riddle_game();
				return;
			}
			show_riddle_game();
			setTimeout(function() {
				$("#alerts").slideUp(500);
			}, 500);
		}
	).fail(function(xhr, status, error) {
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
		<div class="card-body">
			<h3>${first_message}</h3>
			<h3 class="${css_class}">${action}</h3>
			<p class="card-text">${last_message}</p>
			<button type="submit" onclick="${btn_function}()" class="btn btn-success">Yes</button>
			<button type="submit" onclick="hide_alerts()" class="btn btn-${color}">No</button>
			<br>
		</div>`);
	$("#alerts").slideDown(500);
}


/* 
Game Score
*/
function riddle_score(data) {
	let questions_in_total = data.questions_in_total - data.deleted_questions;
	let score = data.right_answers;
	if (questions_in_total == 0) {
		riddle_end_message("text-red", score, "Very Bad :P");
	} else if (score == questions_in_total) {
		riddle_end_message("text-green", score, "Amazing :)");
	} else if (score > questions_in_total / 2) {
		riddle_end_message("text-green", score, "Great :) ");
	} else if (score == questions_in_total / 2) {
		riddle_end_message("text-yellow", score, "Good :)");
	} else if (score > questions_in_total / 2 / 2) {
		riddle_end_message("text-yellow", score, "So so :P");
	} else {
		riddle_end_message("text-red", score, "Bad :P");
	}
	$("#alerts").slideDown(500);
}

function riddle_end_message(css_class, score, message) {
	$("#result").html(`
		<div class="card-body">
			<h3 class="${css_class}">Congratulation</h3>
			<h6>your score is</h6>
			<h3 class="${css_class}">${score}</h3>
			<p class="card-text">Which is <span class="${css_class}">${message}</span></p>
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

