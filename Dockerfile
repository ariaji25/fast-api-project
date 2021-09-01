FROM python:3.8

RUN mkdir /ludes-be

WORKDIR /ludes-be

ADD requierments.txt /ludes-be/

ADD .env /ludes-be/

RUN pip install -r requierments.txt

ADD . /ludes-be/
