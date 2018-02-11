function call() {
    var phoneNum = document.getElementById("inputNumber").value;
    var delaySecs = document.getElementById("inputDelay").value;
    var http = new XMLHttpRequest();
    var base_url = "https://agile-shore-10893.herokuapp.com";
    var url = base_url + "/calling";
    
    if (delaySecs == "" || delaySecs == null) {
    	delay = 0;
    }
    
    var params = "num=" + String(phoneNum) + "&delay=" + String(delaySecs);
    http.open("POST", url);
    http.send(params);
}

$(document).ready(function() {
});