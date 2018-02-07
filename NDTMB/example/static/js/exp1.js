var hidden = false;
//var visiblebutton = false;

/*
setInterval(function(){
    //visiblebutton = false;
    //checkButton();
    document.getElementById("image").style.visibility= hidden ? "visible" : "hidden";
},2000);
*/

setTimeout(function() { 
    document.getElementById("button0").style.visibility='visible'; 
    document.getElementById("button1").style.visibility='visible'; 
    document.getElementById("button2").style.visibility='visible'; 
  }, 2000);

/*
$(document).ready(function() {
  setTimeout(function() {
    $("#button0").show();
    $("#button1").show();
    $("#button2").show();
  }, 2000);
});
*/
/*
#button0 {
  display: none;
}
#button1 {
  display: none;
}
#button1 {
  display: none;
}
*/
/*
setInterval2(function(){
	visiblebutton = true;
	checkButton();
});

*/
/*
function checkButton() {
	/*
	var date = new Date();
	var seconds = date.getSeconds();
	var secondsafter = date.getSeconds();
	
	if (visiblebutton == false) {
		document.getElementById("button0").style.visibility = "hidden";
		document.getElementById("button1").style.visibility = "hidden";
		document.getElementById("button2").style.visibility = "hidden";
	} else {
		document.getElementById("button0").style.visibility = "visible";
		document.getElementById("button1").style.visibility = "visible";
		document.getElementById("button2").style.visibility = "visible";
	}
}


/*
appearButtons(function(){
    document.getElementById("button0").style.visibility= "hidden";
    document.getElementById("button1").style.visibility= hidden ? "visible" : "hidden";
    document.getElementById("button1").style.visibility= hidden ? "visible" : "hidden";


}, 2000);
*/
