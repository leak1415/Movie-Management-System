# Movie Site

A Flask-based web application for managing a collection of movies.

## Features

* List, add, edit, and delete movies.
* Database integration with SQLAlchemy.
* Database migrations with Flask-Migrate.
* Seeding script to populate the database with initial data.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/move-site.git
   cd move-site
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Create a `.env` file** and add the following line:
   ```
   DATABASE_URL="sqlite:///instance/app.db"
   ```

## Usage

### Database Migrations

1. **Initialize the database:**
   ```bash
   flask db init
   ```

2. **Create an initial migration:**
   ```bash
   flask db migrate -m "Initial migration"
   ```

3. **Apply the migrations:**
   ```bash
   flask db upgrade
   ```

### Seeding the Database

To populate the database with initial movie data, run the following command:
```bash
flask seed
```

### Running the Application

To start the development server, run:
```bash
flask run
```

The application will be available at `http://127.0.0.1:5000`.
