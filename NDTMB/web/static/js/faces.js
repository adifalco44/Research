$(window).bind('load', function(){

	var last,diff;
	var timer = parseInt($('#ProbeTime')[0].value);
	$("#ProbeID").removeClass("hidden");
	setTimeout(function(){
		$("#Images").removeClass("hidden");
		$("#ProbeID").addClass("hidden");
		last = event.timeStamp;
	}, timer);
	$("#button1").click(function(event){
		diff = parseInt(event.timeStamp-last);
		$.cookie("timer",diff, {path: '/'});
	});
	$("#button2").click(function(event){
		diff = parseInt(event.timeStamp-last);
		$.cookie("timer",diff, {path: '/'});	
	});
	$("#button3").click(function(event){
		diff = parseInt(event.timeStamp-last);
		$.cookie("timer",diff, {path: '/'});
	});
});
