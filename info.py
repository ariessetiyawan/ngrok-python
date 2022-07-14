import requests
import time
import json
import sys
import logging

def get_ngrok_url():
    hasil='Ngrok tidak aktif !'
    try:
        url = "http://localhost:4040/api/tunnels/"
        res = requests.get(url)
        res_unicode = res.content.decode("utf-8")
        res_json = json.loads(res_unicode)
        dt={"aksi":"NG","urlng":(res_json['tunnels'][0]['public_url'])}
        hsil=requests.post('https://script.google.com/macros/s/xxxx/exec',dt)
        hasil= (res_json['tunnels'][0]['public_url'])
    except Exception as e:
        print(e, file=sys.stderr)
        pass
    return hasil

hasil=get_ngrok_url()
sys.exit()
