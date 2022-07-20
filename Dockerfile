FROM python:3.9

WORKDIR /fastapi_ws

COPY ./requirements.txt /fastapi_ws/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /fastapi_ws/requirements.txt

COPY ./app /fastapi_ws/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
