from flask import Blueprint, render_template

index = Blueprint('index', __name__)


@index.route('/')
def start():
    return render_template('main_page.html')


@index.route('/add', methods=['POST'])
def add_task():
    pass
