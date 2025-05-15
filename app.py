# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify

app = Flask(__name__)

# Stockage en mémoire des tâches
todos = []

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos), 200

@app.route('/todos', methods=['POST'])
def add_todo():
    todo = request.json.get('task')
    if not todo:
        return jsonify({'error': 'Task is required'}), 400
    todos.append(todo)
    return jsonify({'task': todo}), 201

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
