from flask import Flask,request, jsonify
from flask_cors import CORS, cross_origin
from pyngrok import ngrok
ngrok.set_auth_token("2B31mjO1FsSrwzWXXXXXXX_7Vn1dWAzCYhVHSqba6ZMt")
from flask_ngrok import run_with_ngrok
import requests,json
from flask import current_app
from requests import Session
import subprocess,time

app = Flask(__name__) #app name
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
run_with_ngrok(app)

def autoreplyInfo(idgas,ssid):
    with Session() as s:
        url='http://localhost:8001/chats/auto-reply'
        datax={"idgas":idgas,"sessionid":ssid}
        r=s.post(url,data=json.dumps(datax),headers={"Content-Type":"application/json"})
        return (json.loads(r.content))
def kirimpesan(ssid,data):
    try:
        with Session() as s:
            datax={"receiver":"6281330xxx884","message":{"image":{"url":"https://drive.google.com/uc?export=view&id=xxxxxx"},"caption":"lancar lek gak dihidden !"}}
            url='http://localhost:8001/chats/send?id='+ssid
            r=s.post(url,data=json.dumps(data),headers={"Content-Type":"application/json"})
            return (json.loads(r.content))
    except:
        p = subprocess.Popen(['node', '.'], stdout=subprocess.PIPE)
        time.sleep(5)
        with Session() as s:
            datax={"receiver":"6281330xxx884","message":{"image":{"url":"https://drive.google.com/uc?export=view&id=xxxx"},"caption":"lancar lek gak dihidden !"}}
            url='http://localhost:8001/chats/send?id='+ssid
            r=s.post(url,data=json.dumps(data),headers={"Content-Type":"application/json"})
            return (json.loads(r.content))
        pass

def buatsession(ssid,data):
    with Session() as s:
        url='http://localhost:8001/sessions/add'
        r=s.post(url,data=json.dumps(data),headers={"Content-Type":"application/json"})
        return (json.loads(r.content))
def delsession(ssid):
    with Session() as s:
        url='http://localhost:8001/sessions/delete/'+ssid
        r=s.delete(url,headers={"Content-Type":"application/json"})
        return (json.loads(r.content))
        
@app.route("/command", methods=['POST'])
def perintah():
    p = subprocess.Popen(['node', '.'], stdout=subprocess.PIPE)
    data={"app":'WA_CENTER_KUA',"message":"Selamat datang di Layanan WA CENTER KUA"}
    return data
    
@app.route("/")
def hello():
    data={"receiver":"6281330xxx884","message":{"image":{"url":"https://drive.google.com/uc?export=view&id=xxxx"},"caption":"Sukses terkirim tapi muter !"}}
    data={"app":'WA_CENTER_KUA',"command":request.json}
    return data

@app.route("/api_wa/<sessionid>", methods=['POST'])
def api_wa(sessionid):
    data = request.json
    hasilx=kirimpesan(sessionid,data)
    return hasilx

@app.route("/session_add/<sessionid>", methods=['POST','GET'])
def session_add(sessionid):
    data = request.json
    hasilx=buatsession(sessionid,data)

    hasilx.headers.add("Access-Control-Allow-Origin", "*");
    hasilx.headers.add("Access-Control-Allow-Credentials", "true");
    hasilx.headers.add("Access-Control-Allow-Methods", "GET,HEAD,OPTIONS,POST,PUT");
    hasilx.headers.add("Access-Control-Allow-Headers", "Access-Control-Allow-Headers, Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers");

    return hasilx    

@app.route("/session_del/<sessionid>", methods=['DELETE'])
def session_del(sessionid):
    hasilx=delsession(sessionid)
    return hasilx   

@app.route("/autoreply", methods=['POST'])
def autoreply():
    hasilx = request.json
    hasilx=autoreplyInfo(hasilx['idgas'],hasilx['sessionid'])
    return (hasilx)

@app.route("/test", methods=['POST','GET'])
def test():
    data = request.json
    #hasilx=kirimpesan(data)
    #hasilx=autoreplyInfo(data['idgas'],data['sessionid'])
    return (data) 

 
if __name__ == "__main__":
    p = subprocess.Popen(['node', '.'], stdout=subprocess.PIPE)
    app.run()
