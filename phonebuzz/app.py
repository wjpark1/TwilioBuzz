import os
import twilio.twiml
from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Gather
from flask import redirect, url_for

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main():
    return redirect(url_for('voice'))

@app.route("/voice", methods=['GET', 'POST'])
def voice():
    resp = VoiceResponse()
    gather = Gather(finishOnKey="#", action="/number", method="POST")
    gather.say("Please enter a number followed by the pound sign.", voice="woman")
    resp.append(gather)

    resp.redirect("/voice")

    return str(resp)
    
@app.route("/number", methods=['GET', 'POST'])
def number():
    resp = VoiceResponse()
    message = "....."
    if 'Digits' in request.values:
        number = int(request.values['Digits'])
    
        for num in range(1,number+1):
            message += ""
            if num % 15 == 0:
        		message += "FizzBuzz"
            elif num % 3 == 0:
        	    message += "Fizz"
            elif num % 5 == 0:
        	    message += "Buzz"
            else:
        	    message += str(num)
        	
            message += "....."
    	
    message += "Thank you for playing PhoneBuzz."
    resp.say(message, voice="woman")
    return str(resp)
    
app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 3000)))