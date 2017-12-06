// $(window).on('load',function(){
// 	var timer = parseInt($('#ProbeTime')[0].value);
// 	$("#ProbeID").removeClass("hidden");
// 	setTimeout(function(){
// 		$("#Images").removeClass("hidden");
// 		$("#ProbeID").addClass("hidden");
// 	}, timer);
// });

$(window).bind('load', function(){
	var timer = parseInt($('#ProbeTime')[0].value);
	$("#ProbeID").removeClass("hidden");
	setTimeout(function(){
		$("#Images").removeClass("hidden");
		$("#ProbeID").addClass("hidden");
	}, timer);
});
