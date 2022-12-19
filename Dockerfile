### creating docker image
# base image
FROM python:3.8
# make ourself as root user
USER root
# make folder to copl all files to a folder
RUN mkdir /app
# copy all items to that folder
COPY . /app/
# set working directory
WORKDIR /app/
# install dependency
RUN pip3 install -r requirements.txt
# set envirnoment to air flow
ENV AIRFLOW_HOME="/app/airflow"
ENV AIRFLOW__CORE__DAGBAG_IMPORT_TIMEOUT=1000
ENV AIRFLOW__CORE__ENABLE_XCOM_PICKLING=True
# initilize airflow
RUN airflow db init
# creat airflow login creadintials -e=email ,-f=first_name ,-l=last_name, -p=password ,-r=rool,-u=username
RUN airflow users create  -e sanjayav8397@gmail.com -f sanjay -l AV -p admin -r Admin  -u admin
# give permission to start.sh
RUN chmod 777 start.sh
# install awscli = aws command line interface
RUN apt update -y && apt install awscli -y
ENTRYPOINT [ "/bin/sh" ]
CMD ["start.sh"]