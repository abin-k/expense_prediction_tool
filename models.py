from sqlalchemy import Column, Integer, String, Float
from database import Base
# from pydantic import BaseModel


class Prediction(Base):
    __tablename__ = "Predictions"
    
    id = Column(Integer, primary_key=True, index=True)
    Age  =  Column(Float) 
    Gender= Column(Float) 
    OwnHome= Column(Float)  
    Married= Column(Float) 
    Location= Column(Float) 
    Salary=  Column(Float)  
    Children= Column(Float)  
    History=  Column(Float) 
    Catalogs= Column(Float)
    prediction_value =Column(Float) 
    
    
    

#  Class which describes Bank Notes measurements
# class expense(BaseModel):
#     Age:  float 
#     Gender: float 
#     OwnHome:float 
#     Married:float
#     Location:float 
#     Salary: float 
#     Children:float 
#     History:float
#     Catalogs:float
    
    

        

        