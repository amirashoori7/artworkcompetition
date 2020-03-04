var questionsValidationCriteria = [ {
	id : "question1",
	title : "Qustion 1",
	min : 50,
	max : 100
}, {
	id : "question2",
	title : "Qustion 2",
	min : 50,
	max : 100
}, {
	id : "question3",
	title : "Qustion 3",
	min : 35,
	max : 100
} ];
function fetchEntryForm(url) {
	$.ajax({
		url : url,
		async : true,
		beforeSend:function(){
			$(".frameLoding").fadeIn()
		},
		success : function(response) {
			$("#artwork-submit-form-holder-id").html(response)
			if ($("#school-id-val").val() == "0") {
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
			$('#buttonSaveContinue, #buttonSubmit').on("click",
					function(event) {
						event.preventDefault()
						checkValidation().done(function() {
							submitEntryForm($('#entry-form-id').attr("action"))
						})
					})
			$("[data-required='1']").change(function() {
				checkValidation().done(function() {
				})
			})
			$("[data-required='1']").keyup(function() {
				checkValidation().done(function() {
				})
			})
			setTimeout(function() {
				checkValidation().done(function() {
				})
			}, 50)
			getSchoolVal(1)
			$('#school-dropdown').selectpicker()
		},
		error : function(request, status, error) {
			console.log(request.responseText);
			$(".frameLoding").fadeOut()
		},complete: function(){
			$(".frameLoding").fadeOut()
		}
	});
}

function gradeChose(radioBTN) {
	$('.btn-outline-secondary.btn-group').removeClass('active');
	$('#currentlearnergrade').val($(radioBTN).val())
}

var totalFields = 0
var filledFields = 0
var questionsValidated = 0;
function checkValidation() {
	totalFields = 0
	filledFields = 0
	var checkValidProcess = $.Deferred();
	$(".exteded-class").removeClass("text-success")
	$(".exteded-class").removeClass("text-warning")
	$(".exteded-class").removeClass("text-danger")
	$("i.exteded-class").removeClass("fa-thumbs-up")
	$("i.exteded-class").removeClass("fa-thumbs-down")
	$("#entry-form-id").find(".card").removeClass("border-danger")
	$("#entry-form-id").find(".card").removeClass("border-warning")
	$("#entry-form-id").find(".card").removeClass("border-success")
	$(".exteded-class").removeClass("exteded-class")
	$("#entry-form-id")
			.find(".card")
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
															.find(".card-title")
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
															.find(".card-title")
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
															.find(".card-title")
															.addClass(
																	"text-warning exteded-class")
												}
											}

										})
					})
	validateQuestions()
	setTimeout(
			function() {
				$("#buttonSubmit").html(
						"<i class='fa fa-save'>&nbsp;&nbsp;&nbsp;</i>Saved "
								+ filledFields + "/" + totalFields)
				if (filledFields == totalFields
						&& questionsValidated == questionsValidationCriteria.length) {
					$("#buttonSubmit").removeClass(
							"btn-outline-secondary disabled")
					$("#buttonSubmit").addClass("btn-success")
					$("#buttonSaveContinue").addClass("disabled")
					$("#buttonSubmit")
							.html(
									"<i class='fa fa-telegram-plane'>&nbsp;&nbsp;&nbsp;</i> Submit The Entry")
				} else {
					$("#buttonSubmit").addClass("disabled")
					$("#buttonSaveContinue").removeClass("disabled")
				}
				checkValidProcess.resolve()
			}, 500)
	return $.when(checkValidProcess).done(function() {
	}).promise()
}

