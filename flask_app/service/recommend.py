# recommend route
from flask import request
from sqlalchemy.sql.elements import and_
from sqlalchemy.sql.expression import func
from flask_app.models import Movie_info

# recommend prediction
def prediction():
    genre_text = request.args.get('genre')

    if genre_text == "0" :
        selection = Movie_info.query.order_by(func.random()).first()
    else:
        selection = Movie_info.query.filter(and_(Movie_info.genre==genre_text)).order_by(func.random()).first_or_404()
    
    return selection