#author guojingyu
#date      Sep 28, 2014
import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy.orm import session 
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.orm import exc
from sqlalchemy import Sequence 
from sqlalchemy.ext.declarative import declarative_base as sqlalchemyBase
Base = sqlalchemyBase()
class Employee(Base): 
    __tablename__ = "employee"
    id = sa.Column(sa.Integer,primary_key = True)
    name = sa.Column(sa.String(20),nullable = False)
    fullname = sa.Column(sa.String(50),nullable = False)
    password = sa.Column(sa.String(50),nullable = False)
    
    def __repr__(self):
        return "ID : %s , name : %s ,fullname : %s ,password : %s "%(self.id,self.name,self.fullname,self.password)

"""
1.A class using Declarative at a minimum needs a __tablename__ attribute, and at least one Column which is part of
  a primary key
2.
"""