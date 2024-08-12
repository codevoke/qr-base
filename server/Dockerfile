FROM python:3.10

WORKDIR /server

COPY requirements.txt /server

RUN pip install -r requirements.txt

COPY . /server

EXPOSE 8080

CMD ["flask", "run", "--port", "8080"]