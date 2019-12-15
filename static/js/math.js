var tweenMenuShow
function windowLayoutFitSize() {
	$("#main-body").width($(window).width())
	$("#main-body").height($(window).height())
	var frameHeight = ($(window).height() * .85)
	var isHorizontal = true;
	var frameWidth = frameHeight + (frameHeight * 13 / 21)
	$(".page-content").width(frameWidth)
	$(".page-content").height(frameHeight)
	$(".page-content").css({
		"left": ($(window).width() - $(".page-content").width()) / 2 + "px",
		"top": ($(window).height() - $(".page-content").height()) / 2 + "px"
	})
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
			{ scaleY: 1, scaleX: 1, rotation: 0, transformOrigin: "center" })
	})
}
$(window).bind('resize', function () {
	windowLayoutFitSize()
});

$(document).ready(function () {
	$(".menu-icon").load("static/img/icons/menu.svg", function () {
		var tlMenu = new TimelineLite({
			paused: true
		});
		tweenMenuShow = tlMenu.from(".menu-items-holder", .5, {
			top: "-100%",
			transformOrigin: "top"
		});
		tweenMenuShow.reverse()
		$(this).on("click", function () {
			if (tweenMenuShow.reversed())
				tweenMenuShow.play()
			else
				tweenMenuShow.reverse()
		})
	})
	windowLayoutFitSize()
});

$(window).on("load",
	function () {
		$(".menu-item").attr("onclick", "loadContent(this)")
		// loadBackgroundAnimParticles()
		loadUniverseBG()
	})

function loadBackgroundAnimParticles() {
	var canvas, ctx, w, h;

	var h = $(window).height();
	var w = $(window).width();

	var canvas = document.createElement('canvas');
	document.body.appendChild(canvas);
	canvas.width = w;
	canvas.height = h;
	ctx = canvas.getContext('2d');

	function paintCanvas() {
		ctx.fillStyle = "rgba(22,77,122,1)";
		ctx.fillRect(0, 0, w, h);
	}


	function particle(r, off, c) {
		this.x = Math.random() * w;
		this.y = Math.random() * h;
		this.r = r;
		this.offset = Math.random() * 50 + off;
		this.color = "rgba(255,255,255," + c + ")"
		this.draw = function () {
			ctx.fillStyle = this.color;
			ctx.beginPath();
			ctx.arc(this.x, this.y, this.r, Math.PI * 2, false);
			ctx.fill();
		}

	}

	var layer_1 = [],
		layer_2 = [],
		layer_3 = [];

	var layer_1_num = 33;
	var layer_2_num = 66;
	var layer_3_num = 99;


	for (i = 0; i < layer_1_num; i++) {
		layer_1.push(new particle(4, 11, 1));

	}
	for (i = 0; i < layer_2_num; i++) {
		layer_2.push(new particle(2.5, 33, 1));
	}
	for (i = 0; i < layer_3_num; i++) {
		layer_3.push(new particle(1, 66, 1));
	}

	function draw() {
		for (i = 0; i < layer_1.length; i++) {
			var p = layer_1[i];
			p.draw();
			update(p);
			checkBounds(p);
			for (var j = i + 1; j < layer_3.length; j++) {
				p2 = layer_3[j];
				distance(p, p2, w * 1.5);
			}

		}
		for (i = 0; i < layer_2.length; i++) {
			var p = layer_2[i];
			p.draw();
			update(p);
			checkBounds(p);
			for (var j = i + 1; j < layer_3.length; j++) {
				p2 = layer_3[j];
				distance(p, p2);
			}
		}
		for (i = 0; i < layer_3.length; i++) {
			var p = layer_3[i];
			p.draw();
			update(p);
			checkBounds(p);
			for (var j = i + 1; j < layer_3.length; j++) {
				p2 = layer_3[j];
				distance(p, p2);
			}
		}
	}
	function update(p) {
		p.x = p.x - mouse.x / p.offset;
		p.y = p.y - mouse.y / p.offset;
	}
	function checkBounds(p) {
		if (p.x > w) {
			p.x = 0;
		}
		else if (p.x < 0) {
			p.x = w;
		}
		if (p.y > h) {
			p.y = 0;
		}
		else if (p.y < 0) {
			p.y = h;
		}
	}

	var minDist = w * 0.7;

	function distance(p1, p2) {
		var dist;
		var dx = p1.x - p2.x;
		var dy = p1.y - p2.y;
		dist = Math.sqrt(dx * dx + dy * dy);

		if (dist <= minDist) {
			ctx.beginPath();
			ctx.strokeStyle = "rgba(255,255,255," + (0.2 - dist / minDist) + ")";
			ctx.moveTo(p1.x, p1.y);
			ctx.lineTo(p2.x, p2.y);
			ctx.stroke();
			ctx.closePath();
		}
	}

	var mouse = {
		x: 0,
		y: 0
	}

	document.addEventListener('mousemove', function (e) {
		mouse.x = e.clientX - w / 2 || e.pageX - w / 2;
		mouse.y = e.clientY - h / 2 || e.pageY - h / 2;
	}, false);

	function animate() {
		paintCanvas();
		draw();
		requestAnimationFrame(animate);
	}
	// setInterval(function(){
	// 	paintCanvas();
	// 	draw();
	// },30);
	animate();
}


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
	var giantColor = '180,184,240';
	var starColor = '226,225,142';
	var cometColor = '226,225,224';
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
			this.opacityTresh = getRandInterval(.2, 1 - (this.comet + 1 - 1) * .4);
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
				this.fadingOut = this.opacity < 0 ? false : true;
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

				//comet tail
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
  div = $("#schoolDropdown");
  a = div.find("a");
  for (i = 0; i < a.length; i++) {
    txtValue = a[i].textContent || a[i].innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      a[i].style.display = "";
    } else {
      a[i].style.display = "none";
    }
  }
}
