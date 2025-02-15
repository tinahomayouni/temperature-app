from sqlalchemy.orm import Session
from . import models, schemas

def get_medicine_by_name(db: Session, name: str):
    return db.query(models.Medicine).filter(models.Medicine.name == name).first()

def create_medicine(db: Session, medicine: schemas.MedicineBase, temperature: float):
    db_medicine = models.Medicine(name=medicine.name, temperature=temperature)
    db.add(db_medicine)
    db.commit()
    db.refresh(db_medicine)
    return db_medicine
