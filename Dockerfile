#
FROM python:latest

#
LABEL maintainer="ericghoubiguian@live.fr"

#
COPY . /time_calculous_with_Flask_restx

#
WORKDIR /time_calculous_with_Flask_restx

#
RUN apt upgrade -y && apt update -y

#
RUN apt install python3-pip -y

#
RUN pip3 install -r requirements.txt

#
EXPOSE 5000

#
ENTRYPOINT ["python3", "main.py"]