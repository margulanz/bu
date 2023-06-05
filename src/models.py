from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship,declarative_base
#from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Image(Base):
	__tablename__ = 'images'
	id = Column(Integer, primary_key = True)
	url = Column(String)
	label = Column(String)
	percentage = Column(Integer)


