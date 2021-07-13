#!flask/bin/python
from re import U
from flask import Flask, jsonify, abort, request

app = Flask(__name__)

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
    # if not request.json or not 'title' in request.json:
    destinatario = request.args.get('destinatario')
    mensaje = request.args.get('mensaje')
    # task = {
    #     'id': tasks[-1]['id'] + 1,
    #     'title': username,
    #     # 'title': request.json['title'],
    #     'description': request.json.get('description', ""),
    #     'done': False
    # }
    # tasks.append(task)
    # return jsonify({'task': task}), 201

    return '''<h1>The language value is: {} y {}</h1>'''.format(destinatario,mensaje)

if __name__ == '__main__':
    app.run(debug=False)