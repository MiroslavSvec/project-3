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