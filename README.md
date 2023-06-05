# Тестовое задание
Данный проект использует предобученную модель для классификации обьектов на картинке.
## Установка

1) `git clone https://github.com/margulanz/bu.git`
2) `cd bu`
3) `python -m venv venv`
4) `.\venv\scripts\activate`
5) `python -m pip install -r requirements.txt`

## Запуск проекта
`uvicorn src.main:app --reload`

## Эндпойнты

1) POST `/images/` -> загружает изображение
2) GET `/images/id` -> получает информацию о изображении и результат классификации 

## Запуск тестов
`pytest tests/tests.py`

## *
Все эндпойнты можно протестировать самому через `http://localhost:8000/docs`
