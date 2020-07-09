# Шаблон проекта на Flask

> Tagline
>
> [![](https://img.shields.io/badge/some-badge-lightblue)](https://shields.io 'Badges website')

## Стек технологий

#### Backend
- python3
- Flask + addons
- SQLAlchemy ORM
- MVC pattern

#### Frontend
- HTML5
- CSS3
- JS

## Инструкция по запуску

1. Склонируйте репозиторий и перейдите в директорию с проектом
    ```
    git clone <link>
    cd <project_directory>
    ```
    
2. Создайте и активируйте виртуальное окружение
    ```
    virtualenv --python=python3 venv
    source venv/bin/activate
    ```

3. Установите зависимости
    ```
    pip3 install -r requirements.txt
    ```

4. Создайте таблицы в БД
    ```
    python3 manage.py db_reset
    ```

5. Запустите веб-приложение
    ```
    python3 manage.py runserver
    ```
   
## Полезные команды

1. Генерация папки migrations (в случае её отсутствия)
    ```
    python3 manage.py db init
    ```

2. Создание новой миграции
    ```
    python3 manage.py db migrate -m "comment"
    ``` 

3. Обновление архитектуры БД до определённой миграции
    ```
    python3 manage.py db upgrade <migration>
    ```  

4. Откат архитектуры БД до определённой миграции
    ```
    python3 manage.py db downgrade <migration>
    ```  
   
5. Просмотр информации о текущей миграции 
    ```
    python3 manage.py db current
    ```
   
6. Просмотр списка миграций
    ```
    python3 manage.py db history
    ``` 
   
7. Удаление БД и всех миграций
    ```
    python3 manage.py db_delete
    ```
   
8. Сброс данных в БД
    ```
    python3 manage.py db_reset
    ```  
   
Разработано [кем-то](https://exmaple.com 'hover comment')
