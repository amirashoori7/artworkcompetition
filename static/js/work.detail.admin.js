function validateSubmission(reason) {
	switch (reason) {
	case 0:
		if ($("#bioapproved").prop("checked")
				&& $("#workapproved").prop("checked")
				&& $("#qapproved").prop("checked")) {
			var r = confirm("Are you sure that work is approved?");
			if (r == true) {
				$(".status-values").val("4")
				updateTheArtwork()
			} else {
				return
			}
		} else
			toggleMessageBox(
					"Please make sure that the bio, artwork and questions of the entry are correctly submitted",
					true)
		break;
	case 1:
		if ($("#bioapproved").prop("checked")
				&& $("#workapproved").prop("checked")
				&& $("#qapproved").prop("checked")) {
			toggleMessageBox(
					"At least one of the revision reasons must be unchecked",
					true)
			return
		} else {
			var r = confirm("Are you sure that work requires revision?");
			if (r == true) {
				$(".status-values").val("1")
				updateTheArtwork()
			} else {
				return
			}
		}
		break;
	case 2:
		var r = confirm("Are you sure that the artwork is rejected?");
		if (r == true) {
			$(".status-values").val("3")
			updateTheArtwork()
		} else {
			return
		}
		break;
	default:
		alert("Please contact the Technicians")
	}

}

function updateTheArtwork() {
	var form = $('#entry-approval-form')[0];
	var data = new FormData(form);
	$
			.ajax({
				type : "POST",
				enctype : 'multipart/form-data',
				data : data,
				processData : false,
				contentType : false,
				cache : false,
				timeout : 60000,
				url : $("#entry-approval-form").attr("action"),
				beforeSend : function(xhr, settings) {
					function getCookie(name) {
						var cookieValue = null;
						if (document.cookie && document.cookie != '') {
							var cookies = document.cookie.split(';');
							for (var i = 0; i < cookies.length; i++) {
								var cookie = $.trim(cookies[i]);
								if (cookie.substring(0, name.length + 1) == (name + '=')) {
									cookieValue = decodeURIComponent(cookie
											.substring(name.length + 1));
									break;
								}
							}
						}
						return cookieValue;
					}
					if (!(/^http:.*/.test(settings.url) || /^https:.*/
							.test(settings.url))) {
						xhr.setRequestHeader("X-CSRFToken",
								getCookie('csrftoken'));
					}
				},
				success : function(response) {
					if (response.successResult != null) {
						toggleMessageBox(response.successResult, false)
						closeFullScreenDiv()
						$(".menu-item[data-href='/work_lists/']").trigger("click")
					} else if (response.errorResults != null) {
						Object.keys(JSON.parse(response.errorResults)).forEach(
								function(key, value) {
									$('<li/>').text("* " + key).appendTo(
											errorList)
								})
						toggleMessageBox(
								"<span>Unsuccessful."
										+ $('<div>').append(errorList.clone())
												.html(), true)
					}
				},
				error : function(xhr, errmsg, err) {
					console.log(xhr.status + ": " + xhr.responseText)
					toggleMessageBox(xhr.responseText, true)
				},
				complete : function(response) {
					return -1
				}
			})
}

