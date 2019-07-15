import os

from flask import Flask
from flask import request
from flask import render_template

todo_store = {}
todo_store['depo'] = ['Go for run', 'Listen Rock Music']
todo_store['raj'] = ['Read book', 'Play Fifa', 'Drink Coffee']
todo_store['sanket'] = ['Sleep', 'Code']
todo_store['aagm'] = ['play cricket', 'have tea']

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    def select_todos(name):
        global todo_store
        return todo_store[name]

    def add_todo(name,todo):
        global todo_store
        current_todo = todo_store[name]
        current_todo.append(todo)
        todo_store[name] = current_todo

    def get_todos_by_name(name):
            return select_todos(name)
    
    def add_todo_by_name(name,todo):
        add_todo(name, todo)
        return

    # http://127.0.0.1:5000/todos?name=duster
    @app.route('/todos')
    def todos():
        name = request.args.get('name')
        print('---------')
        print(name)
        print('---------')
        person_todo_list = get_todos_by_name(name)
        return render_template('todo_view.html',todos=person_todo_list)

    @app.route('/add_todos')
    def add_todos():
        name = request.args.get('name')
        todo = request.args.get('todo')
        add_todo_by_name(name,todo)
        return 'added successfully'

    return app

