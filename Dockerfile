FROM python:latest

COPY main.py /
COPY channels.json /
COPY requirements.txt /

RUN pip3 install -r requirements.txt

CMD [ "python", "./main.py" ]
