$(window).on('load',function(){
	var timer = parseInt($('#ProbeTime')[0].value);
	// setTimeout(function(){
		$("#ProbeID").removeClass("hidden");
		// $("#ProbeID").addClass("row");
		setTimeout(function(){
			// $("#ProbeID").removeClass("row");
			$("#Images").removeClass("hidden");
			// $("#Images").addClass("row");
			$("#ProbeID").addClass("hidden");
		}, timer);
	// }, 1000);
});
