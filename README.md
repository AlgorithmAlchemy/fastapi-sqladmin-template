# SQLAdmin - CRUD Admin

The project is a **FastAPI**-based REST API application with **SQLAlchemy** and **SQLAdmin** integration, featuring automatic table generation and a CRUD interface for all models.

<p align="left">
  <img src="https://github.com/user-attachments/assets/96da0139-453a-4d16-96c1-4dbe547aa3f0" alt="dd_DeWatermark" height="450" width="600" />
</p>

## Features

* CRUD support for models: `Product`, `Category`, `User`
* Integrated SQLAdmin panel
  Automatic table creation on startup
* OpenAPI documentation available at `/docs`
* Authentication via `User` model (optional)

## Project Structure

```bash
.
├── app/
│   ├── models/        # SQLAlchemy models
│   ├── schemas/       # Pydantic schemas
│   ├── admin/         # SQLAdmin configuration
│   ├── crud/          # CRUD operations
│   └── main.py        # Entry point
├── requirements.txt
└── README_en.md
```

## Models

* `Product`: id, name, category_id, description, changelog
* `Category`: id, name
* `User`: id, username, email

## Installation

```bash
git clone https://github.com/AlgorithmAlchemy/fastapi-sqladmin-template
cd fastapi-sqladmin-template
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Dependencies

* [FastAPI](https://fastapi.tiangolo.com/)
* [SQLAlchemy](https://www.sqlalchemy.org/)
* [SQLAdmin](https://sqladmin.readthedocs.io/)
* [Uvicorn](https://www.uvicorn.org/)

## Admin Panel

```
http://127.0.0.1:8000/admin
```

## API Documentation

```
http://127.0.0.1:8000/docs
```
