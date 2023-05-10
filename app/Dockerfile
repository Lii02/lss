FROM ubuntu:latest as lss

RUN apt-get update

RUN apt-get install -y python3 python3-pip

COPY . ./app

RUN pip install -r app/requirements.txt

EXPOSE 6250

CMD [ "python3", "app/main.py" ]