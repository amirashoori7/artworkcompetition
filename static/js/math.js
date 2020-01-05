var tweenMenuShow
function windowLayoutFitSize() {
	$("#main-body").width($(window).width())
	$("#main-body").height($(window).height())
	var frameHeight = ($(window).height() * .95)
	var isHorizontal = true
	var frameWidth = frameHeight + (frameHeight * 13 / 21)
	$(".page-content").width(frameWidth)
	$(".page-content").height(frameHeight)
	if ($(window).width() < $(window).height()) {
		isHorizontal = false
	}
}

function loadContent(liItem) {
	$("div.page-content").hide()
	var url = ""
	$(".menu-item").removeClass("active")
	$(liItem).addClass("active")
	$("#login-div").load('/account/login/')
	url = $(liItem).attr("data-href")
	var tl = new TimelineLite({paused: true,ease: Power4.easeOut})
	tl.to(".page-content, .page-content-area", 1, { 
		rotationY: -180, 
		top: "5%",
		transformOrigin: "left" })
	.to(".page-content, .page-content-area", 1.3, { 
		left: $(".menu-items-holder").width() - 11,
		rotationY: 0,
		transformOrigin: "left"
	}, "-= .6")
	$(".page-content-area-bg").remove()
	$(".page-content-area").remove()
	$(".page-content").load(url, function () {
		$(".page-content").fadeIn()	
		$(".page-content").prepend($("<div/>").addClass("page-content-area"))
//		$(".page-content-area").html()
		$(".page-content").prepend($("<div/>").addClass("page-content-area-bg"))
		tl.play()
	})
}

$(window).bind('resize', function () {
	windowLayoutFitSize()
})

$(document).ready(function () {
	windowLayoutFitSize()
// loadUniverseBG()
	$(".return-button").load("static/img/icons/close.svg")
})


$(window).on("load", function () {
	$(".menu-item").attr("onclick", "loadContent(this)")
	loadContent($("<li/>").attr("data-href", "/dashindex"))
	toggleMessageBox(null, null)
})


