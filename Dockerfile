FROM python:3.9.2
ADD . .
WORKDIR .
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install librrd-dev libpython3-dev -y
RUN pip install -r requirements.txt
CMD python NMS.py
