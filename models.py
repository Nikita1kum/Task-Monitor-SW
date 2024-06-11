from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    due_date = db.Column(db.Date, nullable=True)
    priority = db.Column(db.String(10), nullable=False, default='Medium')
    status = db.Column(db.String(10), nullable=False, default='Pending')
