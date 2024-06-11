from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, DateField, SubmitField
from wtforms.validators import DataRequired

class TaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description')
    due_date = DateField('Due Date', format='%Y-%m-%d')
    priority = SelectField('Priority', choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')])
    submit = SubmitField('Add Task')
