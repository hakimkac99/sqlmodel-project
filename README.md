# sqlmodel-project

This is a demo app : FastAPI + SQLModel

### Run the app using PostgreSQL + pgAdmin

- Update app/db.py file (uncomment the posgresql config) then run :

`sudo docker compose up --build -d`

- If you want to access pgAdmin, go to `http://localhost:5050/` and connect with the username : "admin@admin.com" an password : "root".

- Get the database server IP address of the running db container :

`docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' db_container`

- Create a new server with the right IP address and Database credentials (postgres:postgres)

- Access to the app docs : `http://localhost:8000/docs`

### Run the app using sqllite

- Simply run `uvicorn app.main:app --reload`

### Running tests (in memory)

- pytest app

### Running Alembic migrations

- generate migrations : `alembic revision --autogenerate -m "revision name"`
- upgrade to the new revision : `alembic upgrade <revision>`
- show history : `alembic history`
- downgrade to an old revision `alembic downgrade <revision>`
