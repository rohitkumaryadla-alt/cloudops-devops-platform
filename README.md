# cloudops-devops-platform

CloudOps DevOps Platform is a FastAPI service for managing users. The API stores user records in MySQL when run with Docker Compose and exposes interactive OpenAPI documentation.

## Features

- Create, list, retrieve, update, and delete users.
- Validate user email addresses and prevent duplicate emails.
- Expose a health check and interactive Swagger UI.
- Run API and MySQL services together with Docker Compose.
- Run automated tests against an isolated in-memory SQLite database.

## Technology

- Python 3.12
- FastAPI and Uvicorn
- SQLAlchemy and PyMySQL
- MySQL 8.0
- pytest

## Running with Docker

Prerequisites: Docker with the Docker Compose plugin.

Start the application:

```bash
docker compose up --build
```

Run in detached mode:

```bash
docker compose up --build -d
```

Check containers:

```bash
docker compose ps
```

View API logs:

```bash
docker compose logs api
```

View MySQL logs:

```bash
docker compose logs mysql
```

Stop the application:

```bash
docker compose down
```

The MySQL data is stored in the `mysql_data` Docker volume and is retained when the containers are stopped with `docker compose down`.

API: [http://localhost:8000](http://localhost:8000)

Swagger: [http://localhost:8000/docs](http://localhost:8000/docs)

Health: [http://localhost:8000/health](http://localhost:8000/health)

The credentials in `docker-compose.yml` are development defaults; replace them before using this configuration in a production environment.

## API Endpoints

| Method | Path | Description | Typical response |
| --- | --- | --- | --- |
| `GET` | `/` | API welcome message | `200 OK` |
| `GET` | `/health` | Health status | `200 OK` |
| `POST` | `/api/users` | Create a user | `201 Created`; `409 Conflict` for duplicate email; `422` for invalid input |
| `GET` | `/api/users` | List users | `200 OK` |
| `GET` | `/api/users/{user_id}` | Retrieve a user | `200 OK`; `404 Not Found` if absent |
| `PUT` | `/api/users/{user_id}` | Replace a user's name and email | `200 OK`; `404 Not Found` if absent |
| `DELETE` | `/api/users/{user_id}` | Delete a user | `204 No Content`; `404 Not Found` if absent |

Create-user request body:

```json
{
	"name": "Ada Lovelace",
	"email": "ada@example.com"
}
```

## Running Locally

Local API execution requires Python 3.12 and a reachable MySQL database. The following starts the Compose MySQL service, then runs the API using the host-published MySQL port.

```powershell
docker compose up -d mysql
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
$env:DATABASE_URL = "mysql+pymysql://cloudops:cloudopspassword@localhost:3306/cloudops"
python -m uvicorn app.main:app --reload
```

For a POSIX shell, activate the environment with `source .venv/bin/activate` and set `DATABASE_URL` to the equivalent MySQL URL before starting Uvicorn.

## Tests

The pytest configuration sets `DATABASE_URL` to in-memory SQLite, so the tests do not require the MySQL container.

```powershell
python -m pytest -v
```

Alternatively, run the repository test script:

```powershell
.\scripts\run-tests.ps1
```

## Project Layout

```text
app/                FastAPI application, routes, schemas, and database models
docker/             API Dockerfile
tests/              API tests and pytest database configuration
scripts/            Test runner scripts
cloudformation/     Reserved for AWS CloudFormation templates
terraform/          Reserved for Terraform configuration
lambda/             Reserved for AWS Lambda code
docker-compose.yml  Local API and MySQL services
requirements.txt    Python dependencies
```

The CloudFormation, Terraform, and Lambda directories are placeholders; no deployment templates or Lambda handlers are currently included. The application creates its SQLAlchemy tables at startup; a database migration framework is not currently configured.

