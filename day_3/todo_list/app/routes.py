from app import app
from flask import render_template

@app.route('/<name>')
def index(name):
    return f"{name} loves cake!"

@app.route('/')
def home():
    user = {"username": "Marina"}
    tasks = [
    {
        'id': 1,
        'title': 'Buy groceries',
        'description': 'Milk, Cheese, Pizza, Fruit, biscuits',
        'done': False
    },
    {
        'id': 2,
        'title': 'Learn Python',
        'description': 'Learn an awesome new programming language',
        'done': True
    }
    ]
    return render_template("index.html", title="Home", user=user, tasks=tasks)
