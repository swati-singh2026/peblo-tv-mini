# Project Notes

## Project

Peblo TV Mini

## Tech Stack

- FastAPI
- PostgreSQL
- React (Vite)
- TypeScript
- Docker
- SQLAlchemy
- Alembic

---

# Progress Log

## Phase 1 – Project Setup ✅

### Completed

- Repository structure created
- Backend (FastAPI) initialized
- CMS (React + Vite) initialized
- Viewer (React + Vite) initialized
- Docker Compose configured
- PostgreSQL container configured
- SQLAlchemy database connection established
- Environment configuration added (.env)
- Health endpoint implemented
- Swagger API configured

### Status

- Backend running successfully
- PostgreSQL connected
- Docker working correctly
- Project foundation completed

---

## Phase 2 – Database Design ✅

### Completed

- SQLAlchemy Base configured
- Database session created
- Show model implemented
- Season model implemented
- Episode model implemented
- Relationships established
  - Show → Seasons
  - Season → Episodes

- Alembic initialized
- Alembic configured with SQLAlchemy metadata
- Initial migration generated
- Database schema migrated successfully

### Status

Database tables created:

- shows
- seasons
- episodes
- alembic_version

Database schema verified using PostgreSQL.

---

## Phase 3 – Seed Data Import ✅

### Completed

- Added assignment seed data
- Added reference.json
- Created seed import script (`init_db.py`)
- Parsed JSON records
- Imported Shows
- Imported Seasons
- Imported Episodes
- Verified imported data

### Import Summary

- Shows: **8**
- Seasons: **10**
- Episodes: **95**

### Status

Seed database imported successfully.

---

# Issues Encountered

## Issue 1

### Problem

Docker daemon was not running.

### Error

```text
failed to connect to docker API
```

### Resolution

Started Docker Desktop and verified the PostgreSQL container was running.

---

## Issue 2

### Problem

Database authentication failed.

### Error

```text
password authentication failed for user
```

### Root Cause

Backend `.env` credentials did not match the PostgreSQL Docker configuration.

### Resolution

Updated `DATABASE_URL` to match Docker PostgreSQL credentials.

---

## Issue 3

### Problem

Unable to use PostgreSQL client.

### Error

```text
psql is not recognized
```

### Root Cause

PostgreSQL client was not installed locally.

### Resolution

Verified database directly using the PostgreSQL Docker container.

---

## Issue 4

### Problem

Alembic generated empty configuration.

### Root Cause

Alembic files were manually created instead of using the initialization command.

### Resolution

Reinitialized Alembic using:

```bash
alembic init alembic
```

Configured `env.py` and `alembic.ini` correctly.

---

## Issue 5

### Problem

Alembic migration was not detecting models.

### Root Cause

SQLAlchemy models were not imported into Alembic metadata.

### Resolution

Imported all models inside `alembic/env.py` and configured:

```python
target_metadata = Base.metadata
```

---

## Issue 6

### Problem

Seed data import failed initially.

### Root Cause

Incorrect JSON path and incomplete import script.

### Resolution

Corrected file path, completed import logic, and verified successful database insertion.

---

# Key Decisions

- Use Dockerized PostgreSQL instead of a local installation.
- Use SQLAlchemy ORM with Alembic migrations.
- Keep Backend, CMS, and Viewer as separate applications.
- Store configuration using environment variables.
- Import assignment seed data before API development.
- Use one database session for bulk seed import.

---

# Current Status

## Completed

- Project setup
- Docker configuration
- PostgreSQL integration
- SQLAlchemy models
- Database relationships
- Alembic migrations
- Database schema creation
- Seed data import
- Swagger API

## Database

- 8 Shows
- 10 Seasons
- 95 Episodes

Backend is stable and ready for API development.

---

# Next Tasks

- Phase 4 – Pydantic Schemas
- Phase 5 – CRUD APIs
- Phase 6 – Artwork Upload & Validation
- Phase 7 – Authentication & Roles
- Phase 8 – Publish Pipeline
- Phase 9 – Catalog APIs
- Phase 10 – Validation Report
- Phase 11 – CMS React
- Phase 12 – Viewer React
- Phase 13 – Testing
- Phase 14 – Docker & GitHub Actions
- Phase 15 – Final README & Demo Video
