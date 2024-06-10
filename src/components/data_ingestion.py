import sys 
import os
from src.exception import CustomException
from src.logger import logging
import pandas as pd 
import numpy as np 

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig: 
    train_data_path :str=os.path.join('Output',"train.csv")
    test_data_path :str=os.path.join('Output',"test.csv")
    raw_data_path :str=os.path.join('Output',"data.csv")
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
    
    def init_data_ingestion(self):
        logging.info("Entered the data ingestion component")
        try:
            df=pd.read_csv('notebook/data/stud.csv')      #read the dataset from anywhere api,database 
            logging.info('Dataset as data_frame loaded....')
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
        
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info("Train test split initiated...")
            
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            
            logging.info("Ingestion of data Completed")
            
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
                
            )
        except Exception as e:
            raise CustomException(e,sys)
        
        
        
if __name__=="__main__":
    obj=DataIngestion()
    obj.init_data_ingestion()