from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from my_project import crud, models, schemas
from my_project.database import SessionLocal, engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/detection_data/", response_model=schemas.DetectionData)
def create_detection_data(detection_data: schemas.DetectionDataCreate, db: Session = Depends(get_db)):
    return crud.create_detection_data(db=db, detection_data=detection_data)

@app.get("/detection_data/", response_model=List[schemas.DetectionData])
def read_detection_data(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    detection_data = crud.get_detection_data(db, skip=skip, limit=limit)
    return detection_data

@app.get("/")
def read_root():
    return {"message": "Welcome to the Detection Data API"}