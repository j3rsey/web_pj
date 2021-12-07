from re import L
from flask_app import db
from sqlalchemy import Column, Integer, String, ForeignKey,Text , PickleType


class MyMovie(db.Model):
    __tablename__ = 'mymovie'

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie_info.id'), primary_key=True) 


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    review_ins = db.Column(db.String, nullable=False)
    #commentCreateTime = db.Column(db.DateTime())
    
    movie_info = db.relationship('Movie_info', secondary='mymovie')


class Movie_info(db.Model):
    __tablename__ = 'movie_info'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    ico_rating = db.Column(db.String)
    score = db.Column(db.Float)
    genre = db.Column(db.String, nullable=False)
    directors = db.Column(db.String, nullable=False)
    actors = db.Column(db.String, nullable=False)
    advance_rate = db.Column(db.String)
    runtime = db.Column(db.String)
    opening_date = db.Column(db.String)
    poster = db.Column(db.String)

    users = db.relationship('User', secondary='mymovie')

class Note(db.Model):
    __tablename__ = "note"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    content = db.Column(db.Text)

    def __init__(self, title, content):
        self.title = title
        self.content = content

