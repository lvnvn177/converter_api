FROM python:3.9

WORKDIR /test

COPY ./requirements.txt /test/requirements.txt

COPY ./.env /test/.env

COPY ./db.py /test/db.py

COPY ./db /test/db

RUN pip install --no-cache-dir --upgrade -r /test/requirements.txt

COPY ./main.py /test/main.py

COPY ./api /test/api

COPY ./load /test/load

COPY ./test.py /test/test.py

COPY ./2304.01852v4_22.pdf /test/2304.01852v4_22.pdf

CMD ["python", "main.py"]