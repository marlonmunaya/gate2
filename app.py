from flask import Flask, jsonify, abort, request
import requests
import json
# from flask_jwt_extended import JWTManager
mensaje =""
destinatario =""
app = Flask(__name__)
# app.config['SECRET_KEY'] = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJiODE0MjUzYy1mMDAyLTQ3MTYtYjkwOS0xMmJhY2E3MDc3ZDEiLCJ1bmlxdWVfbmFtZSI6ImFnZW50ZTVAdGVsZW5ldC5wZSIsIm5hbWVpZCI6ImFnZW50ZTVAdGVsZW5ldC5wZSIsImVtYWlsIjoiYWdlbnRlNUB0ZWxlbmV0LnBlIiwiYXV0aF90aW1lIjoiMDcvMTMvMjAyMSAxMzoxOTo0NCIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvcm9sZSI6IkFETUlOSVNUUkFUT1IiLCJleHAiOjI1MzQwMjMwMDgwMCwiaXNzIjoiQ2xhcmVfQUkiLCJhdWQiOiJDbGFyZV9BSSJ9.0YITXIKLxJHe5Prjt7O53ofcRvi0PNJb-U7TI06cRRE'
# jwt = JWTManager(app)
tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})    

@app.route('/todo/api/v1.0/rec', methods=['POST'])
def create_task():
    global destinatario, mensaje
    # if not request.json or not 'title' in request.json:
    destinatario = "51" + request.values.get('destinatario')
    mensaje = request.values.get('mensaje')
    # token= request.authorization
    # task = {
    #     'id': tasks[-1]['id'] + 1,
    #     'title': username,
    #     # 'title': request.json['title'],
    #     'description': request.json.get('description', ""),
    #     'done': False
    # }
    # tasks.append(task)
    # return jsonify({'task': task}), 201
    print(destinatario)
    print(mensaje)
    sendmsn()
    return '''<h1>The language value is: {} y {}</h1>'''.format(mensaje,mensaje)

def test():    
    url = 'https://live-server-763.wati.io/api/v1/sendSessionMessage/51937535378'
    auth_token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJiODE0MjUzYy1mMDAyLTQ3MTYtYjkwOS0xMmJhY2E3MDc3ZDEiLCJ1bmlxdWVfbmFtZSI6ImFnZW50ZTVAdGVsZW5ldC5wZSIsIm5hbWVpZCI6ImFnZW50ZTVAdGVsZW5ldC5wZSIsImVtYWlsIjoiYWdlbnRlNUB0ZWxlbmV0LnBlIiwiYXV0aF90aW1lIjoiMDcvMTMvMjAyMSAxMzoxOTo0NCIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvcm9sZSI6IkFETUlOSVNUUkFUT1IiLCJleHAiOjI1MzQwMjMwMDgwMCwiaXNzIjoiQ2xhcmVfQUkiLCJhdWQiOiJDbGFyZV9BSSJ9.0YITXIKLxJHe5Prjt7O53ofcRvi0PNJb-U7TI06cRRE'
    param = {'messageText':"mensaje"}
    headers = {'Content-type': 'application/json ; charset=UTF-8','Authorization': 'Bearer ' + auth_token}
    response = requests.post(url, params=param, headers=headers)
    # wait for the response. it should not be higher 
    # than keep alive time for TCP connection
    print(response)
    print(response.json())

def sendmsn():    
    url = 'https://live-server-763.wati.io/api/v1/sendTemplateMessage'
    auth_token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJiODE0MjUzYy1mMDAyLTQ3MTYtYjkwOS0xMmJhY2E3MDc3ZDEiLCJ1bmlxdWVfbmFtZSI6ImFnZW50ZTVAdGVsZW5ldC5wZSIsIm5hbWVpZCI6ImFnZW50ZTVAdGVsZW5ldC5wZSIsImVtYWlsIjoiYWdlbnRlNUB0ZWxlbmV0LnBlIiwiYXV0aF90aW1lIjoiMDcvMTMvMjAyMSAxMzoxOTo0NCIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvcm9sZSI6IkFETUlOSVNUUkFUT1IiLCJleHAiOjI1MzQwMjMwMDgwMCwiaXNzIjoiQ2xhcmVfQUkiLCJhdWQiOiJDbGFyZV9BSSJ9.0YITXIKLxJHe5Prjt7O53ofcRvi0PNJb-U7TI06cRRE'
    param = {'whatsappNumber': destinatario}
    data={"template_name": "confirmacion_pago",
            "broadcast_name": "confirmacion_pago",
            "parameters": [{"name":"name", "value":"John"}]
        }
    headers = {'Accept':'*/*','Content-type': 'application/json-patch+json ; charset=UTF-8','Authorization': 'Bearer ' + auth_token}
    response = requests.post(url, params=param, headers=headers,json=data)
    print(response)
    print(response.json())    


if __name__ == '__main__':
    app.run(debug=False)