from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import crud, database, models
import pickle


app = FastAPI()

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

models.Base.metadata.create_all(bind=database.engine)  # Create tables
        
# Load the machine learning model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

@app.post("/predict/")
def predict(Age:float ,Gender:float ,OwnHome:float ,Married:float ,Location:float ,Salary:float ,Children:float ,History:float ,Catalogs:float, db:Session = Depends(get_db)):
    prediction_value = model.predict([[Age,Gender,OwnHome,Married,Location,Salary,Children,History,Catalogs]])[0]
    crud.create_prediction(db=db,Age=Age, Gender=Gender, OwnHome=OwnHome, Married=Married, Location=Location, Salary=Salary, Children=Children, History=History, Catalogs=Catalogs, prediction_value=prediction_value)
    return {
        "predicted future expenses":prediction_value
    }
@app.put("/view_db/{index}")
def view_db(id:int, db:Session=Depends(get_db)):
    pred_db= crud.view(id=id,db=db)
    if pred_db is None:
        raise HTTPException(status_code=404, detail="id not found")
    return pred_db


@app.get("/predictions/")
def get_all_predictions(db: Session = Depends(get_db)):
    predictions = crud.get_all_predictions(db)
    return predictions

@app.put("/view_db/")
def view_filter_db(skip:int=0, limit:int=10, db:Session=Depends(get_db)):
    pred_db= crud.view_filter(skip=skip,limit=limit,db=db)
    if pred_db is None:
        raise HTTPException(status_code=404, detail="id not found")
    else:
        return pred_db