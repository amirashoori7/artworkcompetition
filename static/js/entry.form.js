function fetchEntryForm(url) {
	$.ajax({
		url : url,
		async : true,
		success : function(response) {
			$("#artwork-submit-form-holder-id").html(response)
			if ($("#school-id-val").val() == "0") {
				$("#region-dropdownDIV").fadeOut()
				$("#schoolDIV").fadeOut()
			}

			$.each($("input[name='learnergradeRadio']"), function(i, val) {
				$(
						"input[name='learnergradeRadio'][value='"
								+ $("#currentlearnergrade").val() + "']").prop(
						'checked', true)
				$(
						"input[name='learnergradeRadio'][value='"
								+ $("#currentlearnergrade").val() + "']")
						.parent().addClass("active")
			})
			$('#entry-form-id').submit(function(event) {
				event.preventDefault()
				submitEntryForm($('#entry-form-id').attr("action"))
			})
			$("[data-required='1']").on("focusout", function() {
				checkValidation()
			})
			setTimeout(checkValidation,50)
			getSchoolVal(1)
		},
		error : function(request, status, error) {
			console.log(request.responseText);
		}
	});
}
var totalFields = 0
var filledFields = 0
function checkValidation() {
	var totalFields = 0
	var filledFields = 0
	$(".exteded-class").removeClass("text-success")
	$(".exteded-class").removeClass("text-warning")
	$(".exteded-class").removeClass("text-danger")
	$("i.exteded-class").removeClass("fa-thumbs-up")
	$("i.exteded-class").removeClass("fa-thumbs-down")
	$("#entry-form-id").find(".card").removeClass("border-danger")
	$("#entry-form-id").find(".card").removeClass("border-warning")
	$("#entry-form-id").find(".card").removeClass("border-success")
	$(".exteded-class").removeClass("exteded-class")
	$("#entry-form-id").find(".card")
			.each(
					function(i, j) {
						var sectionTotalFields = $(j).find(
								"[data-required='1']").length
						totalFields += sectionTotalFields
						var sectionFilledFields = 0
						var card = j
						$(card)
								.find("[data-required='1']")
								.each(
										function(k, l) {
											if ($(l).val().length > 0
													&& $(l).val() != 0) {
												filledFields = filledFields + 1
												sectionFilledFields = sectionFilledFields + 1
											}
											if ((k + 1) == sectionTotalFields) {
												if (sectionFilledFields == 0) {
													$(card)
															.addClass(
																	"border-danger exteded-class")
													$(card)
															.find(".col-md-1 i")
															.addClass(
																	"fa-thumbs-down text-danger exteded-class")
													$(card)
															.find("div")
															.addClass(
																	"text-danger exteded-class")
												} else if (sectionFilledFields == sectionTotalFields) {
													$(card).addClass(
															"border-success")
													$(card)
															.find(".col-md-1 i")
															.addClass(
																	"fa-thumbs-up text-success exteded-class")
													$(card)
															.find("div")
															.addClass(
																	"text-success exteded-class")
												} else {
													$(card)
															.addClass(
																	"border-warning exteded-class")
													$(card)
															.find(".col-md-1 i")
															.addClass(
																	"fa-thumbs-down text-warning exteded-class")
													$(card)
															.find("div")
															.addClass(
																	"text-warning exteded-class")
												}
											}

										})
					})
	setTimeout(function() {
		$("#buttonSubmit").html("Saved " + filledFields + "/" + totalFields)
		$("#buttonSubmit").val("Submit " + filledFields + "/" + totalFields)
		if (filledFields == totalFields) {
			$("#buttonSubmit").removeClass("disabled")
			$("#buttonSaveContinue").addClass("disabled")
		} else {
			$("#buttonSubmit").addClass("disabled")
			$("#buttonSaveContinue").removeClass("disabled")
		}
	}, 200)
}

function submitRegistryForm(url) {
	var form = $('#registry-form')[0];
	$("#register-btn").prop("disabled", true);
	var data = new FormData(form);
	$.ajax({
		type : "POST",
		enctype : 'multipart/form-data',
		data : data,
		processData : false,
		contentType : false,
		cache : false,
		timeout : 60000,
		url : url,
		beforeSend : function(xhr, settings) {
			if (!(/^http:.*/.test(settings.url) || /^https:.*/
					.test(settings.url))) {
				xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
			}
		},
		success : function(response) {
			if (response.successResult != null) {
				toggleMessageBox(response.successResult, false)
				$(".form-signin.form-general-style").find("input#inputEmail")
						.val($("#registry-form").find("input#username").val())
				$(".form-signin.form-general-style")
						.find("input#inputPassword").val(
								$("#registry-form").find("input#password1")
										.val())
				$(".form-signin.form-general-style").submit()
				loadContent($("<li/>").attr({
					"data-href" : "/signup_page/"
				}))
				$("#login-div").load('/account/login/')
			} else if (response.errorResult != null) {
				$("#registry-form").find("small").remove()
				populateErrorMessageFields(response.errorResult)
				toggleMessageBox("<span>Registration unsuccessful.</span>",
						true)

			}
		},
		error : function(xhr, errmsg, err) {
			console.log(xhr.status + ": " + xhr.responseText)
			toggleMessageBox(xhr.responseText, true)
		},
		complete : function(response) {
			$("#register-btn").prop("disabled", false);
			return -1
		}
	})
}

function submitEntryForm(url) {
	$("input[name='status']").remove()
	if(totalFields == filledFields){
		$('#entry-form-id').append('<input type="hidden" name="status" value="0">')
	}
	var form = $('#entry-form-id')[0];
	$("#buttonSubmit, buttonSaveContinue").prop("disabled", true);
	var data = new FormData(form);
	$.ajax({
		type : "POST",
		enctype : 'multipart/form-data',
		data : data,
		processData : false,
		contentType : false,
		cache : false,
		url : url,
		xhr : function() {
			var xhr = new window.XMLHttpRequest();
			xhr.upload.addEventListener("progress", function(evt) {
				if (evt.lengthComputable) {
					var percentComplete = ((evt.loaded / evt.total) * 100)
					$('.progress-bar').css('width', percentComplete + '%')
							.attr('aria-valuenow', percentComplete);

				}
			}, false);
			return xhr;
		},
		beforeSend : function(xhr, settings) {
			if (!(/^http:.*/.test(settings.url) || /^https:.*/
					.test(settings.url))) {
				xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
			}

		},
		success : function(response) {
			if (response.successResult != null) {
				$("#id").val(response.id)
				toggleMessageBox(response.successResult, false)
			}
			if (response.errorResultUser != null)
				populateErrorMessageFields(response.errorResultUser)
			if (response.errorResultWork != null) {
				populateErrorMessageFields(response.errorResultWork)
				$("#id").val(0)
			}
		},
		error : function(xhr, errmsg, err) {
			console.log(xhr.status + ": " + xhr.responseText)
			toggleMessageBox(xhr.responseText, true)
		},
		complete : function(response) {
			$("#buttonSubmit, #buttonSaveContinue").prop("disabled", false)
			return -1
		}
	})
}