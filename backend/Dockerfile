FROM python:3.11

COPY ./app/ .

COPY ./requirements.txt /requirements.txt

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
