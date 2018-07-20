// Need to separate it to diferent files

/*
General requests
*/

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

/*
Buttons
*/

function fade(element) {
	$(element).fadeOut(1500);
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
		$.post(`${user_name}/data`, function(data, status) {
			if (data == user_name) {
				let message =
					"Profile " +
					`${data}` +
					" already exist Please try to log in instead.";
				alerts_box(message, 10000);
			} else if (data[0].status == status) {
				localStorage.setItem("user_comon_data", JSON.stringify(user_name));
				window.location.replace(`/${user_name}`);
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
		$.get(`${user_name}/data`, function(data) {
			if (data == "no profile") {
				let message =
					"Profile " +
					`${user_name}` +
					" does not exist. Create new profile instead";
				alerts_box(message, 10000);
			} else {
				localStorage.setItem("user_comon_data", JSON.stringify(user_name));
				window.location.replace(`/${user_name}`);
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
	$.post(
		`/postjson/${user_name}/riddle-g-setting`,
		JSON.stringify({ riddle_game_data: riddle_game_data }),
		function(data, status) {
			console.log(status);
			console.log(data);
			window.location.replace(
				`/${user_name}/${form_data.riddle_profile.value}/riddle-game`
			);
		}
	).fail(function(xhr, status, error) {
		console.log(xhr);
		console.log(status);
		console.log(error);
	});

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
		$("#question").html(riddle_game_data.question);
		$("#remaining-questions").html(
			"Questions left: " + riddle_game_data.remaining_questions
		);
		$("#right-answers").html(
			"Correct answers: " + riddle_game_data.right_answers
		);
		$("#wrong-answers").html(
			"Wrong answers: " + riddle_game_data.wrong_answers
		);
		$("#skipped-questions").html(
			"Skipped questions: " + riddle_game_data.skipped_questions
		);
		$("#deleted-questions").html(
			"Deleted questions: " + riddle_game_data.deleted_questions
		);

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
				riddle_messages(
					answer.data,
					"Correct",
					"text-green",
					"Next question?",
					"hide_alerts",
					"Next question"
				);
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

function hide_alerts() {
	$("#alerts").slideUp(500);
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
			console.log(riddle_game_data);
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
				console.log("Yes")
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
/*
Templates
*/
function confirm_messages(css_class, action, btn_function, color) {
	$("#result").html(`
		<div class="card-body">
			<h3 class="card-title">The question will be</h3>
			<h3 class="${css_class}">${action} all questions</h3>
			<p class="card-text">Are you sure?</p>
			<button type="submit" onclick="${btn_function}()" class="btn btn-success">Yes</button>
			<button type="submit" onclick="hide_alerts()" class="btn btn-${color}">No</button>
			<br>
		</div>`);
	$("#alerts").slideDown(500);
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
			<h3 class="card-title">Your answer: ${answer}</h3>
			<h6>is</h6>
			<h3 class="${css_class}">${results}</h3>
			<p class="card-text">${message}</p>
			<button type="submit" onclick="${btn_function}()" class="btn btn-success">${button_name}</button>
			<br>
		</div>`);
	if (results == "Wrong") {
		$("#result .card-body").append(`
			<a onclick="confirm_messages('text-yellow', 'appended to end of ', 'skip_question', 'warning')" class="btn btn-warning">Skip Question</a>
			<a onclick="confirm_messages('text-red', ' removed from ', 'delete_question', 'danger')" class="btn btn-danger">Delete Question</a>`);
	}
}
function riddle_end() {
	$("#result").html(`
		<div class="card-body">
			<h3 class="text-green">Congratulation</h3>
			<h6>your score is</h6>
			<h3>${results}</h3>
			
			<button type="submit" onclick="${btn_function}()" class="btn btn-success">${button_name}</button>
			<br>
		</div>`);
}
