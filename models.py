from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game = db.Column(db.String(50), unique=True, nullable=False)
    score_data = db.Column(db.String(120), nullable=False)
    is_live = db.Column(db.Boolean, default=True)

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    team = db.Column(db.String(100), nullable=False)
    sport = db.Column(db.String(50), nullable=False)
    points = db.Column(db.Integer, default=0)
    goals = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Player {self.name} - {self.team} - {self.sport}>'