var phoneno = /^\d{10}$/;
function submitRegistryForm(url) {
	var form = $('#registry-form')[0]
	$("#register-btn").prop("disabled", true)
	var data = new FormData(form)
	$
			.ajax({
				type : "POST",
				enctype : 'multipart/form-data',
				data : data,
				processData : false,
				contentType : false,
				cache : false,
				timeout : 60000,
				url : url,
				beforeSend : function(xhr, settings) {
					$(".frameLoding").fadeIn()
					if (!(/^http:.*/.test(settings.url) || /^https:.*/
							.test(settings.url))) {
						xhr.setRequestHeader("X-CSRFToken",
								getCookie('csrftoken'))
					}
				},
				success : function(response) {
					if (response.successResult != null) {
						toggleMessageBox(response.successResult, false)
						$(".form-signin.form-general-style").find(
								"input#inputEmail").val(
								$("#registry-form").find("input#username")
										.val())
						$(".form-signin.form-general-style").find(
								"input#inputPassword").val(
								$("#registry-form").find("input#password1")
										.val())
						$(".form-signin.form-general-style").submit()
						loadContent($("<li/>").attr({
							"data-href" : "/signup_page/"
						}))
						$("#login-div").load('/account/login/')
						$("input[name='req']").remove()
						$(".nav-item menu-item.active").trigger("click")
					} else if (response.errorResults != null) {
						$("#registry-form").find("small").remove()
						$(".tel-no")
								.each(
										function() {
											if ($(this).val().length > 0
													&& !$(this).val().match(
															phoneno))
												populateDangerMessageField($(
														this).attr("id"),
														"The phone number must be 10 digits. i.e. 0123456789")
										})
						populateErrorMessageFields(response.errorResults, true)
					}
				},
				error : function(xhr, errmsg, err) {
					console.log(xhr.status + ": " + xhr.responseText)
					$(".frameLoding").fadeOut()
					toggleMessageBox(xhr.responseText, true)
				},
				complete : function(response) {
					$("#register-btn").prop("disabled", false);
					$(".frameLoding").fadeOut()
					return -1
				}
			})
}

function validateQuestions() {
	questionsValidated = 0
	$(questionsValidationCriteria).each(
			function(i, j) {
				var ctr = $.trim($("#" + j.id).val()).split(" ").length
				if (ctr < j.min || ctr > j.max) {
					$(".word-counter." + j.id).addClass("text-danger")
					if (!$("#" + j.id).hasClass("is-invalid"))
						$("#" + j.id).addClass("is-invalid")
					$(".word-counter." + j.id).addClass("text-success")
					populateDangerMessageField(j.id,
							"Answer in between " + j.min + " and "
									+ j.max + " words")
					$(".questions-card").addClass(
							"border-warning exteded-class")
					$(".questions-card").find(".col-md-1 i").addClass(
							"fa-thumbs-down text-warning exteded-class")
					$(".questions-card").find(".card-title").addClass(
							"text-warning exteded-class")
				} else {
					$(".word-counter." + j.id).removeClass("text-danger")
					$("#" + j.id).removeClass("is-invalid")
					$(".word-counter." + j.id).addClass("text-success")
					questionsValidated++
					$("small." + j.id).remove()
				}
				$(".word-counter." + j.id).html(
						"Word Count (" + ctr + " out of [" + j.min + " - "
								+ j.max + "] words)")
			})
}

function submitEntryForm(url) {
	$("#registry-form").find("small").remove()
	$("input[name='status']").remove()
	if (totalFields == filledFields
			&& questionsValidated == questionsValidationCriteria.length) {
		$('#entry-form-id').append(
				'<input type="hidden" name="status" value="0">')
	}
	var form = $('#entry-form-id')[0]
	console.log("submitEntryForm")
	$("#buttonSubmit, buttonSaveContinue").prop("disabled", true)
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
					$('.progress-bar').html(percentComplete + '%')
				}
			}, false);
			return xhr;
		},
		beforeSend : function(xhr, settings) {
			$(".frameLoding").fadeIn()
			if (!(/^http:.*/.test(settings.url) || /^https:.*/
					.test(settings.url))) {
				xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
			}
		},
		success : function(response) {
			if (response.successResult != null) {
				$(".nav-item menu-item.active").trigger("click")
				toggleMessageBox(response.successResult, false)
				if (totalFields == filledFields)
					$(".nav-item.menu-item.active").trigger("click")
			}
			if (response.errorResults != null)
				populateErrorMessageFields(response.errorResults)
			if (response.errorResults != null) {
				populateErrorMessageFields(response.errorResults)
			}
		},
		error : function(xhr, errmsg, err) {
			$(".frameLoding").fadeOut()
			console.log(xhr.status + ": " + xhr.responseText)
			toggleMessageBox(xhr.responseText, true)
		},
		complete : function(response) {
			$(".frameLoding").fadeOut()
			$("#buttonSubmit, #buttonSaveContinue").prop("disabled", false)
			return false
		}
	})
}