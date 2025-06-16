
# 🧩 - CRUD Admin

Проект — это REST API-приложение на базе **FastAPI** с интеграцией **SQLAlchemy**, **SQLAdmin**, поддержкой автогенерации таблиц и CRUD-интерфейса для всех моделей.


<p align="left">
  <img src="https://github.com/user-attachments/assets/96da0139-453a-4d16-96c1-4dbe547aa3f0" alt="dd_DeWatermark" width="700" />
</p>


## 🚀 Возможности

- 📦 CRUD для моделей: `Product`, `Category`, `User`
- 🧾 Поддержка SQLAdmin панели
- ⚙️ Автоматическое создание таблиц при запуске
- 📝 Документация OpenAPI (`/docs`)
- 🔒 Аутентификация через `User` модель (при необходимости)

## 📁 Структура

```bash
.
├── app/
│   ├── models/        # SQLAlchemy модели
│   ├── schemas/       # Pydantic схемы
│   ├── admin/         # SQLAdmin конфигурация
│   ├── crud/          # CRUD-операции
│   └── main.py        # Точка входа
├── requirements.txt
└── README.md
````

## 🧱 Модели

* `Product`: id, name, category\_id, description, changelog
* `Category`: id, name
* `User`: id, username, email

## 🔧 Установка

```bash
git clone https://github.com/твой-юзер/твой-репо.git
cd твой-репо
python -m venv venv
source venv/bin/activate  # или .\venv\Scripts\activate на Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## 🛠 Зависимости

* [FastAPI](https://fastapi.tiangolo.com/)
* [SQLAlchemy](https://www.sqlalchemy.org/)
* [SQLAdmin](https://sqladmin.readthedocs.io/)
* [Uvicorn](https://www.uvicorn.org/)

## 🗂 Панель администратора

После запуска доступна по адресу:

```
http://127.0.0.1:8000/admin
```

## 📜 Документация API

Доступна по адресу:

```
http://127.0.0.1:8000/docs
```

## 📋 Changelog

Изменения проекта документируются в [CHANGELOG.md](./CHANGELOG.md).


Этот проект лицензирован под MIT. См. файл [LICENSE](./LICENSE).

```
 
---

Хочешь — могу добавить бейджи (CI, релиз, версия, license), автогенерацию документации, CI/CD pipeline или шаблон issue/PR.
```
