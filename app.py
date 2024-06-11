from flask import Flask, render_template, redirect, url_for, request
from config import Config
from models import db, Task
from forms import TaskForm
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    form = TaskForm()
    if form.validate_on_submit():
        new_task = Task(
            title=form.title.data,
            description=form.description.data,
            due_date=form.due_date.data,
            priority=form.priority.data,
            status='Pending'
        )
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_task.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
