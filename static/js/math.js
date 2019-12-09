function windowLayoutFitSize() {
	var frameWidth = $("#main-frame").width();
	$(".menu-items").each(function () {
		$(this).css("left", (frameWidth - $(this).width()) / 2)
	})
	$("#main-body").width($(window).width())
	$("#main-body").height($(window).height())
}
function loadContent(liItem) {
	$("div.page-content").hide()
	var url = ""
	// if (target.is("li")) {
	url = $(liItem).attr("data-href")
	// } else
	// 	url = liItem
	$("div.page-content").load(url, function () {
		$("div.page-content").fadeIn()
		TweenMax.fromTo(".page-content", 1, { scaleY: 0, scaleX: 0, rotation: -180 }, 
		{ scaleY: 1, scaleX: 1, rotation: 0, transformOrigin: "center" })
	})
}
$(window).bind('resize', function () {
	windowLayoutFitSize()
});

$(document).ready(function () {
	windowLayoutFitSize()
});

$(window).on("load",
	function () {
		$(".menu-item").attr("onclick", "loadContent(this)")
		loadBackgroundAnim()
	})

function loadBackgroundAnim() {
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
