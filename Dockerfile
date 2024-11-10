FROM python:3.9

WORKDIR /test

COPY ./requirements.txt /test/requirements.txt

COPY ./.env /test/.env

COPY ./db.py /test/db.py

RUN pip install --no-cache-dir --upgrade -r /test/requirements.txt

COPY ./main.py /test/main.py

COPY ./api /test/api

COPY ./load /test/load

CMD ["python", "main.py"]
