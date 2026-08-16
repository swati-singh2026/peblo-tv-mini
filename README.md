# Peblo TV Mini

Take-home challenge for Peblo.

## Tech Stack

- FastAPI
- PostgreSQL
- React
- TypeScript
- Docker
- SQLAlchemy
- Alembic

---

# Project Structure

```text
peblo-tv-mini/
├── backend/                 # FastAPI Backend
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── db/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── scripts/
│   │   └── data/
│   ├── alembic/
│   ├── alembic.ini
│   └── requirements.txt
│
├── cms/                     # React CMS
├── viewer/                  # React Viewer
├── docker-compose.yml
├── .env.example
└── README.md
```

---

# Setup

## 1. Clone Repository

```bash
git clone <repository-url>
cd peblo-tv-mini
```

---

## 2. Start PostgreSQL

```bash
docker compose up -d
```

---

## 3. Configure Environment

Create `backend/.env`

```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/peblo_tv

SECRET_KEY=supersecretkey
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## 4. Start Backend

```bash
cd backend

python -m venv .venv

# Windows
.venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Backend:

```
http://127.0.0.1:8000
```

Swagger Docs:

```
http://127.0.0.1:8000/docs
```

---

# Database

The application uses PostgreSQL with SQLAlchemy ORM and Alembic migrations.

Current schema:

- Shows
- Seasons
- Episodes

Relationships:

```
Show
 └── Season
      └── Episode
```

Migration:

```bash
alembic upgrade head
```

---

# Seed Data

Seed data provided with the assignment can be imported using:

```bash
python -m app.scripts.init_db
```

Imported successfully:

- Shows: **8**
- Seasons: **10**
- Episodes: **95**

---

# Progress

## ✅ Completed

### Phase 1 — Project Setup

- Repository setup
- FastAPI backend initialization
- React (Vite) CMS setup
- React (Vite) Viewer setup
- Docker Compose configuration
- PostgreSQL integration
- Health endpoint
- Environment configuration

### Phase 2 — Database Design

- SQLAlchemy models
- Model relationships
- Database session
- Alembic configuration
- Initial migration
- PostgreSQL schema generation

### Phase 3 — Seed Data Import

- Added assignment seed data
- JSON import script
- Database population
- Import verification

---

# Current Status

- ✅ FastAPI backend running
- ✅ PostgreSQL running in Docker
- ✅ Database connected
- ✅ Alembic configured
- ✅ Initial migration completed
- ✅ Database schema created
- ✅ Seed data imported
- ✅ Swagger API documentation available

---

# Issues Encountered

| Issue                                 | Resolution                                                          |
| ------------------------------------- | ------------------------------------------------------------------- |
| PostgreSQL authentication failure     | Updated database credentials in `.env` and `docker-compose.yml`.    |
| Alembic generated empty configuration | Reinitialized Alembic using `alembic init` and configured `env.py`. |
| Migration not detecting models        | Imported SQLAlchemy models into Alembic metadata.                   |
| Seed data import path issue           | Corrected JSON file location and import script.                     |

---

# Upcoming Work

- Pydantic Schemas
- CRUD APIs
- Artwork Upload & Validation
- Authentication & Role-based Access
- Publish Pipeline
- Catalog APIs
- Validation Report
- CMS (React)
- Viewer (React)
- Testing
- Docker Compose (Full Stack)
- GitHub Actions
- Final README
- Demo Video

---

# License

Developed as part of the **Peblo TV Mini Take-Home Challenge**.
