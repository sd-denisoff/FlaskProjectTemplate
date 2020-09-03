# Flask Project Template

> [![](https://i.postimg.cc/7PQfGGH4/PPn-P-logo.png)](https://ppnp.me 'official team website')
>
> [![](https://img.shields.io/badge/PM%26BA-Pavel%20Krylov-lightgrey)](https://vk.com/pkryloff 'VK profile')
> [![](https://img.shields.io/badge/UX%2FUI-Leonid%20Kravtsov-green)](https://vk.com/kravtsovjr 'VK profile')
> [![](https://img.shields.io/badge/backend-Stepan%20Denisov-lightblue)](https://vk.com/sd.denisoff 'VK profile')
> [![](https://img.shields.io/badge/frontend-Matvey%20Kottsov-orange)](https://vk.com/kottsovcom 'VK profile')
> [![](https://img.shields.io/badge/DS%2FML-Denis%20Kozlov-blue)](https://vk.com/dkozl 'VK profile')

## Technology stack

#### Backend
- python3
- Flask + addons
- SQLAlchemy ORM
- MVC pattern

#### Frontend
- HTML5
- CSS3
- JS

## Launch instruction

1. Clone the repository and change the directory
    ```
    git clone <link>
    cd <project_directory>
    ```
    
2. Create a virtual environment and activate it
    ```
    virtualenv --python=python3 venv
    source venv/bin/activate
    ```

3. Install dependencies
    ```
    pip3 install -r requirements.txt
    ```

4. Create tables in the database
    ```
    python3 manage.py db_reset
    ```

5. Launch web application
    ```
    python3 runner.py
    ```
   
## Useful commands

1. Generate migrations folder (if does not exists)
    ```
    python3 manage.py db init
    ```

2. Create new migration
    ```
    python3 manage.py db migrate -m "comment"
    ``` 

3. Update database architecture to a specific migration
    ```
    python3 manage.py db upgrade <migration>
    ```  

4. Rollback of database architecture to a specific migration
    ```
    python3 manage.py db downgrade <migration>
    ```  
   
5. View current migration info
    ```
    python3 manage.py db current
    ```
   
6. View migrations list
    ```
    python3 manage.py db history
    ``` 
   
7. Remove a database and all migrations
    ```
    python3 manage.py db_delete
    ```
   
8. Reset data in the database
    ```
    python3 manage.py db_reset
    ```  

Developed by [PPnP Team](https://ppnp.me 'official team website')
