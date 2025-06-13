# Changelog

Все заметные изменения в этом проекте будут документироваться в этом файле.

Формат основан на [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
и этот проект использует [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Добавлено
- Поля `description` и `changelog` в модель `Product`
- Поддержка `ModelView` для `Category` и `User` в admin-панели
- CRUD-интерфейс для всех моделей
- Автоматическое создание таблиц при запуске приложения

### Удалено
- Устаревшие декораторы `@app.on_event` (подлежит замене на lifespan)

---

## [0.1.0] - 2025-06-13

### Добавлено
- Инициализация проекта на FastAPI
- Модель `Product` с полями `id`, `name`, `category_id`
- Модель `Category` и `User`
- SQLAdmin-панель для модели `Product`

