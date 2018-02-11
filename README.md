# TwilioBuzz
This is a code challenge offered by LendUp to engineering candidates - the finished product should allow the user to play FizzBuzz with a computer program either by calling a Twilio phone number, or by having said Twilio number call a verified number. The user should also have the option to delay the call by a specified amount of time, and should be able to view and replay any past phone calls of their choice (the latter feature is currently in progress).

## Tech
This application was built with HTML, CSS, JavaScript, Flask, SQLite 3 and Twilio.

## Installation
You can try the app at https://agile-shore-10893.herokuapp.com/. However, you will only be able to call Twilio, rather than have Twilio call you (or another number) because Twilio's free account version only allows one verified number per Twilio number and I have already connected my own phone number as the verified number. 

To gain access to the full version, please do the following:
1) Clone the repo into a local directory of your choice
2) Open Terminal (or CLI of your choice) and cd into the project directory
3) Run `pip install -r requirements.txt` (this will download/update the dependencies listed in 'requirements.txt')
4) [Create a free account with Twilio](https://www.twilio.com/try-twilio), get a voice-enabled Twilio number and create a verified caller ID
5) [Set your environment variables](https://medium.com/@himanshuagarwal1395/setting-up-environment-variables-in-macos-sierra-f5978369b255) using your Twilio credentials, which will automatically be imported by 'config.py.' Alternatively, you can hard-code them into 'config.py', but make sure to delete them before sharing/uploading your code
6) [Create a free account with Heroku](https://signup.heroku.com/login) and create a domain - replace all instances of 'https://agile-shore-10893.herokuapp.com/' in app.py and scripts.js with your domain. 
7) Go to your Twilio account, navigate to your Twilio number and add your new domain as a webhook in "A CALL COMES IN" under "Voice & Fax".

## Thank You!
If you have any questions or comments, shoot me an email at wjpark@berkeley.edu. Thanks!
