from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas, database

app = FastAPI()

@app.post("/add_medicine/")
def add_medicine(medicine: schemas.MedicineBase, temperature: float, db: Session = Depends(database.get_db)):
    return crud.create_medicine(db=db, medicine=medicine, temperature=temperature)

@app.get("/medicine/{name}")
def get_temperature(name: str, db: Session = Depends(database.get_db)):
    medicine = crud.get_medicine_by_name(db=db, name=name)
    if medicine is None:
        raise HTTPException(status_code=404, detail="Medicine not found")
    return {"name": medicine.name, "temperature": medicine.temperature}
