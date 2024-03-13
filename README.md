
# Flask movies API 

A basic movies CRUD (create read update and delete)
with Flask framework.

### Libraries included

- Flask-cors: for interdomain operations.
- psycopg2: connection with database (PostgreSQL)
- python-decouple: for managing env variables
- flask_parameter_validation: for validating parameters, e.g.: correct uuid format and movie properties.


### Run Locally

Clone the project

```bash
  https://github.com/spancavil/flask-movies-crud.git
```

Go to the project directory

```bash
  cd my-project
```

#### optional:
Create virtual environment and activate it

```bash
python3 -m venv .venv
. .venv/bin/activate
```

Install dependencies

```bash
  pip install -r /path/to/requirements.txt
```

Start the server

```bash
  python3 ./src/app.py
```