FROM python:latest

COPY main.py /

RUN pip3 install -r requirements.txt

CMD [ "python", "./main.py" ]