function loadUniverseBG() {
	window.requestAnimationFrame = window.requestAnimationFrame || window.mozRequestAnimationFrame ||
		window.webkitRequestAnimationFrame || window.msRequestAnimationFrame

	var starDensity = .216,
	speedCoeff = .05,
	width,
	height,
	starCount,
	circleRadius,
	circleCenter,
	first = true,
	cometColor = '180,184,240',
	giantColor = '160,134,240',
	starColor = '170,114,240',
	canva = document.getElementById('universe'),
	stars = [];

	windowResizeHandler()
	window.addEventListener('resize', windowResizeHandler, false)

	createUniverse()

	function createUniverse() {
		universe = canva.getContext('2d')

		for (var i = 0; i < starCount; i++) {
			stars[i] = new Star()
			stars[i].reset()
		}

		draw()
	}

	function draw() {
		universe.clearRect(0, 0, width, height)

		var starsLength = stars.length

		for (var i = 0; i < starsLength; i++) {
			var star = stars[i]
			star.move()
			star.fadeIn()
			star.fadeOut()
			star.draw()
		}

		window.requestAnimationFrame(draw)
	}

	function Star() {

		this.reset = function () {
			this.giant = getProbability(3)
			this.comet = this.giant || first ? false : getProbability(10)
			this.x = getRandInterval(0, width - 10)
			this.y = getRandInterval(0, height)
			this.r = getRandInterval(1.1, 2.6)
			this.dx = getRandInterval(speedCoeff, 6 * speedCoeff) + (this.comet + 1 - 1) * speedCoeff * getRandInterval(50, 120) + speedCoeff * 2
			this.dy = -getRandInterval(speedCoeff, 6 * speedCoeff) - (this.comet + 1 - 1) * speedCoeff * getRandInterval(50, 120)
			this.fadingOut = null
			this.fadingIn = true
			this.opacity = 0
			this.opacityTresh = getRandInterval(.4, 1 - (this.comet + 1 - 1))
			this.do = getRandInterval(0.0005, 0.002) + (this.comet + 1 - 1) * .001
		}

		this.fadeIn = function () {
			if (this.fadingIn) {
				this.fadingIn = this.opacity > this.opacityTresh ? false : true
				this.opacity += this.do
			}
		}

		this.fadeOut = function () {
			if (this.fadingOut) {
				this.fadingOut = this.opacity < 0 ? false : true;
				this.opacity -= this.do / 2
				if (this.x > width || this.y < 0) {
					this.fadingOut = false
					this.reset()
				}
			}
		}

		this.draw = function () {
			universe.beginPath()

			if (this.giant) {
				universe.fillStyle = 'rgba(' + giantColor + ',' + this.opacity + ')'
				universe.arc(this.x, this.y, 2, 0, 2 * Math.PI, false)
			} else if (this.comet) {
				universe.fillStyle = 'rgba(' + cometColor + ',' + this.opacity + ')'
				universe.arc(this.x, this.y, 1.5, 0, 2 * Math.PI, false)

				// comet tail
				for (var i = 0; i < 30; i++) {
					universe.fillStyle = 'rgba(' + cometColor + ',' + (this.opacity - (this.opacity / 20) * i) + ')'
					universe.rect(this.x - this.dx / 4 * i, this.y - this.dy / 4 * i - 2, 2, 2)
					universe.fill()
				}
			} else {
				universe.fillStyle = 'rgba(' + starColor + ',' + this.opacity + ')'
				universe.rect(this.x, this.y, this.r, this.r)
			}

			universe.closePath()
			universe.fill()
		}

		this.move = function () {
			this.x += this.dx
			this.y += this.dy
			if (this.fadingOut === false) {
				this.reset()
			}
			if (this.x > width - (width / 4) || this.y < 0) {
				this.fadingOut = true
			}
		}

			setTimeout(function () {
				first = false
			}, 50)
	}

	function getProbability(percents) {
		return ((Math.floor(Math.random() * 1000) + 1) < percents * 10)
	}

	function getRandInterval(min, max) {
		return (Math.random() * (max - min) + min)
	}

	function windowResizeHandler() {
		width = window.innerWidth
		height = window.innerHeight
		starCount = width * starDensity
		circleRadius = (width > height ? height / 2 : width / 2)
		circleCenter = {
			x: width / 2,
			y: height / 2
		}

		canva.setAttribute('width', width)
		canva.setAttribute('height', height)
	}
}

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
	var tl = new TimelineLite({paused: true})
	if(messageText == null || messageBoxTween==null) {
		// THE TOGGLE WHILE DOCUMENT LOADING AND WHEN BOX SHOULD BE HIDDEN
		$(".error-message-box").html("")
		$(".success-message-box").html("")
		if(messageBoxTween != null && !messageBoxTween.reversed()){
			TweenLite.to(".message-box", .3, {
				opacity: 1,
				width: 0,
				top: 22
			})
			messageBoxTween.reverse()
			return
		}
		messageBoxTween = tl.to(".message-box-container", .3, {
			opacity: 1, 
			width: "88%", 
			height: "88%",
			top: "5.5%",
			left: "5.5%"
		})
		messageBoxTween.reverse()
	} else {
		// SHOWS ERROR MESSAGE
		$(".message-box").fadeIn()
		$(".message-box").html("")
		$(".message-box-container").removeClass("red")
		var height = $(".message-box").height()
		if(isError){
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
			opacity: 1,
			width: $(".page-content").width(),
			top: 22
		})
		messageBoxTween.play()
	}
}

function showDialogPage(element, url){
	$(".dialog-popup-content").remove()
	$(".page-content").append($("<div/>").addClass("dialog-popup-content"))
	TweenLite.from(".dialog-popup-content", 1, {width: "0", height: "0", transformOrigin: "left", defaultEase: Power4.easeOut})
	$(".dialog-popup-content").load(url, function(){
		$(this).append($("<div/>").addClass("close-button").on("click",function(){
			$(".dialog-popup-content").fadeOut()
		}))
		$(this).find(".close-button").load('static/img/icons/close.svg')
	})
	return -1
}
