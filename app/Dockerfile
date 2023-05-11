FROM ubuntu:latest as lss

ENV LSS_ACCESS_KEY="lssaccess"

ENV LSS_PASSWORD_KEY="lsspassword"

RUN apt-get update

RUN apt-get install -y python3 python3-pip

COPY . ./app

RUN pip install -r app/requirements.txt

EXPOSE 6250

CMD [ "python3", "app/main.py" ]