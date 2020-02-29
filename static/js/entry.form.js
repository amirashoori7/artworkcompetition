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
			$('#buttonSaveContinue, #buttonSubmit').on("click",
					function(event) {
						event.preventDefault()
						if(window.location.href.indexOf("?req") > 0)
							checkValidation().done(function() {
								submitEntryForm($('#entry-form-id').attr("action"))
							})
						else
							return
					})
			$("[data-required='1']").change(function() {
				checkValidation().done(function() {
				})
			})
			$(".questions").each(function(){
				$(this).on("keyup",function(){
					var ctr = $.trim($(this).val()).split(" ").length
					if(ctr < 50 || ctr > 100){
						$(".word-counter."+$(this).attr("id")).addClass("text-danger")
 						if(!$(this).hasClass("is-invalid"))
 							$(this).addClass("is-invalid")
						$(".word-counter."+$(this).attr("id")).addClass("text-success")
					} else {
						$(".word-counter."+$(this).attr("id")).removeClass("text-danger")
						$(this).removeClass("is-invalid")
						$(".word-counter."+$(this).attr("id")).addClass("text-success")
					}
					$(".word-counter."+$(this).attr("id")).html("Word Count ("+ctr+" out of [50 - 100] words)")
				})
			})
			setTimeout(function() {
				checkValidation().done(function() {
				})
			}, 50)
			getSchoolVal(1)
		},
		error : function(request, status, error) {
			console.log(request.responseText);
		}
	});
}

function gradeChose(radioBTN) {
	$('.btn-outline-secondary.btn-group').removeClass('active');
	$('#currentlearnergrade').val($(radioBTN).val())
}

var totalFields = 0
var filledFields = 0
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
	setTimeout(function() {
		$("#buttonSubmit").html(
				"<i class='fa fa-save'></i>   Saved " + filledFields + "/"
						+ totalFields)
		if (filledFields == totalFields) {
			$("#buttonSubmit").removeClass("disabled")
			$("#buttonSaveContinue").addClass("disabled")
			$("#buttonSubmit").html(
					"<i class='fa fa-telegram-plane'></i> Submit The Entry")
		} else {
			$("#buttonSubmit").addClass("disabled")
			$("#buttonSaveContinue").removeClass("disabled")
		}
		checkValidProcess.resolve()
	}, 200)
	return $.when(checkValidProcess).done(function() {
	}).promise()
}



var phoneno = /^\d{10}$/;
function submitRegistryForm(url) {
	var form = $('#registry-form')[0]
	$("#register-btn").prop("disabled", true)
	var data = new FormData(form)
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
				xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'))
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
				$("input[name='req']").remove()
				$(".nav-item menu-item.active").trigger("click")
			} else if (response.errorResults != null) {
				$("#registry-form").find("small").remove()
				$(".tel-no").each(function(){
					if($(this).val().length > 0 && !$(this).val().match(phoneno))
						populateDangerMessageField($(this).attr("id"),
						"The phone number must be 10 digits. i.e. 0123456789")
				})
				populateErrorMessageFields(response.errorResults, true)
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
	$("#registry-form").find("small").remove()
	$("input[name='status']").remove()
	if (totalFields == filledFields) {
		$('#entry-form-id').append(
				'<input type="hidden" name="status" value="0">')
	}
	if ($.trim($("#question1").val()).length > 0
			&& ($.trim($("#question1").val()).split(" ").length <= 50 ||
					$.trim($("#question1").val()).split(" ").length > 100)) {
		populateDangerMessageField("question1",
				"This field must be between 50 and 100 words")
		return false
	}
	if ($.trim($("#question2").val())
			&& ($.trim($("#question2").val()).split(" ").length <= 50 || 
					$.trim($("#question2").val()).split(" ").length > 100)) {
		populateDangerMessageField("question2",
				"This field must be between 50 and 100 words")
		return false
	}
	if ($.trim($("#question3").val()).length > 0
			&& ($.trim($("#question3").val()).split(" ").length <= 50 || 
					$.trim($("#question3").val()).split(" ").length > 100)) {
		populateDangerMessageField("question3",
				"This field must be between 50 and 100 words")
		return false
	}
	var form = $('#entry-form-id')[0]
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
			console.log(xhr.status + ": " + xhr.responseText)
			toggleMessageBox(xhr.responseText, true)
		},
		complete : function(response) {
			$("#buttonSubmit, #buttonSaveContinue").prop("disabled", false)
			return -1
		}
	})
}