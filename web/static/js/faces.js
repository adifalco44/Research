$(document).ready(function(){
	var timer = document.getElementById("#Gallery1ID").value;
	setTimeout(function(){
		$("#ProbeID").removeClass("hidden");
		$("#ProbeID").addClass("row");
		setTimeout(function(){
			$("#ProbeID").removeClass("row");
			$("#Images").removeClass("hidden");
			$("#Images").addClass("row");
			$("#ProbeID").addClass("hidden");
		},timer);
	},timer);
});

