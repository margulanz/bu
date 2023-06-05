from sqlalchemy.orm import Session
from . import models, schemas



def create_image(db: Session):
	image = models.Image()
	db.add(image)
	db.commit()
	db.refresh(image)
	return image

def get_image(id : int, db: Session):
	return db.query(models.Image).filter(models.Image.id == id).first()

def update_image(id: int, result:dict, db: Session):
	image = get_image(id,db)
	image.label = result['Label']
	image.percentage = result['percentage']
	db.commit()
