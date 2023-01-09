from flask import Flask, request
from fastapi import FastAPI
import requests


app = Flask(__name__)



@app.route('/')
def index():
    return 'Hello!'

@app.route('/audio_url')
def audio_url():
    audiourl = request.args.get('audio_url')
    return audiourl

url = "https://api.aiforthai.in.th/partii-webapi"
 
files = {'wavfile': ('RecTest1.wav', open('RecTest1.wav', 'rb'), 'audio/wav')}
 
headers = {
    'Apikey': "ebhSp3ApGgSnw8vSrUcdV9NB2Kv6LdsB",
    'Cache-Control': "no-cache",
    'Connection': "keep-alive",
    }
 
param = {"outputlevel":"--uttlevel","outputformat":"--txt"}
 
response = requests.request("POST", url, headers=headers, files=files, data=param)
 
print("Result = " + response.text)

if __name__== '__main__':
    app.run(debug=True)