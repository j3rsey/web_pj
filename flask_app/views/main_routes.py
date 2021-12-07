from flask import Blueprint, render_template, request, redirect, url_for
from flask_app import db
from flask_app.models import Movie_info, User, MyMovie, Note
from datetime import datetime
from flask_app.service.recommend import prediction

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('main_img.html')    

@bp.route('/movie_list')
def movie_list():
    movie_list = Movie_info.query.order_by(Movie_info.id.asc())
    print(movie_list)
    return render_template('movie_list.html', movie_list=movie_list)

@bp.route('/movie_list/title/<int:id>/')
def movie_content(id):
    movie_i = Movie_info.query.get_or_404(id)
    return render_template('movie_info_1.html', movie_i=movie_i)

@bp.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        note = Note(request.form['title'], request.form['content'])
        db.session.add(note)
        db.session.commit()
        return redirect(url_for('.index_r'))

    return render_template('add.html')

@bp.route('/read')
def index_r():
    note = Note.query.all()
    return render_template('index_r.html', note=note)

@bp.route('/read/edit/<int:id>', methods=['POST', 'GET'])
def edit(id):
    note = Note.query.get(id)
    if request.method == 'POST':
        note.title = request.form['title']
        note.content = request.form['content']
        db.session.commit()
        return redirect(url_for('.index_r'))
    return render_template('add.html', note=note)

@bp.route('/read/delete/<int:id>', methods=['POST', 'GET'])
def delete(id):
    note = Note.query.get(id)
    db.session.delete(note)
    db.session.commit()

    return redirect(url_for('.index_r'))
