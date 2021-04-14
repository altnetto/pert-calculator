from flask import Blueprint, render_template, redirect, request
from flask.helpers import url_for
from app.models.task_model import TaskModel
from app.app import db

index = Blueprint('index', __name__)


@index.route('/')
def start():

    data = {
        '68': {'range': 0, 'min': 0, 'max': 0, 'expected': 0},
        '95': {'range': 0, 'min': 0, 'max': 0, 'expected': 0},
        '99': {'range': 0, 'min': 0, 'max': 0, 'expected': 0}
    }

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
                data[range] = { 'min': f'{minimals[range]:.2f}', 'max': f'{maximums[range]:.2f}', 'expected': f'{expecteds[range]:.2f}', 'range': f'{ranges[range]:.2f}' }

    return render_template('main_page.html', tasks = tasks, data = data)


@index.route('/add', methods=['GET','POST'])
def add_task():
    if request.method == "POST":
        name = request.form.get('activity')
        optmist = float(request.form.get('optmist'))
        most_probable = round(float(request.form.get('most-probable')), 2)
        pessimist = float(request.form.get('pessimist'))
        critical = True if request.form.get('critical') else False

        new_task = TaskModel(name, critical, optmist, most_probable, pessimist)

        db.session.add(new_task)
        db.session.commit()

    return redirect(url_for('index.start'))


@index.route('/delete/<int:id>')
def delete(id):
    task = TaskModel.query.filter_by(id = id).first()
    
    db.session.delete(task)
    db.session.commit()

    return redirect(url_for('index.start'))


@index.route('/update/<int:id>', methods = ['GET', 'POST'])
def update(id):
    
    task_edit = TaskModel.query.filter_by(id = id).first()

    if request.method == 'POST':

        task_edit.name = request.form.get('activity')
        task_edit.optmist = float(request.form.get('optmist'))
        task_edit.most_probable = round(float(request.form.get('most-probable')), 2)
        task_edit.pessimist = float(request.form.get('pessimist'))
        task_edit.critical = True if request.form.get('critical') else False
        task_edit.expected_time = task_edit.calculate_expected()

    task_edit.editing = not task_edit.editing

    db.session.add(task_edit)
    db.session.commit()

    return redirect(url_for('index.start'))