from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/create_log', methods=['POST'])
def create_log():
    pass

@main.route('/add')
def add():
    return render_template('add.html')

@main.route('/view')
def view():
    return render_template('view.html')