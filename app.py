from flask import Flask, jsonify, abort, request
import requests
import json

mensaje =""
destinatariowati =""
datos={}
app = Flask(__name__)

tasks = [
    {
        'prueba': 1,
        'prueba2': u'Buy groceries',
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/todo/api/v1.0/rec', methods=['POST'])
def create_task():
    global destinatariowati, mensaje, datos
    # if not request.json or not 'title' in request.json:
    destinatariowati = "51" + request.values.get('destinatario')
    destinatario = request.values.get('destinatario')
    mensaje = request.values.get('mensaje')
    try:
        datos = json.loads(mensaje)
        if (datos['service']=='bienvenida4'):
            sendwati()
    except:
        # sendgateway(mensaje,destinatario)
        sendwaboxapp(destinatario,mensaje)

    print(destinatariowati)
       
    return '''<h1>The language value is: {} y {}</h1>'''.format(destinatario,mensaje)

def test():    
    url = 'https://live-server-763.wati.io/api/v1/sendSessionMessage/51937535378'
    auth_token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJiODE0MjUzYy1mMDAyLTQ3MTYtYjkwOS0xMmJhY2E3MDc3ZDEiLCJ1bmlxdWVfbmFtZSI6ImFnZW50ZTVAdGVsZW5ldC5wZSIsIm5hbWVpZCI6ImFnZW50ZTVAdGVsZW5ldC5wZSIsImVtYWlsIjoiYWdlbnRlNUB0ZWxlbmV0LnBlIiwiYXV0aF90aW1lIjoiMDcvMTMvMjAyMSAxMzoxOTo0NCIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvcm9sZSI6IkFETUlOSVNUUkFUT1IiLCJleHAiOjI1MzQwMjMwMDgwMCwiaXNzIjoiQ2xhcmVfQUkiLCJhdWQiOiJDbGFyZV9BSSJ9.0YITXIKLxJHe5Prjt7O53ofcRvi0PNJb-U7TI06cRRE'
    param = {'messageText':"mensaje"}
    headers = {'Content-type': 'application/json ; charset=UTF-8','Authorization': 'Bearer ' + auth_token}
    response = requests.post(url, params=param, headers=headers)

    print(response)
    print(response.json())

def sendwati():    
    url = 'https://live-server-763.wati.io/api/v1/sendTemplateMessage'
    auth_token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI5MzYyNGQ3ZC03YWM0LTRkNzAtYjMzMS0yZGRkOGQ4YTJjNWQiLCJ1bmlxdWVfbmFtZSI6ImFnZW50ZTVAdGVsZW5ldC5wZSIsIm5hbWVpZCI6ImFnZW50ZTVAdGVsZW5ldC5wZSIsImVtYWlsIjoiYWdlbnRlNUB0ZWxlbmV0LnBlIiwiYXV0aF90aW1lIjoiMTEvMDUvMjAyMSAyMTozNToxMyIsImRiX25hbWUiOiJ3YXRpTGl2ZTc2MyIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvcm9sZSI6IkFETUlOSVNUUkFUT1IiLCJleHAiOjI1MzQwMjMwMDgwMCwiaXNzIjoiQ2xhcmVfQUkiLCJhdWQiOiJDbGFyZV9BSSJ9.ful2Vi947Y3jIKrgDkdGW7dpAnC6yFhYUwfALo0oUQc'
    param = {'whatsappNumber': destinatariowati}
    data={"template_name": datos["service"],
            "broadcast_name": datos["service"],
            "parameters": [{"name":"name", "value": datos["name"]}]
        }
    data2={"template_name": datos["service"],
            "broadcast_name": datos["service"],
        "parameters":[
            {"name":"name","value": datos["name"]},
            {"name":"cedula","value": datos["cedula"]},
            {"name":"codigo","value": datos["codigo"]},
            {"name":"dia_pago","value": datos["dia pago"]},
            {"name":"zona","value": datos["zona"]},
            {"name":"total cobrar","value": datos["total cobrar"]},
            {"name":"corte","value": datos["corte"]}
            ]
        }
    headers = {'Accept':'*/*','Content-type': 'application/json-patch+json ; charset=UTF-8','Authorization': 'Bearer ' + auth_token}
    response = requests.post(url, params=param, headers=headers,json=data2)
    print(response)
    print(response.json())    

def sendgateway(msn,destino):    
    url = 'https://smsgateway.me/api/v4/message/send'
    auth_token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhZG1pbiIsImlhdCI6MTYyNjcyNTU5MCwiZXhwIjo0MTAyNDQ0ODAwLCJ1aWQiOjg5NTk4LCJyb2xlcyI6WyJST0xFX1VTRVIiXX0.xHr7EHibHbAf-tYXH3Jq03wcxChwR4qj2oSQVZsJ0nE'
    # param = {'whatsappNumber': destinatario}
    headers = {'Accept':'*/*','Content-type': 'application/json-patch+json ; charset=UTF-8','Authorization': auth_token}
    data = [{
    "from": "GPON NETWORKS",
    "phone_number": destino,
    "message": msn,
    "device_id": 125132
    }]
    response = requests.post(url, headers=headers,json=data)
    print(response)
    print(response.json())

def sendwaboxapp(destino,mensaje):    
    token='?token=5303b353839545c8d5041da4eb118d866040e7fe2e166&uid=51927793746'
    uid='&uid=51927793746'
    to='&to=51'+destino
    custom_id='&custom_id=85214mih'
    text = '&text='+ mensaje
    url2 = 'https://www.waboxapp.com/api/send/chat'+token+uid+to+custom_id+text 
    response = requests.post(url2)
    print(response)
    print(response.json())   

if __name__ == '__main__':
    app.run(debug=False)
    # sendwaboxapp()