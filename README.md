# Candidates API

A FastAPI-based REST API for candidate management and analysis with PostgreSQL integration.

## Features

- Unemployment candidate analysis
- Location-based statistics
- Notification system
- Scalable and maintainable architecture
- Automatic Swagger documentation

## Prerequisites

- Python 3.11+
- PostgreSQL 14+
- virtualenv or similar

## Installation

1. Clone the repository:

2. Create and activate virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create `.env` file in the project root:
```env
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
POSTGRES_SERVER=localhost
POSTGRES_DB=candidates_db
```

5. Initialize the database:
```bash
# Create database in PostgreSQL
psql -U postgres -p 5433
CREATE DATABASE candidates_db;
\q

# Run migrations
alembic upgrade head
```

## Running the Application

1. Start the development server:
```bash
uvicorn main:app --reload
```

2. Access the documentation:
- Swagger UI: http://localhost:8000/docs

## Main Endpoints

### Candidate Analysis
```
GET /api/v1/candidates/analyze/
```
Returns:
- Total unemployed candidates
- Location with most unemployed candidates
- Number of candidates in that location
- Analysis timestamp

## Database Management

### Create new migration
```bash
alembic revision --autogenerate -m "Change description"
```

### Apply migrations
```bash
alembic upgrade head
```

### Rollback last migration
```bash
alembic downgrade -1
```

## Development

### Architecture

The project follows a layered architecture:
1. **API Layer**: Request/Response handling
2. **Service Layer**: Business logic
3. **Repository Layer**: Data access
4. **Database Layer**: Models and DB connection

### Code Conventions

- Follow PEP 8
- Google-style docstrings
- Type hints for all functions
- Tests for new functionality

## Testing

Run tests:
```bash
pytest
```

## API Documentation

The API documentation is automatically generated and can be accessed at:

- `/docs` - Swagger UI documentation

