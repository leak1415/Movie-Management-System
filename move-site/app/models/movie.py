from app.extensions import db


class Movie(db.Model):
    __tablename__ = "movie"

    movie_id = db.Column(db.Integer, primary_key=True)
    movie_name = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, default=0.0)
    quality = db.Column(db.String(50), nullable=False)

    # New fields
    rating = db.Column(db.Float, nullable=True)
    year = db.Column(db.Integer, nullable=True)
    director = db.Column(db.String(255), nullable=True)
    role = db.Column(db.String(255), nullable=True)
    time_watching = db.Column(db.Integer, nullable=True)  # in minutes
    image = db.Column(db.String(255), nullable=True)  # store filename or URL
    chair_number = db.Column(db.Integer, nullable=True)
    hall_name = db.Column(db.String(255), nullable=True)
    trailer_url = db.Column(db.String(255))  # YouTube link (optional)
    trailer_file = db.Column(db.String(255))

    def __repr__(self):
        return f"<Movie {self.movie_name}>"
