# Movie Site

A movie management application. Originally built with Flask, now also available as a Django app running side-by-side.

## Features

* List, add, edit, and delete movies.
* Flask: SQLAlchemy, Flask-Migrate, seed script.
* Django: Parity pages (home, list, view, add, edit, delete, search/filter) and uploads using the same static folders.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/Movie-Management-System.git
   cd Movie-Management-System
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

4. **Install dependencies:**
   - Flask app:
     ```bash
     pip install -r move-site/requirements.txt
     ```
   - Django app (side-by-side, optional):
     ```bash
     pip install django djangorestframework pillow python-dotenv
     ```

5. **(Optional) Create a `.env` file** if you want to override defaults (Flask):
   ```
   DATABASE_URL="sqlite:///app.db"
   SECRET_KEY="dev"
   ```

## Usage

### Database Migrations (Flask)

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

### Seeding the Database (Flask)

To populate the database with initial movie data, run the following command:
```bash
flask seed
```

### Running the Applications

- Flask (default):
  ```bash
  flask run
  # or
  python move-site/run.py
  ```
  App URL: `http://127.0.0.1:5000`

- Django (side-by-side):
  ```bash
  python django-site/manage.py migrate
  python django-site/manage.py runserver 8000
  ```
  App URL: `http://127.0.0.1:8000`

Notes:
- Both apps can run independently. The Django app reuses the Flask static folders at `move-site/app/static` for images and trailers.
