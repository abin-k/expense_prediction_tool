from sqlalchemy.orm import Session
import database
from models import Prediction
import pickle

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

with open("model.pkl", "rb") as file:
    model = pickle.load(file)

with open("label_encoders.pkl", "rb") as file:
    label_encoders = pickle.load(file)

with open("scaler.pkl", "rb") as file:
    scaler = pickle.load(file)        
    
    
    
    
def predict(Age:str ,Gender:str ,OwnHome:str ,Married:str ,Location:str ,Salary:int ,Children:int ,History:str ,Catalogs:int):
    Age=label_encoders['Age_encoder'].transform([Age])[0]
    Gender=label_encoders['Gender_encoder'].transform([Gender])[0]
    OwnHome=label_encoders['OwnHome_encoder'].transform([OwnHome])[0]
    Married=label_encoders['Married_encoder'].transform([Married])[0]
    Location=label_encoders['Location_encoder'].transform([Location])[0]
    History=label_encoders['History'].transform([History])[0]

    features=scaler.transform([[Age, Gender, OwnHome, Married, Location, Salary, Children, History, Catalogs]])
    prediction_value = model.predict(features)
    return prediction_value

    
    
def create_prediction(db:Session, Age:str ,Gender:str ,OwnHome:str ,Married:str ,Location:str ,Salary:int ,Children:int ,History:str ,Catalogs:int, prediction_value :float):
    db_prediction = Prediction(Age=Age, Gender=Gender, OwnHome=OwnHome, Married=Married, Location=Location, Salary=Salary, Children=Children, History=History, Catalogs=Catalogs, prediction_value=prediction_value)    
    db.add(db_prediction )
    db.commit()
    return db_prediction 

def view(db:Session,id:int ):
    return db.query(Prediction).filter(Prediction.id==id).first()

def view_filter(db:Session,skip:int=0, limit:int=10):
    return db.query(Prediction).offset(skip).limit(limit).all()

def get_all_predictions(db: Session):
    return db.query(Prediction).all()





