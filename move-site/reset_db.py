# reset_db.py
from app import create_app
from app.extensions import db
from app.models.movie import Movie

app = create_app()

with app.app_context():
    print("Dropping all tables...")
    db.drop_all()

    print("Creating all tables...")
    db.create_all()

    # Seed sample data with new fields
    movie1 = Movie(
        movie_name="Inception",
        type="Action",
        price=12.50,
        quality="4K",
        rating=8.8,
        year=2010,
        director="Christopher Nolan",
        role="Leonardo DiCaprio",
        time_watching=148,
        image="inception.jpg",
        chair_number=120,
        hall_name="IMAX Hall 1"
    )

    movie2 = Movie(
        movie_name="The Godfather",
        type="Drama",
        price=10.00,
        quality="HD",
        rating=9.2,
        year=1972,
        director="Francis Ford Coppola",
        role="Marlon Brando",
        time_watching=175,
        image="godfather.jpg",
        chair_number=80,
        hall_name="Classic Hall A"
    )



db.session.add_all([movie1, movie2])
db.session.commit()

print("✅ Database reset and seeded successfully!")
