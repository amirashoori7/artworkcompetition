var tweenMenuShow
function windowLayoutFitSize() {
	$("#main-body").width($(window).width())
	$("#main-body").height($(window).height())
	var frameHeight = ($(window).height() * .95)
	var isHorizontal = true;
	var frameWidth = frameHeight + (frameHeight * 13 / 21)
	$(".page-content").width(frameWidth)
	$(".page-content").height(frameHeight)
	if ($(window).width() < $(window).height()) {
		isHorizontal = false;
	}
}

function loadContent(liItem) {
	$("div.page-content").hide()
	var url = ""
	url = $(liItem).attr("data-href")
	$("div.page-content").load(url, function () {
		tweenMenuShow.reverse()
		$("div.page-content").fadeIn()
		TweenMax.fromTo(".page-content", 1, { scaleY: 0, scaleX: 0, rotation: -180 },
			{ 
			scaleY: 1, 
			scaleX: 1,
			rotation: 0,
			left: ($(window).width() - $(".page-content").width()) / 2,
			top: ($(window).height() - $(".page-content").height()) / 2 + "px",
			transformOrigin: "center"
		})
			
	})
}

$(window).bind('resize', function () {
	windowLayoutFitSize()
});

$(document).ready(function () {
	$(".menu-icon").load("static/img/icons/menu.svg", function () {
		var tlMenu = new TimelineLite({
			paused: true
		})
		tweenMenuShow = tlMenu.from(".menu-items-holder", .5, {
			top: "-100%",
			transformOrigin: "top"
		})
		tweenMenuShow.reverse()
		$(this).on("click", function () {
			if (tweenMenuShow.reversed())
				tweenMenuShow.play()
			else
				tweenMenuShow.reverse()
		})
	})
	windowLayoutFitSize()
	loadUniverseBG()
	$(".return-button").load("static/img/icons/close.svg")
})


$(window).on("load", function () {
	$(".menu-item").attr("onclick", "loadContent(this)")
	// loadBackgroundAnimParticles()
	toggleMessageBox(null, null)
})


