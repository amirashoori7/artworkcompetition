var tweenMenuShow
var isHorizontal = false
var provinces = ["EC", "FS", "GT", "KZN", "LP", "MP", "NW", "NC", "WC"]

function populateWarningMessageField(fieldId, text) {
	var errorSection = $("<small/>").addClass("text-warning")
	$("<br/>").appendTo(errorSection)
	errorSection.append(text)
	$("#" + fieldId).parent().find("label").after(errorSection)
}

function populateDangerMessageField(fieldId, text) {
	$("small." + fieldId).remove()
	var errorSection = $("<small/>").addClass("text-danger " + fieldId)
	$("<br/>").appendTo(errorSection)
	errorSection.append(text)
	$("#" + fieldId).before(errorSection)
}

// FOR MANY FIELDS
function populateErrorMessageFields(errorString) {
	Object.keys(JSON.parse(errorString)).forEach(function(key, value) {
		var errorSection = $("<small/>").addClass("text-danger")
		$("<br/>").appendTo(errorSection)
		errorSection.append(JSON.parse(errorString)[key][0].message)
		$("#" + key).after(errorSection)
	})
}

function openFullScreenDiv(htmlContenet) {
	$(".full-screen-div").html(htmlContenet)
	$(".full-screen-div").css("display", "block")
	$(this).find(".close-button").load('static/img/icons/close.svg')
	$(".dialog-popup-content").append(
			$("<div/>").addClass("close-button").attr("onclick",
					"closeFullScreenDiv()"))
	TweenLite.to(".full-screen-div", .333, {
		scale : 1,
		top : 0,
		right : 0,
		left : 0,
		bottom : 0,
		transformOrigin : "center"
	})
}

function closeFullScreenDiv() {
	TweenLite.to(".full-screen-div", .333, {
		scale : 0,
		transformOrigin : "center",
		onComplete : function() {
			$(".full-screen-div").html("")
		}

	})
}

function loadContent(liItem) {
	$(".navbar-collapse").removeClass("show")
	$("div#page-content").hide()
	$("#banner-bottom-1").fadeIn()
	$(".frameLoding").fadeIn()
	var url = ""
	$(".menu-item").removeClass("active")
	$(liItem).addClass("active")
	url = $(liItem).attr("data-href")
	$(".page-content-area-bg").remove()
	$(".page-content-area").remove()
	$.ajax({
		url : url,
		cache : false,
		success : function(response) {
			var tl = new TimelineLite({
				paused : true,
				ease : Power4.easeOut
			})
			tl.to("#page-content", 1, {
				opacity : 0
			}).to("#page-content", 1.2, {
				opacity : 1
			}, "-= .4")
			$("#page-content").fadeIn()
			$("#page-content").html("")
			$(".page-content-holder").prepend(
					$("<div/>").addClass("page-bg-svg"))
			$(".page-bg-svg").find("span").remove()
			$("#page-content").prepend(
					$("<div/>").addClass("page-content-area"))
			$(".page-content-area").html(response)
			convertImg2SVG("svgNonMenu")
			$("#page-content").prepend(
					$("<div/>").addClass("page-content-area-bg"))
			$(".page-content-area-bg").html(
					$(".menu-item.active").find("a").html())
			$(".banners-background-image").css(
					"background-position",
					Math.floor(Math.random() * 333) + "px "
							+ Math.floor(Math.random() * 333) + "px")
			tl.play()
			if ($(liItem).attr("data-color") != null) {
				var color = "var(" + $(liItem).attr("data-color") + ")";
				$("#banner-top").css("background-color",
						"var(" + $(liItem).attr("data-color") + ")")
			}
			$(".frameLoding").fadeOut()
		}
	})
}

$(document).ready(function() {
	runTimer()
	convertImg2SVG("svg")
	$("#login-div").load('/account/login/')
	TweenLite.to(".full-screen-div", 1, {
		scale : 0,
		transformOrigin : "center"
	})

})

function convertImg2SVG(className) {
	$('img.' + className).each(function() {
		var $img = jQuery(this);
		var imgID = $img.attr('id');
		var imgClass = $img.attr('class');
		var imgURL = $img.attr('src');

		jQuery.get(imgURL, function(data) {
			var $svg = jQuery(data).find('svg');
			if (typeof imgID !== 'undefined') {
				$svg = $svg.attr('id', imgID);
			}
			if (typeof imgClass !== 'undefined') {
				$svg = $svg.attr('class', imgClass + ' replaced-svg');
			}
			$svg = $svg.removeAttr('xmlns:a');
			$img.replaceWith($svg);
		})
	})
}


