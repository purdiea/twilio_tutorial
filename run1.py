# Sample app from Twilio tutorial
# https://www.twilio.com/docs/quickstart/python/twiml/say-response#sample-app
# Code to play a message
from flask import Flask
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming requests."""
    resp = VoiceResponse()
    resp.say("Hello Monkey")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)