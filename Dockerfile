FROM python
ADD . .
WORKDIR .
RUN pip install -r requirements.txt
CMD python app.py
