# what is "@dataclass"
# with "@dataclass"
from dataclasses import dataclass
@dataclass
class employee:
    emp_name:str
    age:int

# without "@dataclass"
class employee:
    def __init(self,emp_name,age):
        self.emp_name:emp_name
        self.age:age
##### git
'''
git config --global user.email "sanjayav8397@gmail.com"
git config --global user.name "Sanjay9783"
git add .
git commit -m "docker_update"
git push origin main
'''

###
'''
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
'''


##### steps for deployment #####
'''
step 1:- mogodb atlas, connect, my application-python 3.6
            connet mongodb ip address 0.0.0.0/0
         mongodb atlas url: 
            mongodb+srv://sanjay:sanjay@cluster0.ua1lgcn.mongodb.net/?retryWrites=true&w=majority
step 2:- insert dataset to mongodb atlas
step 3:-
        test code localy once after dumping data to mongodb atlas
step 4:- create 'Docker file'
        create 'start.sh'
        create 'docker-compose.yaml'
        create '.dockerignore'
        create 'training_pipeline.py,batch_prediction.py' file in new folder airflow/dags
        create 'main.yaml' in new folder .github/workflow

step 5:- set all secret keys to main.yaml file
        ---> from IAM aws
        AWS_ACCESS_KEY_ID = AKIA3FISYO36HEZM2KPJ
        AWS_SECRET_ACCESS_KEY = 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
        AWS_REGION = ap-south-1
        ---> from ECR aws
        AWS_ECR_LOGIN_URI = 767227885308.dkr.ecr.ap-south-1.amazonaws.com
        ECR_REPOSITORY_NAME = sensor-fault
        ---> from s3 aws
        BUCKET_NAME = aps-fault-sensor
        MONGO_DB_URL = mongodb+srv://sanjay:sanjay@cluster0.ua1lgcn.mongodb.net/?retryWrites=true&w=majority

    in aws create new user by searching-->IAM-->user-->add_user-->name-->admin_acess-->download csv

    in aws search 'ecr' -->repositry-->change location to mumbai at top corner--> create repo

    in aws search s3--> create bucket

step 6:- EC2 --> WE NEED TO CREATE

in aws ec2-->instances-->launch_instances-->give name, choose ubantu , create_key, Configure storage=30gb-->launch_instances
    select your instance-->security_tab-->click on security group-->in inbound rules--edit inbound rules-->add rule--chose all_traffic,anywhere-ipv4
    instance-->connect-->connect

step 7:-
    after step6  we will get a consol exicute code line by line to installdocker in aws-ubantu
    clear
    #curl -fsSL https://get.docker.com -o get-docker.sh
    #sudo sh get-docker.sh
    #sudo usermod -aG docker ubuntu
    #newgrp docker
    docker --version

step 8:-
    open project repop in github-->setings-->actions-->runners-->new self-hosted runner-->linux----
    ---> run commands below in ec2 machine one by one 
                    configure in github--
                        after first command -->enter -->type 'self-hosted'-->enter
                            √ Connected to GitHub

                            # Runner Registration

                            Enter the name of the runner group to add this runner to: [press Enter for Default] 
                                -->enter
                            Enter the name of runner: [press Enter for ip-172-31-45-106] self-hosted
                                -->self-hosted
                            This runner will have the following labels: 'self-hosted', 'Linux', 'X64' 
                            Enter any additional labels (ex. label-1,label-2): [press Enter to skip] 
                                -->enter
                            √ Runner successfully added
                            √ Runner connection is good

                            # Runner settings

                            Enter name of work folder: [press Enter for _work]
                                -->enter

                            Settings Saved.

                            ubuntu@ip-172-31-45-106:~/actions-runner$ ./run.sh

step 9:-
    github-->setings-->secrets-->actions-->new repo secret ----
            add one by one
        ---> AWS_ACCESS_KEY_ID = AKIA3FISYO36HEZM2KPJ
            AWS_SECRET_ACCESS_KEY = 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
            AWS_REGION = ap-south-1
            AWS_ECR_LOGIN_URI = 767227885308.dkr.ecr.ap-south-1.amazonaws.com
            ECR_REPOSITORY_NAME = sensor-fault
            BUCKET_NAME = aps-fault-sensor
            MONGO_DB_URL = mongodb+srv://sanjay:sanjay@cluster0.ua1lgcn.mongodb.net/?retryWrites=true&w=majority


step 10:- 
       if in github setings-->action-->runner--> 

cd actions-runner/
./config.sh --url https://github.com/Sanjay9783/aps-fault-detection --token A2FDSSDDGKGQOQ5QECDOFRLDUKENQ
./run.sh


'''