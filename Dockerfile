FROM python:3.9.2
WORKDIR .
RUN apt-get update
RUN apt-get upgrade -y
RUN pip install -r requirements.txt

