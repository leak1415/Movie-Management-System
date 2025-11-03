from ..extensions import db
from ..models.movie import Movie

def seed_movies():
    movies_data = [
        (5, 'Frozen II', 'Animation', 8.99, 'HD'),
        (6, 'Joker', 'Drama', 11.50, 'HD'),
        (7, 'The Dark Knight', 'Action', 12.50, '4K'),
        (8, 'Spider-Man: No Way Home', 'Action', 14.00, '4K'),
        (9, 'Black Panther', 'Superhero', 13.50, '4K'),
        (10, 'Interstellar', 'Sci-Fi', 14.50, '4K')
    ]

    for movie_id, name, type_, price, quality in movies_data:
        existing = Movie.query.filter_by(movie_id=movie_id).first()
        if not existing:
            db.session.add(Movie(
                movie_id=movie_id,
                movie_name=name,
                type=type_,
                price=price,
                quality=quality
            ))
            print(f"✅ Added movie: {name}")
        else:
            print(f"⚠️ Skipped existing movie: {name}")

    db.session.commit()
    print("🎉 Movie seeding completed!")
