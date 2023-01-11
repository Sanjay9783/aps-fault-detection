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

### git
'''
git config --global user.email "sanjayav8397@gmail.com"
git config --global user.name "Sanjay9783"
git add .
git commit -m "airflow-update"
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
''' class = 11 dec
step 1:- mogodb atlas (dumping data to mongodb web)
            connect-->my application-->python 3.6
            # connet mongodb ip address 0.0.0.0/0
            # copy mongodb atlas url
            mongodb atlas url: mongodb+srv://sanjay:sanjay@cluster0.ua1lgcn.mongodb.net/?retryWrites=true&w=majority
                insert dataset to mongodb atlas (by running data_dump.py)
                # test code localy once after dumping data to mongodb atlas

step 2:-create 'Docker file' (time = 1.49 - 2.01)
        create 'start.sh'
        create 'docker-compose.yaml'
        create '.dockerignore'
        create 'training_pipeline.py,batch_prediction.py' file in new folder airflow/dags (time = 2.02 - 2.16)
        create 'main.yaml' in new folder .github/workflow (time = 2.16 - 2.38)

step 3:- set all secret keys required for main.yaml file
        ---> from IAM aws
            AWS_ACCESS_KEY_ID = AKIA3FISYO36MAV3YRAA
            AWS_SECRET_ACCESS_KEY = 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
        ---> from ECR aws
            AWS_ECR_LOGIN_URI = 767227885308.dkr.ecr.ap-south-1.amazonaws.com/
            ECR_REPOSITORY_NAME = sensor_fault
        ---> from s3 aws
            BUCKET_NAME = aps-fault-sensor
        AWS_REGION = ap-south-1
        MONGO_DB_URL = mongodb+srv://sanjay:sanjay@cluster0.ua1lgcn.mongodb.net/?retryWrites=true&w=majority

    in aws create new user by searching-->IAM (time  = 2.45)
        -->user-->add_user-->give_name + access_key-->(attach existing policies directly)AdministratorAcess-->download csv
                inside downloaded csv we will get = (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION)
    in aws search 'ecr' (time = 2.56)
        -->repositry-->change location to mumbai at top corner--> create repo (ap-south-1)
                after creating repo copy repo url (767227885308.dkr.ecr.ap-south-1.amazonaws.com/sensor_fault)
                    in url we will get = (AWS_ECR_LOGIN_URI,ECR_REPOSITORY_NAME)
    in aws search s3 (time = 3.00 - 3.02)
        --> buckets --> create bucket

step 4:- EC2 --> WE NEED TO CREATE EC2 machine (time = 3.04.50 - 3.19 )
    in aws search ec2
        --->instances-->launch_instances-->give name, choose ubuntu, create_key(Create new key pair-->give name), Configure storage=30gb-->launch_instances
        --->select your created instance-->security-->click on 'security groups'-->in 'inbound rules'-->Edit inbound rules-->'Add rule'-->choose ('All traffic','Anywhere-ipv4')-->save_rules
        --->select your created instance-->instance-->connect-->connect--> it will open new tab 'EC2 Instance Connect'

step 5:-(time = 3.19 - 3.25)
    after step4  we will get a consol/tab('EC2 Instance Connect') exicute below code line by line to installdocker in aws-ubantu 
        -->clear
        -->curl -fsSL https://get.docker.com -o get-docker.sh
        -->sudo sh get-docker.sh
        -->sudo usermod -aG docker ubuntu
        -->newgrp docker
        -->docker --version

step 6:-(time = 3.25 - )
    open project repop in github-->setings-->actions-->runners-->'New self-hosted runner'-->linux----
    ---> run commands below in ec2 machine one by one
            ---> code in 'Download' tab
            ---> code in 'Configure' tab
                    after pasting 1st code hit--->enter (./config.sh --url https://github.com/Sanjay9783/aps-fault-detection --token A2FDSSFZOT4MNIKOJ7IB6SDDX2KOM)
                        √ Connected to GitHub
                        # Runner Registration
                        -->Enter the name of the runner group to add this runner to: [press Enter for Default] --> enter
                        -->Enter the name of runner: [press Enter for ip-172-31-45-106] -->'self-hosted'
                        This runner will have the following labels: 'self-hosted', 'Linux', 'X64' 
                        -->Enter any additional labels (ex. label-1,label-2): [press Enter to skip] -->enter
                        √ Runner successfully added
                        √ Runner connection is good
                        # Runner settings
                        -->Enter name of work folder: [press Enter for _work]-->enter
                        Settings Saved.
                    second code in configure "./run.sh"

step 7:-(time ends = 3.50)
    github-->setings-->secrets and variables-->actions-->new repo secret ----
            add one by one
        --->AWS_ACCESS_KEY_ID = AKIA3FISYO36MAV3YRAA
            AWS_SECRET_ACCESS_KEY = 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
            AWS_REGION = ap-south-1
            AWS_ECR_LOGIN_URI = 767227885308.dkr.ecr.ap-south-1.amazonaws.com/
            ECR_REPOSITORY_NAME = sensor_fault
            BUCKET_NAME = aps-fault-sensor
            MONGO_DB_URL = mongodb+srv://sanjay:sanjay@cluster0.ua1lgcn.mongodb.net/?retryWrites=true&w=majority

step 8:- 
        if in github setings-->action-->runner(ofline)
            in EC2 instance Connect (tab/consol) run below code
                -->cd actions-runner
                -->./run.sh)

./config.sh --url https://github.com/Sanjay9783/aps-fault-detection --token A2FDSSDDGKGQOQ5QECDOFRLDUKENQ

step 9:-
        to check deployment is done or not
        in ec2 consol --> docker ps

        in ec2 instance copy link:
        https://ec2-13-233-140-101.ap-south-1.compute.amazonaws.com/
        change 
        http://ec2-13-233-140-101.ap-south-1.compute.amazonaws.com:8080
        itwill pop up airflow

'''