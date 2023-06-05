from fastapi import FastAPI, File, UploadFile, Depends, HTTPException
from sqlalchemy.orm import Session

import uuid
from . import models, classify, crud
from .database import SessionLocal
app = FastAPI()

IMAGEDIR = "images/"




def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/images/")
async def upload_image(file: UploadFile = File(...), db: Session = Depends(get_db)):
    image_obj = crud.create_image(db)
    file.filename = f"{image_obj.id}.jpg"
    image = await file.read()
    with open(f"{IMAGEDIR}{file.filename}", "wb") as f:
        f.write(image)
    result = classify.classify(f"{IMAGEDIR}{file.filename}")
    crud.update_image(image_obj.id, result, db)
    return {'status': 'success'}



@app.get("/images/{id}")
async def get_image_prediction(id:int, db: Session = Depends(get_db)):
    image = crud.get_image(id,db)
    if image is None:
        raise HTTPException(status_code=404, detail="Image not found")

    return image