//<script src="jquery-cookie/src/jquery.cookie.js">

$(window).bind('load', function(){

	var timer = parseInt($('#ProbeTime')[0].value);
	$("#ProbeID").removeClass("hidden");
	setTimeout(function(){
		$("#Images").removeClass("hidden");
		$("#ProbeID").addClass("hidden");
	}, timer);

	var last, diff;
	last = event.timeStamp;
	$("#button1").click(function(event){
		diff = parseInt(event.timeStamp-last);
		$.cookie("timer",diff);
		alert('waiting on button 3');
	});
	$("#button2").click(function(event){
		diff = parseInt(event.timeStamp-last);
		$.cookie("timer",diff);	
		alert('waiting on button 3');
	});
	$("#button3").click(function(event){
		diff = parseInt(event.timeStamp-last);
		$.cookie("timer",diff);
		alert('waiting on button 3');
	});

});
//</script>
