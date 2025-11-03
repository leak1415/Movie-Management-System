from ..extensions import db
from ..models.movies import Movie

class PostService:
    @staticmethod
    def get_all_movies():
        """Return all posts."""
        return Movie.query.all()

    @staticmethod
    def get_movie_by_id(post_id):
        """Return a post by its ID or None if not found."""
        return Movie.query.get(post_id)

    @staticmethod
    def create_movie(title, type, price,quality):
        """Create and save a new movie."""
        movie = Movie(movie_name=title, type=type,price=price,quality=quality)
        db.session.add(movie)
        db.session.commit()
        return movie

    @staticmethod
    def update_post(movie_id, movie_name=None, type=None,price=None,quality=None):
        """Update an existing movie."""
        movie = Movie.query.get(movie_id)
        if not movie:
            raise ValueError("movie not found")

        if movie_name:
            movie.title = movie_name
        if type:
            movie.type = type
        if price:
            movie.price = price
        if quality:
            movie.quality = quality

        db.session.commit()
        return movie

    @staticmethod
    def delete_post(movie_id):
        """Delete a movie."""
        movie = Movie.query.get(movie_id)
        if not movie:
            raise ValueError("movie not found")

        db.session.delete(movie)
        db.session.commit()
        return True
