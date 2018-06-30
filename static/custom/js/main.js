
// Need to separate it to diferent files

/*
General requests
*/


// Currently logged user name is stored in localStorage
function get_comon_data() {
	const get_comon_data = localStorage.getItem("user_comon_data");
	const comon_data = JSON.parse(get_comon_data);
	// For testing
	console.log(comon_data);
	return comon_data;
}

$(document).ready(function() {
	
})

/*
Profile (index.hmtl) form requests
*/

function create_profile() {
	let user_name = $("[name=username]").val();
	$.post(`${user_name}/data`, function (data, status) {
		console.log(status)
		// Data are sent as str
		// IF the user exist api will return the user name so then
		if (data == user_name) {
			$("#message").html("Profile " + `${data}` + " already exist");
			$("#create_profile_overlay").slideDown(1000);
		// Data are sent as arr
		// IF the user does not exist yet return "succes"
		}else if (data[0].status == status) {
			localStorage.setItem("user_comon_data", JSON.stringify(`${data[1].profile}`));
			window.location.replace(`/user/${data[1].profile}`);
		}else {
			$("#message").html("Sorry.\n There seems to be a problem ...");
			$("#create_profile_overlay").slideDown(1000);
		}
	})
	return false
} 


/*
Create Game (riddle.hmtl) 
*/

function create_riddle_game(form_data) {
	let user = get_comon_data();
	const riddle_game_data = new Game(
		form_data.categories.value,
		form_data.mods.value,
		form_data.tries.value,
		user
	);

	function Game(categories, mods, tries, user) {
		this.id = user;
		this.categories = categories;
		this.mods = mods;
		this.tries = tries;
	}

	$.post(
		`/postjson/${user}/riddle_g_setting`,
		JSON.stringify({ riddle_game_data: riddle_game_data }),
		function(data, status) {
			console.log(status);
			console.log(data);
			window.location.replace(`/user/${user}/riddle-game`);
			
		}
	);
	
	return false;
}

// Riddle Game

function show_riddle_game() {
	let user = get_comon_data();
	$.get(`/postjson/${user}/riddle_g_setting`, function(data) {
		console.log(data);		
		let riddle_game_data = data.game[0];
		$("#question").html("Q: " + riddle_game_data.question);
		$("#right-answers").html("Correct answers: " + riddle_game_data.right_answers);
		$("#wrong-answers").html("Wrong answers: " + riddle_game_data.wrong_answers);
		$("#skipped-questions").html("Skipped questions: " + riddle_game_data.skipped_questions);
		
		console.log(riddle_game_data);

	});
	$("#riddle-game").fadeIn(5000);
}

function riddle_game_answer(form) {
	let user = get_comon_data()
	let answer = form.answer.value
	console.log(answer);
	$.post(
		`/postjson/${user}/riddle-game`,
		JSON.stringify({ answer: answer }),
		function(data) {
			let riddle_game_data = data.game[0];
			if (riddle_game_data.result == "Correct") {
				$("#result").html(riddle_game_data.result);				
			}
			else {
				$("#result").html(riddle_game_data.result);	
			}
			$("#right-answers").html("Correct answers: " + riddle_game_data.right_answers);
			$("#wrong-answers").html("Wrong answers: " + riddle_game_data.wrong_answers);
			$("#skipped-questions").html("Skipped questions: " + riddle_game_data.skipped_questions);
		}
	);
	return false
}

function skip_question() {

	return false;
}

$(document).ready(function () {
	
})