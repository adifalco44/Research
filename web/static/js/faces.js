$(window).load(function(){});

$(document).ready(function(){
	setTimeout(function(){
		$("#ProbeID").addClass("row");
		setTimeout(function(){
			$("#Images").removeClass("row hidden");
			$("#Images").addClass("row");
			$("#ProbeID").addClass("row hidden");
		},1000);
	},1000);
});

