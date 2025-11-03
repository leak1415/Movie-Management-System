from flask import Blueprint, jsonify, request
from ..extensions import db
from ..models.movie import Movie

movie_bp = Blueprint('movie_bp', __name__, url_prefix='/movies')

# ---------------------------------
# GET /movies – get all movies
# ---------------------------------
@movie_bp.route('/', methods=['GET'])
def get_movies():
    movies = Movie.query.all()
    data = [
        {
            "movie_id": m.movie_id,
            "movie_name": m.movie_name,
            "type": m.type,
            "price": m.price,
            "quality": m.quality
        }
        for m in movies
    ]
    return jsonify(data), 200


# ---------------------------------
# GET /movies/<int:id> – get a single movie
# ---------------------------------
@movie_bp.route('/<int:id>', methods=['GET'])
def get_movie(id):
    movie = Movie.query.get_or_404(id)
    return jsonify({
        "movie_id": movie.movie_id,
        "movie_name": movie.movie_name,
        "type": movie.type,
        "price": movie.price,
        "quality": movie.quality
    }), 200


# ---------------------------------
# POST /movies – create a new movie
# ---------------------------------
@movie_bp.route('/', methods=['POST'])
def create_movie():
    data = request.get_json()

    movie_name = data.get('movie_name')
    type_ = data.get('type')
    price = data.get('price')
    quality = data.get('quality')

    if not movie_name or not type_ or price is None or not quality:
        return jsonify({"error": "Missing required fields"}), 400

    new_movie = Movie(
        movie_name=movie_name,
        type=type_,
        price=price,
        quality=quality
    )

    db.session.add(new_movie)
    db.session.commit()

    return jsonify({
        "message": "Movie added successfully",
        "movie_id": new_movie.movie_id
    }), 201


# ---------------------------------
# PUT /movies/<int:id> – update a movie
# ---------------------------------
@movie_bp.route('/<int:id>', methods=['PUT'])
def update_movie(id):
    movie = Movie.query.get_or_404(id)
    data = request.get_json()

    movie.movie_name = data.get('movie_name', movie.movie_name)
    movie.type = data.get('type', movie.type)
    movie.price = data.get('price', movie.price)
    movie.quality = data.get('quality', movie.quality)

    db.session.commit()
    return jsonify({"message": "Movie updated successfully"}), 200


# ---------------------------------
# DELETE /movies/<int:id> – delete a movie
# ---------------------------------
@movie_bp.route('/<int:id>', methods=['DELETE'])
def delete_movie(id):
    movie = Movie.query.get_or_404(id)
    db.session.delete(movie)
    db.session.commit()
    return jsonify({"message": "Movie deleted successfully"}), 200
