import re
from flask import Flask, jsonify, abort, request
from flask_cors import CORS
import requests
import json

from werkzeug.wrappers import response

mensaje =""
responselive=""
destinatariowati =""
datos={}

app = Flask(__name__)
CORS(app)

tasks = [
    {
        'prueba': 1,
        'prueba2': u'Buy groceries',
    }
]
mwptrue={
  "estado": "exito",
  "mensaje": "Operación exitosa."
}
mwpfalse={
  "estado": "sin exito",
  "mensaje": "Operación falló."
}

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/todo/api/v1.0/live', methods=['GET'])
def live():
    livesendmsg()
    return jsonify({'tasks': livesendmsg()})    

@app.route('/todo/api/v1.0/mwp', methods=['POST'])
def mwp():
    print(str(request.json))
    resp = jsonify(success=True)
    if (resp.status_code==200):        
        datas = request.json
        sendtomwp(datas)
        
        return jsonify(mwptrue)
    else:
        return jsonify(mwpfalse)

@app.route('/todo/api/v1.0/rec', methods=['POST'])
def create_task():
    global destinatariowati, mensaje, datos
    # if not request.json or not 'title' in request.json:
    destinatariowati = "51" + request.values.get('destinatario')
    destinatario = request.values.get('destinatario')
    mensaje = request.values.get('mensaje')
    
    try:
        datos = json.loads(mensaje)
        if ("wati" in datos['service']):
            sendwati()
        if (datos['service']=='file'):
            livesendmsg(destinatariowati,mensaje)   
    except:
        # sendgateway(mensaje,destinatario)
        # sendwaboxapp(destinatario,mensaje)
        livesendmsg(destinatariowati,mensaje)

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
    auth_token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI0M2I0Mjk3My0yNWI3LTRhYjYtODQxYy1lNTQwZDU3OTQ4YmIiLCJ1bmlxdWVfbmFtZSI6ImFnZW50ZTVAdGVsZW5ldC5wZSIsIm5hbWVpZCI6ImFnZW50ZTVAdGVsZW5ldC5wZSIsImVtYWlsIjoiYWdlbnRlNUB0ZWxlbmV0LnBlIiwiYXV0aF90aW1lIjoiMTIvMDcvMjAyMSAxNDowNzoyOCIsImRiX25hbWUiOiJ3YXRpTGl2ZTc2MyIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvcm9sZSI6IkFETUlOSVNUUkFUT1IiLCJleHAiOjI1MzQwMjMwMDgwMCwiaXNzIjoiQ2xhcmVfQUkiLCJhdWQiOiJDbGFyZV9BSSJ9.aSbOQ_quBqa7xnEL3kJCsSJxUcXuztCLwYC0HEkCJgo'
    split=datos["service"].split(".")
             
    param = {'whatsappNumber': destinatariowati}
    data={"template_name": datos["service"],
            "broadcast_name": datos["service"],
            "parameters": [{"name":"name", "value": datos["name"]}]
        }
    data2={"template_name": split[1],
            "broadcast_name": split[1],
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

def livesendmsg(destinatario,mensaje):   
    url = 'https://api.pagegear.co/liveconnect/account/token'
    headers = {'Accept':'*/*','Content-type': 'application/json'}
    data = {
    "cKey": "77f75b91674e06b4e305b95c026d53d1",
    "privateKey": "851d1d96d6633b4ced6d3d50d6d6a956"
    }
    response = requests.post(url, headers=headers,json=data)
    responsejson = response.json()
    tokenlive = responsejson["PageGearToken"]
    
    try:
        datostoken = json.loads(str(mensaje))
        if (datostoken['service']=='file'):
            livesendfile(tokenlive,destinatario,mensaje)
        # print(str(datostoken))   
        print("file")  
    except:
        livesendmsg1(tokenlive,destinatario,mensaje)
        print("msg")    
        print(str(mensaje))    
    # return tokenlive

def livesendmsg1(token,destinatario,mensaje):   
    url = 'https://api.pagegear.co/liveconnect/direct/wa/sendMessage'
    headers = {'Accept':'*/*','Content-type': 'application/json','PageGearToken': token}
    datamsg1 = {
    "id_canal": 2974,
    "numero": int(destinatario),
    "mensaje": mensaje
    }
    try:
        response = requests.post(url, headers=headers,json=datamsg1)
        print("exito envio msg liveconnect")
    except:
        print("Fallo al enviar msg")  
    # responsejson = response.json()

def livesendfile(token,destinatario,mensaje):   
    url = 'https://api.pagegear.co/liveconnect/direct/wa/sendFile'
    headers = {'Accept':'*/*','Content-type': 'application/json','PageGearToken': token}
    datosfile = json.loads(mensaje)
    datafile = {
    "id_canal": 2974,
    "numero": int(destinatario),
    "url" : datosfile['url'],
    "nombre": datosfile['nombre'],
    "extension": datosfile['extension']
    }
    print(datosfile['url'])
    try:
        response = requests.post(url, headers=headers,json=datafile)
        print("exito envio file liveconnect")
    except:
        print("Fallo al enviar file")  
    # responsejson = response.json()
   
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

#/////////////////MIKROWISP PRE-REGISTRO///////////////////

def sendtomwp(req):   
    urllima = 'https://oficina.gpon.pe/api/v1/NewPreRegistro'
    urlcusco ='https://oficinacusco.gpon.pe/api/v1/NewPreRegistro'
    tokenmwp = "cFhtUEdjTFlVMWpXY3FXUjR1Rmxzdz09"

    headers = {'Accept':'*/*','Content-type': 'application/json'}
   
    try:    
          
        req["token"] = tokenmwp
        datadump= json.dumps(req)
        datajson = json.loads(datadump)
        # datajson.update(datatoken)
        # print(str(datajson))

        response = requests.post(urllima, headers=headers,json=datajson)
        print(response.json())
        print("exito envio mikrowisp")
    except:
        print("Fallo al enviar mikrowisp")  
    # responsejson = response.json()    

if __name__ == '__main__':
    app.run(debug=False)
    # sendwaboxapp()
