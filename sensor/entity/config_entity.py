import os,sys
from sensor.exception import SensorException
from sensor.logger import logging
from datetime import datetime

'''
there are main 6 steps in this project 
    1-DataIngestion
    2-DataValidation
    3-DataTransformation
    4-ModelTrainer
    5-ModelEvaluation
    6-ModelPusher

this file will act as in put file for each and every step
'''

FILE_NAME = "sensor.csv"
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"

class TrainingPipelineConfig:

    def __init__(self):
        try:
            self.artifact_dir = os.path.join(os.getcwd(),"artifact",f"{datetime.now().strftime('%m%d%Y__%H%M%S')}")
        except Exception  as e:
            raise SensorException(e,sys)     


class DataIngestionConfig:

    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        '''
        input for data_ingetion.py file it will fetch input from hear
        '''
        try:
            self.database_name="aps"
            self.collection_name="sensor"
            # creating main direcory for storing data from database and test, train data
            self.data_ingestion_dir = os.path.join(training_pipeline_config.artifact_dir , "data_ingestion")
            # storing directory for data imported from database "data_ingestion/feature_store/"
            self.feature_store_file_path = os.path.join(self.data_ingestion_dir,"feature_store",FILE_NAME)
            # directory for staoring train and test data "data_ingestion/dataset/"
            self.train_file_path = os.path.join(self.data_ingestion_dir,"dataset",TRAIN_FILE_NAME)
            self.test_file_path = os.path.join(self.data_ingestion_dir,"dataset",TEST_FILE_NAME)
            self.test_size = 0.2
        except Exception  as e:
            raise SensorException(e,sys)     

    def to_dict(self,)->dict:
        try:
            return self.__dict__
        except Exception  as e:
            raise SensorException(e,sys)     

class DataValidationConfig:...
class DataTransformationConfig:...
class ModelTrainerConfig:...
class ModelEvaluationConfig:...
class ModelPusherConfig:...