function loadUniverseBG() {
	window.requestAnimationFrame = window.requestAnimationFrame || window.mozRequestAnimationFrame ||
		window.webkitRequestAnimationFrame || window.msRequestAnimationFrame;

	var starDensity = .216;
	var speedCoeff = .05;
	var width;
	var height;
	var starCount;
	var circleRadius;
	var circleCenter;
	var first = true;
	var cometColor = '180,184,240';
	var giantColor = '160,134,240';
	var starColor = '170,114,240';
	var canva = document.getElementById('universe');
	var stars = [];

	windowResizeHandler();
	window.addEventListener('resize', windowResizeHandler, false);

	createUniverse();

	function createUniverse() {
		universe = canva.getContext('2d');

		for (var i = 0; i < starCount; i++) {
			stars[i] = new Star();
			stars[i].reset();
		}

		draw();
	}

	function draw() {
		universe.clearRect(0, 0, width, height);

		var starsLength = stars.length;

		for (var i = 0; i < starsLength; i++) {
			var star = stars[i];
			star.move();
			star.fadeIn();
			star.fadeOut();
			star.draw();
		}

		window.requestAnimationFrame(draw);
	}

	function Star() {

		this.reset = function () {
			this.giant = getProbability(3);
			this.comet = this.giant || first ? false : getProbability(10);
			this.x = getRandInterval(0, width - 10);
			this.y = getRandInterval(0, height);
			this.r = getRandInterval(1.1, 2.6);
			this.dx = getRandInterval(speedCoeff, 6 * speedCoeff) + (this.comet + 1 - 1) * speedCoeff * getRandInterval(50, 120) + speedCoeff * 2;
			this.dy = -getRandInterval(speedCoeff, 6 * speedCoeff) - (this.comet + 1 - 1) * speedCoeff * getRandInterval(50, 120);
			this.fadingOut = null;
			this.fadingIn = true;
			this.opacity = 0;
			this.opacityTresh = getRandInterval(.2, 1 - (this.comet + 1 - 1) * .8);
			this.do = getRandInterval(0.0005, 0.002) + (this.comet + 1 - 1) * .001;
		};

		this.fadeIn = function () {
			if (this.fadingIn) {
				this.fadingIn = this.opacity > this.opacityTresh ? false : true;
				this.opacity += this.do;
			}
		};

		this.fadeOut = function () {
			if (this.fadingOut) {
				this.fadingOut = this.2 < 0 ? false : true;
				this.opacity -= this.do / 2;
				if (this.x > width || this.y < 0) {
					this.fadingOut = false;
					this.reset();
				}
			}
		};

		this.draw = function () {
			universe.beginPath();

			if (this.giant) {
				universe.fillStyle = 'rgba(' + giantColor + ',' + this.opacity + ')';
				universe.arc(this.x, this.y, 2, 0, 2 * Math.PI, false);
			} else if (this.comet) {
				universe.fillStyle = 'rgba(' + cometColor + ',' + this.opacity + ')';
				universe.arc(this.x, this.y, 1.5, 0, 2 * Math.PI, false);

				// comet tail
				for (var i = 0; i < 30; i++) {
					universe.fillStyle = 'rgba(' + cometColor + ',' + (this.opacity - (this.opacity / 20) * i) + ')';
					universe.rect(this.x - this.dx / 4 * i, this.y - this.dy / 4 * i - 2, 2, 2);
					universe.fill();
				}
			} else {
				universe.fillStyle = 'rgba(' + starColor + ',' + this.opacity + ')';
				universe.rect(this.x, this.y, this.r, this.r);
			}

			universe.closePath();
			universe.fill();
		};

		this.move = function () {
			this.x += this.dx;
			this.y += this.dy;
			if (this.fadingOut === false) {
				this.reset();
			}
			if (this.x > width - (width / 4) || this.y < 0) {
				this.fadingOut = true;
			}
		};

		(function () {
			setTimeout(function () {
				first = false;
			}, 50)
		})()
	}

	function getProbability(percents) {
		return ((Math.floor(Math.random() * 1000) + 1) < percents * 10);
	}

	function getRandInterval(min, max) {
		return (Math.random() * (max - min) + min);
	}

	function windowResizeHandler() {
		width = window.innerWidth;
		height = window.innerHeight;
		starCount = width * starDensity;
		circleRadius = (width > height ? height / 2 : width / 2);
		circleCenter = {
			x: width / 2,
			y: height / 2
		}

		canva.setAttribute('width', width);
		canva.setAttribute('height', height);
	}
}

function dropDownFunction() {
  $("#schoolDropdown").toggleClass("show");
}

function filterFunction() {
  var input, filter, a, i;
  input = $(".school-input");
  filter = input.val().toUpperCase();
  div = $("#schoolDropdown")
  a = div.find("a");
  for (i = 0; i < a.length; i++) {
    txtValue = a[i].textContent || a[i].innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      a[i].style.display = ""
    } else {
      a[i].style.display = "none"
    }
  }
}


//SHOWS/HIDES THE MESSAGE BOX, 
// INPUT: 1- gets a text message and boolean (True pops the error message. False pops the success message)
var messageBoxTween;
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
				top: 0
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
		$(".message-box-container").removeClass("red")
		if(isError){
			$(".error-message-box").html(messageText)
			$(".success-message-box").html("")
			$(".success-message-box").fadeOut()
			$(".message-box-container").addClass("red")
		} else {
		// SHOWS SUCCESS MESSAGE
			$(".error-message-box").html("")
			$(".error-message-box").fadeOut()
			$(".success-message-box").html(messageText)
		}
		TweenLite.to(".message-box", .6, {
			opacity: 1,
			width: $(".page-content").width(),
			top: parseInt($(".page-content").css("top")) + (($(".message-box").height()) / 2)
		})
		messageBoxTween.play()
	}
}
