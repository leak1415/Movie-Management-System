from app import create_app
from app.extensions import db
from app.seeds.movies_seed import seed_movies

app = create_app()

with app.app_context():
    db.create_all()  # Ensure tables exist
    seed_movies()
