from sqlalchemy.orm import Session
from models import Prediction


def create_prediction(db:Session, Age:float ,Gender:float ,OwnHome:float ,Married:float ,Location:float ,Salary:float ,Children:float ,History:float ,Catalogs:float, prediction_value :float):
    db_prediction = Prediction(Age=Age, Gender=Gender, OwnHome=OwnHome, Married=Married, Location=Location, Salary=Salary, Children=Children, History=History, Catalogs=Catalogs, prediction_value=prediction_value)
    db.add(db_prediction )
    db.commit()
    db.refresh(db_prediction )
    return db_prediction 

def view(db:Session,id:int ):
    return db.query(Prediction).filter(Prediction.id==id).first()

def view_filter(db:Session,skip:int=0, limit:int=10):
    return db.query(Prediction).offset(skip).limit(limit).all()

def get_all_predictions(db: Session):
    return db.query(Prediction).all()

