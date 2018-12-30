/*
Profile (index.hmtl) form requests
*/

function create_profile() {
	if (valid_form()) {
		let user_name = $("[name=username]").val();
		$.post(`${user_name}/create_profile`, function (data, status) {
			if (data == user_name.toLowerCase()) {
				let message = "Profile " + `<span class="text-red">${user_name}</span>` + " already exist...<br>Please try to log in instead.";
				alerts_box(message, 10000);
			} else if (data[0].status == status) {
				window.location.replace(`/${user_name}/riddle-g-setting`);
			} else {
				let message = "Sorry. There seems to be a problem ...";
				alerts_box(message, 10000);
			}
		}).fail(function (xhr, status, error) {
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
		$.get(`${user_name}/log_in`, function (data) {
			if (data == "no profile") {
				let message = "Profile " + `<span class="text-red">${user_name}</span>` + " does not exist...<br> Create new profile instead";
				alerts_box(message, 10000);
			} else {
				window.location.replace(`/${user_name}/riddle-g-setting`);
			}
		}).fail(function (xhr, status, error) {
			console.log(xhr);
			console.log(status);
			console.log(error);
		});
		return false;
	}
}	