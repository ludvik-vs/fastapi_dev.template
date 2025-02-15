from sqlalchemy import Column, Integer, String 
from database import Base


#Modelos
class Test(Base):
    __tablename__ = 'Test'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), unique=True, nullable=False)