function filterFunction() {
	var input, filter, a, i;
	input = $(".school-input")
	filter = input.val().toUpperCase()
	div = $("#schoolDropdown")
	a = div.find("a")
	for (i = 0; i < a.length; i++) {
		txtValue = a[i].textContent || a[i].innerText
		if (txtValue.toUpperCase().indexOf(filter) > -1) {
			a[i].style.display = ""
		} else {
			a[i].style.display = "none"
		}
	}
}

// SHOWS/HIDES THE MESSAGE BOX,
// INPUT: 1- gets a text message and boolean (True pops the error message. False
// pops the success message)
function toggleMessageBox(messageText, isError) {
	if (isError) {
		$(".error-message-content").html(messageText)
		$("#error-message-modal").modal("show")
	} else {
		$(".success-message-content").html(messageText)
		$("#success-message-modal").modal("show")
	}
}

function toggleConfirmationBox(callback) {
	$(".confirmation-message-content").html(arguments[1])
	$("#confirmation-box-modal").modal("show")
	var args = [].slice.call(arguments)
	$("#confirmation-box-btn").on("click",function(){
		callback(args)
		$("#confirmation-box-modal").modal("hide")
	})
}

function showDialogPage(element, url) {
	$("<div/>").load(
			url,
			function(response) {
				openFullScreenDiv("<div class='dialog-popup-content'>"
						+ response + "</div>")
			})
	return -1
}

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

function getSchoolVal(reason) {
	if (reason == 1) {
						$("#province-dropdown").html("")
						$("#province-dropdown")
								.html('<option value="" selected="selected">Province</option>')
						$("#province-dropdown").removeClass("disabled")
						$(provinces).each(
								function(i, j) {
									if (!$('#province-dropdown option[value="'
											+ j + '"]').length)
										$("#province-dropdown").append(
												$("<option/>").attr("value", j)
														.text(
																getProvince(""
																		+ j
																		+ "")))
																		if(i+1==j.length && $("#province-id-val").val().length>0)
																			{$("#province-dropdown").val($("#province-id-val").val())
																				$("#province-dropdown").selectpicker("refresh")}

								})
						$("#school-dropdown").removeClass("disabled")
								return
					} else {
						$("#schoolDIV").fadeIn()
						$(".bs-searchbox").find("input[type='text']").keyup(function(){
							if($(this).val().length > 2){
								$("small.school-dropdown").remove()
								$("#school-dropdown").html("")
								$("#school-dropdown").selectpicker("refresh")
								filterSchool($(this).val())
							} else {
								populateDangerMessageField("school-dropdown","Please type at least 3 charachters")
								$("#school-dropdown").html("")
								$("#school-dropdown").selectpicker("refresh")
							}
						})
					}
}
function filterSchool(schoolTXT){
	var prov = $("#province-dropdown").val()
	$.ajax({
				type : "POST",
				url : "/get_school?reason=2&prov=" + prov
						+ "&schooltxt=" + schoolTXT,
				beforeSend : function(xhr, settings) {
					if (!(/^http:.*/.test(settings.url) || /^https:.*/
							.test(settings.url))) {
						xhr.setRequestHeader("X-CSRFToken",
								getCookie('csrftoken'));
					}
				},
				success : function(response) {
						$(response).each(
								function(i, j) {
									$("#school-dropdown").append(
											$("<option/>").attr("value",j[0]).text(
													j[3]).attr("onclick","selectSchool(this)"))
								})
								$("#school-dropdown").selectpicker("refresh")
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

function selectSchool(schoolAnchor){
	$("small.school-dropdown").remove()
	$("#school-dropdown").val($(schoolAnchor).val())
	$("#school-id-val").val($(schoolAnchor).val())
	$("#school-dropdown").selectpicker("refresh")
	checkValidation().done(function() {
				})
}

function getProvince(str) {
	switch (str) {
	case "EC":
		return "Eastern Cape"
	case "FS":
		return "Free State"
	case "GT":
		return "Gauteng"
	case "KZN":
		return "KwaZulu Natal"
	case "LP":
		return "Limpopo"
	case "MP":
		return "Mpumalanga"
	case "NW":
		return "North West"
	case "NC":
		return "Northern Cape"
	case "WC":
		return "Western Cape"
	}
}
var countDownDate = new Date("Apr 30, 2020 17:00:00").getTime();
function runTimer() {
	var x = setInterval(function() {
		var now = new Date().getTime();
		var distance = countDownDate - now;
		var days = Math.floor(distance / (1000 * 60 * 60 * 24));
		var hours = Math.floor((distance % (1000 * 60 * 60 * 24))
				/ (1000 * 60 * 60));
		var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
		var seconds = Math.floor((distance % (1000 * 60)) / 1000);
		$('[data-text="days"]').html($("<span/>").text(days))
		$('[data-text="hrs"]').html($("<span/>").text(hours))
		$('[data-text="mins"]').html($("<span/>").text(minutes))
		$('[data-text="sec"]').html($("<span/>").text(seconds))
		if (distance < 0) {
			clearInterval(x);
		}
	}, 1000);
}

function showItemMenu(e) {
	e.preventDefault()
	loadContent($("<li/>").attr("data-href", "/signup_page/"))
}

function submitAnEvaluationForm() {
	var url = arguments[0][2], formId = arguments[0][3], submitBTNId = arguments[0][4], newStatus = arguments[0][5]
	if (newStatus != null)
		$('#' + formId).find('#statusfield').val(newStatus)
	var form = $('#' + formId)[0]
	$("#" + submitBTNId).prop("disabled", true)
	var data = new FormData(form)
	$.ajax({
		type : "POST",
		data : data,
		processData : false,
		contentType : false,
		cache : false,
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
				$('#admin-console-content').load('/work_lists?status=-2')
				closeFullScreenDiv()
			} else if (response.errorResults != null) {
				populateErrorMessageFields(response.errorResults)
			} else if (response.errorResult != null)
				toggleMessageBox("<span>" + response.errorResult + "</span>",
						true)
		},
		error : function(xhr, errmsg, err) {
			console.log(xhr.status + ": " + xhr.responseText)
			toggleMessageBox(xhr.responseText, true)
		},
		complete : function(response) {
			$("#" + submitBTNId).prop("disabled", false)
			return -1
		}
	})
}

function loginForm(url, formId, submitBTNId) {
	var form = $('#' + formId)[0]
	$("#" + submitBTNId).prop("disabled", true)
	var data = new FormData(form)
	$.ajax({
		type : "POST",
		data : data,
		processData : false,
		contentType : false,
		cache : false,
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
			} else if (response.errorResults != null) {
				populateErrorMessageFields(response.errorResults)
			} else if (response.errorResult != null)
				toggleMessageBox("<span>" + response.errorResult + "</span>",
						true)
			else {
				$("#login-div").load('/account/login/')
			}
		},
		error : function(xhr, errmsg, err) {
			console.log(xhr.status + ": " + xhr.responseText)
			toggleMessageBox(xhr.responseText, true)
		},
		complete : function(response) {
			$("#" + submitBTNId).prop("disabled", false)
			return -1
		}
	})
}

