# Домашнее задание к лекции «Python и БД. ORM»
## Задание 1
Составить модели классов SQLAlchemy по заданной схеме, реализация приведена в файле models.py
## Задание 2
Используя SQLAlchemy, составить запрос выборки магазинов, продающих целевого издателя.

Напишите Python-скрипт, который:

подключается к БД любого типа на ваш выбор, например, к PostgreSQL;
импортирует необходимые модели данных;
принимает имя или идентификатор издателя (publisher), например, через input(). Выводит построчно факты покупки книг этого издателя в виде форматированной таблицы. Это задание реализовано в файле main.py
## Задание 3
Заполните БД тестовыми данными.

Тестовые данные берутся из папки fixtures. Пример содержания в JSON-файле.

Возможная реализация: прочитать JSON-файл, создать соотведствующие экземляры моделей и сохранить в БД.
Реализация этого задания приведена в файле main.py в функции load_test_data()