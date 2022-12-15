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