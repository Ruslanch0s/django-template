FROM python:3.10

RUN apt-get update
RUN pip install --upgrade pip

#RUN mkdir "src"
WORKDIR /src

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD gunicorn -b 0.0.0.0:8000 config.wsgi:application