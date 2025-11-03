from flask import Blueprint, render_template, request, redirect, url_for
from ..extensions import db
from ..models.movie import Movie

movie_fr_bp = Blueprint('movie_fr_bp', __name__, url_prefix='/')

# Home page (index.html)
@movie_fr_bp.route('/')
def home():
    movies = Movie.query.all()
    return render_template("index.html", movies=movies)
@movie_fr_bp.route('/about')
def about():
    return render_template("about-us.html")

# List movies page (optional)
@movie_fr_bp.route('/list_movies')
def list_movies():
    movies = Movie.query.all()
    return render_template("list-movies.html", movies=movies)

# Add movie
@movie_fr_bp.route("/add_movie", methods=["GET", "POST"])
def add_movie():
    if request.method == "POST":
        movie_name = request.form.get("movie_name")
        type_ = request.form.get("type")
        price = request.form.get("price")
        quality = request.form.get("quality")
        rating = request.form.get("rating")
        year = request.form.get("year")
        director = request.form.get("director")
        role = request.form.get("role")
        time_watching = request.form.get("time_watching")
        hall_name = request.form.get("hall_name")
        chair_number = request.form.get("chair_number")

        if not all([movie_name, type_, price, quality]):
            return "Title, Type, Price, and Quality are required!", 400

        try:
            price = float(price)
            rating = float(rating) if rating else None
            year = int(year) if year else None
            time_watching = int(time_watching) if time_watching else None
        except ValueError:
            return "Price, Rating, Year, and Time Watching must be numbers.", 400

        new_movie = Movie(
            movie_name=movie_name,
            type=type_,
            price=price,
            quality=quality,
            rating=rating,
            year=year,
            director=director,
            role=role,
            time_watching=time_watching,
            hall_name=hall_name,
            chair_number=chair_number
        )
        db.session.add(new_movie)
        db.session.commit()

        return redirect(url_for('movie_fr_bp.list_movies'))

    # Pass an empty movie dict for template
    return render_template("add-movie.html", movie={})




# Edit movie
@movie_fr_bp.route("/edit_movie/<int:movie_id>", methods=["GET", "POST"])
def edit_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)

    if request.method == "POST":
        movie.movie_name = request.form.get("movie_name")
        movie.type = request.form.get("type")
        try:
            movie.price = float(request.form.get("price"))
        except ValueError:
            return "Price must be a number.", 400
        movie.quality = request.form.get("quality")

        db.session.commit()
        # Redirect to home page
        return redirect(url_for('movie_fr_bp.home'))

    return render_template("edit-movie.html", movie=movie)

# Delete movie
@movie_fr_bp.route("/delete_movie/<int:movie_id>", methods=["POST"])
def delete_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    db.session.delete(movie)
    db.session.commit()
    # Redirect to home page
    return redirect(url_for('movie_fr_bp.home'))

# Search movies
@movie_fr_bp.route("/movies/search")
def search_movies():
    query = request.args.get("q", "").strip()
    if query:
        movies = Movie.query.filter(Movie.movie_name.ilike(f"%{query}%")).all()
    else:
        movies = Movie.query.all()
    return render_template("list-movies.html", movies=movies)

# Filter movies by type
@movie_fr_bp.route("/movies/type/<type_name>")
def filter_by_type(type_name):
    movies = Movie.query.filter_by(type=type_name).all()
    return render_template("list-movies.html", movies=movies)
# View single movie details
@movie_fr_bp.route("/view_movie/<int:movie_id>")
def view_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    return render_template("view-movie.html", movie=movie)
