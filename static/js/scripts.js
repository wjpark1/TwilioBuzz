function call() {
    var phoneNum = document.getElementById("inputNumber").value;
    var delaySecs = document.getElementById("inputDelay").value;
    var http = new XMLHttpRequest();
    var base_url = "https://will-phonebuzz.herokuapp.com";
    var url = base_url + "/calling";
    
    if (delaySecs == "" || delaySecs == null) {
    	delay = 0;
    }
    
    var params = "num=" + phoneNum + "&delay=" + delaySecs;
    http.open("POST", url);
    http.send(params);
}

$(document).ready(function() {
});