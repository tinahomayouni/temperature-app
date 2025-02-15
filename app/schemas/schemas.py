from pydantic import BaseModel

class MedicineBase(BaseModel):
    name: str

class Medicine(MedicineBase):
    id: int
    temperature: float

    class Config:
        orm_mode = True
