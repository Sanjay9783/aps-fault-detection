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
git config --global user.email "sanjayav8397@gmail.com"
git config --global user.name "Sanjay9783"
git add .
git commit -m "fgsfh"
git push origin main


##### steps for deployment #####
step 1:- mogodb atlas, connect, my application-python 3.6
         mongodb atlas url: 
            mongodb+srv://sanjay:sanjay@cluster0.ua1lgcn.mongodb.net/?retryWrites=true&w=majority
step 2:- insert dataset to mongodb atlas
step 3:-
        test code localy once after dumping data to mongodb atlas
step 4:- create 'Docker file'
        create 'start.sh'
        create 'docker-compose.yaml'
        create '.dockerignore'
        create airflow/dags folder

           