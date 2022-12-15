from dataclasses import dataclass

'''
there are main 6 steps in this project 
    1-DataIngestion
    2-DataValidation
    3-DataTransformation
    4-ModelTrainer
    5-ModelEvaluation
    6-ModelPusher
'''

@dataclass
class DataIngestionArtifact:
    '''
    out for data_ingestion.py
    '''
    feature_store_file_path:str
    train_file_path:str 
    test_file_path:str


@dataclass
class DataValidationArtifact:
    report_file_path:str


class DataTransformationArtifact:...
class ModelTrainerArtifact:...
class ModelEvaluationArtifact:...
class ModelPusherArtifact:...




