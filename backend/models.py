from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Rule(Base):
    __tablename__ = 'rules'
    
    id = Column(Integer, primary_key=True)
    rule_string = Column(String, nullable=False)

engine = create_engine('sqlite:///rules.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
