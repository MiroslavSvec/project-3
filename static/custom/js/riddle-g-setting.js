
$('select[name=mods]').change(function () {
	$('#tries').slideToggle(500);
});


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
			function (data) {
				if (data == riddle_game_data.riddle_profile_name + "\n") {
					alerts_box(
						"Profile " +
						`<span class="text-red">${data}</span>` +
						" already exist or you finished the game under the profile already...<br>Please choose unique game profile name",
						5000
					);
				} else {
					window.location.replace(
						`/${user_name}/${form_data.riddle_profile.value}/riddle-game`
					);
				}
			}
		).fail(function (xhr, status, error) {
			console.log(xhr);
			console.log(status);
			console.log(error);
		});
	}

	return false;
}