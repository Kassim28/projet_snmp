FROM python:3.9.2
WORKDIR .
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install librrd-dev libpython3-dev -y
RUN pip install -r requirements.txt
CMD export FLASK_APP=NMS.py
CMD flask run -p 8001
