//	  Pending = -1
//    Submitted = 0
//    Requires_Revision = 1
//    Revised_work = 2
//    Rejected_Stage_0 = 3
//    Accepted_Stage_0 = 4
//    Waiting_For_Decision = 5
//    Accepted_Stage_1 = 6
//    Rejected_Stage_1 = 7
//    Waiting_For_Artpost = 8
//    Rejected_Stage_2 = 9
//    Artpost_Recieved = 10
//    Rejected_Stage_3 = 11
//    Winner = 12
function validateSubmission(reason) {
	switch (reason) {
	case 0:
		if ($("#bioapproved").prop("checked")
				&& $("#workapproved").prop("checked")
				&& $("#qapproved").prop("checked")) {
			toggleConfirmationBox(updateTheArtwork,"Are you sure that work is approved?", "4")
		} else
			toggleMessageBox("Please make sure that the learner has been submitted the bio, artwork and questions correctly",
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
			toggleConfirmationBox(updateTheArtwork,"Are you sure that work requires revision?", "1")
		}
		break;
	case 2:
		toggleConfirmationBox(updateTheArtwork,"Are you sure that the artwork is rejected?", "3")
		break;
	default:
		alert("Please contact the Technicians")
	}

}

function updateTheArtwork() {
	$(".status-values").val(arguments[0][2])
	$(".frameLoding").fadeIn()
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
					closeFullScreenDiv()
					if (response.successResult != null) {
						toggleMessageBox(response.successResult, false)
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
					closeFullScreenDiv()
					$(".frameLoding").fadeOut()
				},
				complete : function(response) {
					closeFullScreenDiv()
					$(".frameLoding").fadeOut()
					$('#admin-console-content').load('/work_lists?status=-2')
					return false
				}
			})
}

function flagit(btn, workid){
	flag = 0
	if($(btn).hasClass('btn-outline-warning'))
		flag = 1
	$.ajax({
		type : "POST",
		url : "/flag_work?work_id="+workid+"&flag=" + flag,
		beforeSend : function(xhr, settings) {
			if (!(/^http:.*/.test(settings.url) || /^https:.*/
					.test(settings.url))) {
				xhr.setRequestHeader("X-CSRFToken",
						getCookie('csrftoken'));
			}
			$(".frameLoding").fadeIn()
		},
		success : function(response) {
			console.log(response)
			$(".frameLoding").fadeOut()
			if (response.successResult != null) {
				toggleMessageBox(response.successResult, false)
				if($(btn).hasClass('btn-outline-warning')){
					$(btn).removeClass('btn-outline-warning')
					$(btn).addClass('btn-warning')
				}else{
					$(btn).removeClass('btn-warning')
					$(btn).addClass('btn-outline-warning')
				}
			}  else if (response.errorResult != null)
				toggleMessageBox("<span>" + response.errorResult + "</span>",
						true)
		},
		error : function(xhr, errmsg, err) {
			$(".frameLoding").fadeOut()
			console.log(xhr.status + ": " + xhr.responseText)
			toggleMessageBox(xhr.responseText, true)
		},
		complete : function(response) {
			return -1
		}
	})
}
