FROM python:3

WORKDIR /home

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD python honeybot.py
