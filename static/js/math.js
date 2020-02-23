var tweenMenuShow
var isHorizontal = false
var testData = [ {
	name : "Jack",
	surname : "smith"
} ]



function populateWarningMessageField(fieldId, text) {
	var errorSection = $("<small/>").addClass("text-warning")
	$("<br/>").appendTo(errorSection)
	errorSection.append(text)
	$("#" + fieldId).parent().find("label").after(errorSection)
}

function populateDangerMessageField(fieldId, text) {
	$("small."+fieldId).remove()
	var errorSection = $("<small/>").addClass("text-danger "+fieldId)
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
	$(".dialog-popup-content").append($("<div/>").addClass("close-button").attr("onclick","closeFullScreenDiv()"))
	TweenLite.to(".full-screen-div", 1, {
		scale : 1,
		top : 0,
		right : 0,
		left : 0,
		bottom : 0,
		transformOrigin : "center"
	})
}

function closeFullScreenDiv(){
	TweenLite.to(".full-screen-div", 1, {
		scale : 0,
		transformOrigin : "center",
		onComplete: function(){
			$(".full-screen-div").html("")
		}
		
	})
}

function loadContent(liItem) {
	$(".navbar-collapse").removeClass("show")
	$("div#page-content").hide()
	$("#banner-bottom-1").fadeIn()
	var url = ""
	$(".menu-item").removeClass("active")
	$(liItem).addClass("active")
	url = $(liItem).attr("data-href")
	$(".page-content-area-bg").remove()
	$(".page-content-area").remove()
	$.ajax({
		url: url,
		cache: false,
		success: function(response) {
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
			$(".page-content-holder").prepend($("<div/>").addClass("page-bg-svg"))
			$(".page-bg-svg").find("span").remove()
			$("#page-content").prepend(
					$("<div/>").addClass("page-content-area"))
			$(".page-content-area").html(response)
			convertImg2SVG("svgNonMenu")
			$("#page-content").prepend(
					$("<div/>").addClass("page-content-area-bg"))
			$(".page-content-area-bg").html($(".menu-item.active").find("a").html())
			$(".banners-background-image").css(
		"background-position",
		Math.floor(Math.random() * 333) + "px "
				+ Math.floor(Math.random() * 333) + "px")
			tl.play()
			if($(liItem).attr("data-color")!=null){
				var color = "var("+$(liItem).attr("data-color")+")";
				$("#banner-top").css("background-color", "var("+$(liItem).attr("data-color")+")")
			}
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

function convertImg2SVG(className){
		$('img.'+className).each(function() {
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

$(window).on("load", function() {
	$(".frameLoding").fadeOut()
	$(".menu-item").attr("onclick", "loadContent(this)")
	$(".menu-item[data-href='/home/']").trigger("click")
	toggleMessageBox(null, null)
})

function dropDownFunction() {
	$("#schoolDropdown").toggleClass("show")
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
var messageBoxTween
function toggleMessageBox(messageText, isError) {
	var tl = new TimelineLite({
		paused : true
	})
	if (messageText == null || messageBoxTween == null) {
		// THE TOGGLE WHILE DOCUMENT LOADING AND WHEN BOX SHOULD BE HIDDEN
		$(".error-message-box").html("")
		$(".success-message-box").html("")
		if (messageBoxTween != null && !messageBoxTween.reversed()) {
			TweenLite.to(".message-box", .3, {
				opacity : 1,
				width : 0,
				top : 22
			})
			messageBoxTween.reverse()
			return
		}
		messageBoxTween = tl.to(".message-box-container", .3, {
			opacity : 1,
			scaleY : 0,
			transfromOrigin : "top"
		})
		messageBoxTween.play()
	} else {
		// SHOWS ERROR MESSAGE
		$(".message-box").fadeIn()
		$(".message-box").html("")
		$(".message-box-container").removeClass("red")
		var height = $(".message-box").height()
		if (isError) {
			$(".error-message-box").html(messageText)
			$(".success-message-box").html("")
			$(".success-message-box").fadeOut()
			$(".message-box-container").addClass("red")
			height = $(".error-message-box").height()
		} else {
			// SHOWS SUCCESS MESSAGE
			$(".error-message-box").html("")
			$(".error-message-box").fadeOut()
			$(".success-message-box").html(messageText)
			height = $(".success-message-box").height()
		}
		TweenLite.to(".message-box", .6, {
			opacity : 1,
			width : "100%",
			top : 22
		})
		messageBoxTween.reverse()
	}
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
	var prov = $("#province-dropdown").val()
	var reg = $("#region-dropdown").val()
	$
	.ajax({
		type : "POST",
		url : "/get_school?reason="+reason+"&prov="+prov+"&reg="+reg,
		beforeSend : function(xhr, settings) {
			if (!(/^http:.*/.test(settings.url) || /^https:.*/
					.test(settings.url))) {
				xhr.setRequestHeader("X-CSRFToken",
						getCookie('csrftoken'));
			}
		},
		success : function(response) {
			if(reason==1) {
				$("#province-dropdown").html("")
				$("#province-dropdown").html('<option value="" selected="selected">Province</option>')
				$("#province-dropdown").removeClass("disabled")
				$(response).each(function(i,j){
					console.log(j)
					if(!$('#province-dropdown option[value="'+j+'"]').length)
						$("#province-dropdown").append($("<option/>").attr("value",j).text(getProvince(""+j+"")))
					
				})
			} else if(reason==2){
				$("#region-dropdown").html('<option value="" selected="selected">Region</option>')
				$("#region-dropdownDIV").fadeIn()
				$("#region-dropdown").removeClass("disabled")
				$(response).each(function(i,j){
					if(!$('#region-dropdown option[value="'+j+'"]').length)
						$("#region-dropdown").append($("<option/>").attr("value",j).text(j))
				})
			}
			else{
				$("#school-dropdown").html('<option value="" selected="selected" value="0" disabled="disabled">School</option>')
				$("#schoolDIV").fadeIn()
				$("#region-dropdownDIV").fadeIn()
				$("#school-dropdown").removeClass("disabled")
				$(response).each(function(i,j){
					console.log(j)
					if(!$('#school-dropdown option[value="'+j[1]+'"]').length)
						$("#school-dropdown").append($("<option/>").attr("value",j[0]).text(j[3]))
				})
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

function getProvince(str){
    switch(str){
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
var countDownDate = new Date("Mar 3, 2020 00:00:00").getTime();
function runTimer(){
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

function submitAForm(url, formId, submitBTNId) {
	var form = $('#'+formId)[0]
	$("#"+submitBTNId).prop("disabled", true)
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
		}, success : function(response) {
			if (response.successResult != null) {
				toggleMessageBox(response.successResult, false)
				$('#admin-console-content').load('/work_lists/')
			} else if (response.errorResults != null) {
				populateErrorMessageFields(response.errorResults)
			} else if (response.errorResult != null)
			toggleMessageBox("<span>"+response.errorResult+"</span>",
					true)
		}, error : function(xhr, errmsg, err) {
			console.log(xhr.status + ": " + xhr.responseText)
			toggleMessageBox(xhr.responseText, true)
		}, complete : function(response) {
			$("#"+submitBTNId).prop("disabled", false)
			return -1
		}
	})
}

function loginForm(url, formId, submitBTNId) {
	var form = $('#'+formId)[0]
	$("#"+submitBTNId).prop("disabled", true)
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
		}, success : function(response) {
			if (response.successResult != null) {
				toggleMessageBox(response.successResult, false)
				$('#'+formId).find("input#id").val(response.id)
			} else if (response.errorResults != null) {
				populateErrorMessageFields(response.errorResults)
			} else if (response.errorResult != null)
			toggleMessageBox("<span>"+response.errorResult+"</span>",
					true)
			else
				$("#login-div").load('/account/login/')
		}, error : function(xhr, errmsg, err) {
			console.log(xhr.status + ": " + xhr.responseText)
			toggleMessageBox(xhr.responseText, true)
		}, complete : function(response) {
			$("#"+submitBTNId).prop("disabled", false)
			return -1
		}
	})
}