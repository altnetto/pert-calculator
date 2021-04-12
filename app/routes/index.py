from flask import Blueprint, render_template, redirect, request
from flask.helpers import url_for
from app.models.task_model import TaskModel
from app.app import db

index = Blueprint('index', __name__)


@index.route('/')
def start():

    tasks = TaskModel.query.all()

    return render_template('main_page.html', tasks = tasks)


@index.route('/add', methods=['GET','POST'])
def add_task():
    if request.method == "POST":
        name = request.form.get('activity')
        optmist = float(request.form.get('optmist'))
        most_probable = float(request.form.get('most-probable'))
        pessimist = float(request.form.get('pessimist'))
        critical = request.form.get('critical')

        expected_time = (optmist + 4*most_probable + pessimist)/6
        standard_deviation = (pessimist - optmist)/6
        variance = standard_deviation**2

        new_task = TaskModel(name, critical, optmist, most_probable, pessimist, expected_time, standard_deviation, variance)

        db.session.add(new_task)
        db.session.commit()

    return redirect(url_for('index.start'))
