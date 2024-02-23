from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import crud, database, models
import pickle
from crud import get_db


app = FastAPI()
models.Base.metadata.create_all(bind=database.engine)  # Create tables
        
        
@app.post("/predict/")
def predict(Age:str ,Gender:str ,OwnHome:str ,Married:str ,Location:str ,Salary:int ,Children:int ,History:str ,Catalogs:int, db:Session = Depends(get_db)):
    prediction_value=crud.predict(Age, Gender, OwnHome, Married, Location, Salary, Children, History, Catalogs)
    crud.create_prediction(db=db, Age=Age, Gender=Gender, OwnHome=OwnHome, Married=Married, Location=Location, Salary=Salary, Children=Children, History=History, Catalogs=Catalogs, prediction_value=prediction_value[0])
    return {"predicted_future_expenses": prediction_value[0]}



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
    
    
    
    
# Load the machine learning model
# with open("model.pkl", "rb") as file:
#     model = pickle.load(file)

# @app.post("/predict/")
# def predict(Age:float ,Gender:float ,OwnHome:float ,Married:float ,Location:float ,Salary:float ,Children:float ,History:float ,Catalogs:float, db:Session = Depends(get_db)):
#     prediction_value = model.predict([[Age,Gender,OwnHome,Married,Location,Salary,Children,History,Catalogs]])[0]
#     crud.create_prediction(db=db,Age=Age, Gender=Gender, OwnHome=OwnHome, Married=Married, Location=Location, Salary=Salary, Children=Children, History=History, Catalogs=Catalogs, prediction_value=prediction_value)
#     return {
#         "predicted future expenses":prediction_value
#     }    