var alphaNumeric = /^[0-9a-zA-Z]+$/;
function forgotMyPSW(url, formId, submitBTNId) {
	var form = $('#' + formId)[0]
	if($("#inputPassword2").val() != $("#inputPassword1").val()){
		toggleMessageBox("The password doesn't match the repeat.", true)
		return
	}
	if($("#inputPassword2").val().length < 8){
		toggleMessageBox("The password should be at least 8 charachters.", true)
		return
	}
	if(!$("#inputPassword2").val().match(alphaNumeric)){
		toggleMessageBox("The password should include both digits and text.", true)
		return
	}
	$("#" + submitBTNId).prop("disabled", true)
	var data = new FormData(form)
	$.ajax({
		type : "POST",
		data : data,
		processData : false,
		contentType : false,
		cache : false,
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
				$('#' + formId).find("input#id").val(response.id)
			} else if (response.errorResults != null) {
				populateErrorMessageFields(response.errorResults)
			} else if (response.errorResult != null)
				toggleMessageBox("<span>" + response.errorResult + "</span>",
						true)
			else {
				$("#login-div").load('/account/login/')
			}
		},
		error : function(xhr, errmsg, err) {
			console.log(xhr.status + ": " + xhr.responseText)
			toggleMessageBox(xhr.responseText, true)
		},
		complete : function(response) {
			$("#" + submitBTNId).prop("disabled", false)
			return -1
		}
	})
}

function showForgotPsw(){
	$('.forgot-psw').load('/account/reset_password')
	$(".forgot-psw").show()
	$(".login-ul").hide()
}
function hideForgotPsw(){
	$(".forgot-psw").hide()
	$(".login-ul").show()
}