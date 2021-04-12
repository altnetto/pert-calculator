from flask import Blueprint, render_template, redirect, request
from flask.helpers import url_for
from app.models.task_model import TaskModel
from app.app import db

index = Blueprint('index', __name__)


@index.route('/')
def start():

    tasks = TaskModel.query.all()

    if tasks:
        
        critical_tasks = TaskModel.query.filter_by(critical = True).all()

        if critical_tasks:
            ranges = {"68": 1, "95": 2, "99": 3}
            minimals = {"68": 0, "95": 0, "99": 0}
            expecteds = {"68": 0, "95": 0, "99": 0}
            maximums = {"68": 0, "95": 0, "99": 0}
            data = {"68": None, "95": None, "99": None}
            average_variances = 0
            total_expected_time = 0

            for task in critical_tasks:
                average_variances += float(task.variance)
                total_expected_time += float(task.expected_time)

            average_variances = average_variances**(0.5)

            for range in ranges:
                ranges[range] *= average_variances
                minimals[range] = total_expected_time - ranges[range]
                expecteds[range] = total_expected_time
                maximums[range] = total_expected_time + ranges[range]
                data[range] = { 'min': minimals[range], 'max': maximums[range], 'expected': expecteds[range], 'range': ranges[range] }


    return render_template('main_page.html', tasks = tasks, data = data)


@index.route('/add', methods=['GET','POST'])
def add_task():
    if request.method == "POST":
        name = request.form.get('activity')
        optmist = float(request.form.get('optmist'))
        most_probable = float(request.form.get('most-probable'))
        pessimist = float(request.form.get('pessimist'))
        critical = True if request.form.get('critical') else False

        new_task = TaskModel(name, critical, optmist, most_probable, pessimist)

        db.session.add(new_task)
        db.session.commit()

    return redirect(url_for('index.start'))
