var tweenMenuShow
var isHorizontal = false
var testData = [ {
	name : "Jack",
	surname : "smith"
} ]

function populateErrorMessageFields(errorString) {
	Object.keys(JSON.parse(errorString)).forEach(function(key, value) {
		var errorSection = $("<small/>").addClass("text-danger")
		$("<br/>").appendTo(errorSection)
		errorSection.append(JSON.parse(errorString)[key][0].message)
		$("#" + key).parent().find("label").after(errorSection)
		console.log(errorSection)
	})
}

function populateWarningMessageField(fieldId, text) {
	var errorSection = $("<small/>").addClass("text-warning")
	$("<br/>").appendTo(errorSection)
	errorSection.append(text)
	$("#" + fieldId).parent().find("label").after(errorSection)
}

function loadContent(liItem) {
	$("div#page-content").hide()
	var url = ""
		$(".menu-item").removeClass("active")
	$(".background-image").css("background-position",Math.floor(Math.random() * 333)+"px "+Math.floor(Math.random() * 333)+"px")
	$(liItem).addClass("active")
	url = $(liItem).attr("data-href")
	$(".page-content-area-bg").remove()
	$(".page-content-area").remove()
	$("#page-content").load(
			url,
			function(response) {
				var tl = new TimelineLite({
					paused : true,
					ease : Power4.easeOut
				})
				tl.to("#page-content", 1, {
					rotationY : -180,
					transformOrigin : "left"
				}).to("#page-content", 1.2, {
					left : $(".menu-items-holder-left").width(),
					rotationY : 0,
					transformOrigin : "left"
				}, "-= .4")
				$("#page-content").fadeIn()
				$("#page-content").html("")
				$("#page-content").prepend(
						$("<div/>").addClass("page-content-area"))
				$(".page-content-area").html(response)
				$("#page-content").prepend(
						$("<div/>").addClass("page-content-area-bg"))
				tl.play()
				if ($(liItem).attr("data-bg") != null)
					$(".page-content-area-bg").css("background-image",
							$(liItem).attr("data-bg"))
				else
					$(".page-content-area-bg").css("background-image", "none")
			})

	$(".main-logo").load("/static/img/logo.svg")
}

$(document).ready(function() {
	$('img.svg').each(function() {
	    var $img = jQuery(this);
	    var imgID = $img.attr('id');
	    var imgClass = $img.attr('class');
	    var imgURL = $img.attr('src');

	    jQuery.get(imgURL, function(data) {
	        // Get the SVG tag, ignore the rest
	        var $svg = jQuery(data).find('svg');

	        // Add replaced image's ID to the new SVG
	        if(typeof imgID !== 'undefined') {
	            $svg = $svg.attr('id', imgID);
	        }
	        // Add replaced image's classes to the new SVG
	        if(typeof imgClass !== 'undefined') {
	            $svg = $svg.attr('class', imgClass+' replaced-svg');
	        }

	        // Remove any invalid XML tags as per http://validator.w3.org
	        $svg = $svg.removeAttr('xmlns:a');

	        // Replace image with new SVG
	        $img.replaceWith($svg);

// // Add an handler
// jQuery('path').each(function() {
// jQuery(this).click(function() {alert(jQuery(this).attr('id'));});
// });
	    })
	})
	showDialogPage(null,'/account/login/')

})

$(window).on("load", function() {
	TweenLite.to(".full-screen-div", 1, {
		scale : 0,
		transformOrigin : "center"
	})
	$(".menu-item").attr("onclick", "loadContent(this)")
	loadContent($("<li/>").attr({
		"data-href" : "/home/"
	}))
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
			width : "88%",
			height : "88%",
			top : "5.5%",
			left : "5.5%"
		})
		messageBoxTween.reverse()
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
			width : $("#page-content").width(),
			top : 22
		})
		messageBoxTween.play()
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

function openFullScreenDiv(htmlContenet) {
	$(".full-screen-div").html(htmlContenet)
	$(".full-screen-div").css("display", "block")
	$(".full-screen-div").append(
			$("<div/>").addClass("close-button").on("click", function() {
				TweenLite.to(".full-screen-div", 1, {
					scale : 0,
					transformOrigin : "center"
				})
				setTimeout(function() {
					$(".full-screen-div").html("")
				}, 1000)
			}))
	$(this).find(".close-button").load('static/img/icons/close.svg')
	TweenLite.to(".full-screen-div", 1, {
		scale : 1,
		top : 0,
		right : 0,
		left : 0,
		bottom : 0,
		transformOrigin : "center"
	})
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
