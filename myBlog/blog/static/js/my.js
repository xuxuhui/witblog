$(document).ready(function(){
	$(".likeit").click(function(){
		var article_id;
		var elem = $(this);
		$(this).animate({
			opacity: '0.7'
		});
		article_id = elem.attr("data-article_id");
		$.get("/blog/likeit/"+article_id+"/", function(like){
			elem.html("喜爱 "+like+"&nbsp&nbsp&nbsp&nbsp&nbsp<img src='/static/img/like.png'>");
			elem.animate({ opacity: '1'})
		});
	});
});

var cool = new function() {
	this.str = "";
	this.last = 0;
	this.index = 1;
	this.i = 0;
}

function showCool(){
	if (window.location.pathname == '/' && window.location.search == "") {
		$("#main").hide();	
		$(".cool").css({'display':'block'});
		cool.str = $("pre").text();
		$("pre").text("");
		showCode();
	return 1
	}
}

function showCode() {
	$("pre").text(function(n, s) {
		var cur;
		switch (cool.last)
		{
			case '\n':
			case 0:
				cur = cool.index + " "
				cool.index++
				break;

			default:
				cur = cool.str[cool.i];
				cool.i++;
				break;
		}
		cool.last = cur;
		s += cur;
		return s;
	})

	if (cool.str.length > cool.i) {
		setTimeout(showCode, 30);
		if (cool.str.length - cool.i == 2) {
			$("#main").fadeIn("slow");
			$(".cool").fadeOut(3000);
		}
	}
}
