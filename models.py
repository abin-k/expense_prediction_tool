from sqlalchemy import Column, Integer, String, Float
from database import Base
# from pydantic import BaseModel


class Prediction(Base):
    __tablename__ = "Predictions"
    
    id = Column(Integer, primary_key=True, index=True)
    Age  =  Column(String(50) ) 
    Gender= Column(String(50)) 
    OwnHome= Column(String(50))  
    Married= Column(String(50)) 
    Location= Column(String(50)) 
    Salary=  Column(Integer)  
    Children= Column(Integer)  
    History=  Column(String(50)) 
    Catalogs= Column(Integer)
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
    
    

        

        