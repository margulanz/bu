from pydantic import BaseModel
from .models import Image



class ImageBase(BaseModel):
	id : int
	label : str = ''
	url : str
	percentage: int = None
	class Config:
		orm_mode = True



