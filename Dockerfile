FROM python:3.9-slim-bookworm

WORKDIR /finance

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . /finance

CMD ["/bin/sh", "run.sh"]