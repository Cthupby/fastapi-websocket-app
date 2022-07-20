# FastAPI WebSocket App  

## Технологии проекта:

1. Web-framework: [FastAPI](https://fastapi.tiangolo.com/), [Starlette](https://www.starlette.io/)
2. Database: [PostgreSQL](https://www.postgresql.org/)

## Установка и использование  

### При помощи [Docker](https://docs.docker.com/)
1. Необходимо скачать проект  
2. Создать образ проекта  
   ```docker build -t fastapi_ws .```  
3. Создать и активировать контейнер проекта  
   ```docker run -p 80:80 fastapi_ws```

### При помощи [Virtualenv](https://virtualenv.pypa.io/en/latest/)
1. Необходимо скачать проект  
2. Создать и активировать виртуальное окружение  
   ```python -m virualenv venv```  
   ```source ./venv/bin/activate```
3. Установить рекомендуемые библиотеки  
   ```pip install --no-cache-dir --upgrade -r /fastapi_ws/requirements.txt```
4. Запустить проект  
   ```"uvicorn app.main:app --host 0.0.0.0 --port 80```  
