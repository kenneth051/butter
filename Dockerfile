FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .
RUN chmod +x ./docker-entrypoint.sh
EXPOSE 8000