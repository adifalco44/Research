$(document).ready(function(){
	setTimeout(function(){
		$("#ProbeID").removeClass("hidden");
		$("#ProbeID").addClass("row");
		setTimeout(function(){
			$("#ProbeID").removeClass("row");
			$("#Images").removeClass("hidden");
			$("#Images").addClass("row");
			$("#ProbeID").addClass("hidden");
		},300);
	},300);
});

