FROM python:3.9
ADD . .
WORKDIR .
RUN pip install -r requirements.txt
CMD python app.py
