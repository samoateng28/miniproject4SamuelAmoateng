# INF601 - Advanced Programming in Python
# samuel Amoateng
# Mini Project 4



Samuel Media
This is a platform where users can blog articles and share with each other.

## Setup

```bash
# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Initialize the database

Run these commands in order:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

A non-interactive admin user was created locally for convenience: `admin / adminpass`.

## Run the server

```bash
python manage.py runserver
```

- Home: `/`
- About: `/about/`
- Features: `/features/`
- Contact: `/contact/`
- Dashboard (login required): `/dashboard/`
- Auth: `/login/`, `/logout/`, `/register/`
- Admin: `/admin/`

## Notes
- A sample `Post` model is registered in the admin.
- Static files directory is `static/`.

