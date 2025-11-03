from flask import Flask
from .extensions import db, migrate
from .config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    from .routes.movies_routes import movie_bp
    from .routes.movies_fr_routes import movie_fr_bp
    app.register_blueprint(movie_bp)
    app.register_blueprint(movie_fr_bp)

    return app

def register_commands(app):
    import click
    from .seeds.movies_seed import seed_movies

    @app.cli.command("seed")
    def seed():
        """Seed the database with initial data."""
        with app.app_context():
            db.create_all()  # Ensure tables exist
            seed_movies()
            click.echo("🎉 Database seeded successfully!")