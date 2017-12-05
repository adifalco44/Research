$(window).load(function() {
});

var MYLIBRARY = MYLIBRARY || (function(){
    var _args = {}; // private

    return {
        init : function(Args) {
            _args = Args;
            // some other initialising
        },
        helloWorld : function() {
            alert('Hello World! -' + _args[0]);
        }
    };
}());

$(document).ready(function() {
	setTimeout(function() {
		$("#Gallery1ID").removeClass("hidden");
		$("#Gallery2ID").removeClass("hidden");
		$("#Gallery3ID").removeClass("hidden");
		$("#ProbeID").addClass("hidden");
	},50);
});
