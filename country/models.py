from sqlalchemy import Column,Integer,String,Boolean,ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Country(Base):
    __tablename__ = "country"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String,unique=True,index=True)
    states = relationship("State", back_populates="country")
    is_deleted = Column(Boolean,default=False)

class State(Base):
    __tablename__="state"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String,unique=True,index=True)
    country_id = Column(Integer, ForeignKey("country.id"))
    country = relationship("Country", back_populates="states")
    districts = relationship("District", back_populates="state")
    is_deleted = Column(Boolean,default=False)

class District(Base):
    __tablename__="district"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String,unique=True,index=True)
    state_id = Column(Integer, ForeignKey("state.id"))
    state = relationship("State", back_populates="districts")
    villages = relationship("Village", back_populates="district")
    is_deleted = Column(Boolean,default=False)

class Village(Base):
    __tablename__="village"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String,unique=True,index=True)
    district_id = Column(Integer, ForeignKey("district.id"))
    district = relationship("District", back_populates="villages")
    is_deleted = Column(Boolean,default=False)


