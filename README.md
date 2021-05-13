# vuebufferi

## Development setup
### Clone & setup project (only first time):
```bash
# Clone repository
git clone git@github.com:athenekilta/vuebufferi.git
cd vuebufferi
# Create and activate virtualenv
python3 -m venv venv
. venv/bin/activate
# Install requirements (inside virtualenv)
pip install -r requirements.txt
# Generate a .env file with secret key
(echo 'import secrets'; echo 'print(f"SECRET_KEY={secrets.token_urlsafe()}")') | python > .env
# Run migrations
python manage.py migrate
# Create superuser for Django
python manage.py createsuperuser
```

### Run development server:
```bash
# If venv is not already active
. venv/bin/activate
python manage.py runserver
```

### Make and apply migrations
When you pull code that includes new migrations, you should run `python manage.py migrate`.

In case your code requires changes in the database, run `python manage.py makemigrations` followed by `python manage.py migrate`.