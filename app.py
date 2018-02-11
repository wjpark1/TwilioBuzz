import os
from flask import Flask, request, render_template
from flask import redirect, url_for
import twilio.twiml
from twilio.twiml.voice_response import VoiceResponse, Gather
from twilio.rest import Client
import time

app = Flask(__name__)
global base_url
base_url = "https://agile-shore-10893.herokuapp.com"

@app.route("/", methods=['GET', 'POST'])
def main():
    #return redirect(url_for('voice'))
    return render_template('index.html')

@app.route("/duplicate", methods=['GET', 'POST'])
def duplicate():
    #return redirect(url_for('voice'))
    return render_template('index.html')

@app.route("/calling", methods=['POST'])
def calling():
    data = request.args.get('num', '')
    # data = request.data
    # data = str(request.data)
    # data = request.form
    # data = request.get_data()

    # equalsIndex = data.index("=")
    # andIndex = data.index("&")
    # phoneNum = data[equalsIndex+1:andIndex]
    # phoneNum = "+1" + data
    # phoneNum = str(phoneNum)
    
    # data = data[andIndex+1:]
    # equalsIndex = data.index("=")
    # delaySecs = data[equalsIndex+1:]
    # delaySecs = int(delaySecs)
    # time.sleep(delaySecs)

    phoneNum = "+18186691671"
    fromNum = "+14248356673"
    account_sid = "AC62ddce460d6bddb103150545ff1ca851"
    auth_token  = "db0a6b71305a1ec16c4aaa189a6e496e"
    client = Client(account_sid, auth_token)
    url = base_url + "/voice"
    
    call = client.calls.create(to=phoneNum, from_=fromNum, url=url)
    # return ("Calling...")
    return str(data)

@app.route("/voice", methods=['GET', 'POST'])
def voice():
    resp = VoiceResponse()
    gather = Gather(action="/number", method="POST")
    gather.say("Please enter a number followed by the pound sign.", voice="woman")
    resp.append(gather)

    #resp.redirect("/voice")

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