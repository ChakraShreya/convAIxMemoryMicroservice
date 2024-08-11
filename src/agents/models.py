from sqlalchemy import Column,ForeignKey,String,DateTime,JSON
from sqlalchemy.orm import relationship
from datetime import datetime

from agents.database import Base

class Agent(Base):
    __tablename__="agents"

    id = Column(String,primary_key=True,index=True)
    timestamp = Column(DateTime,default=datetime.utcnow)
    
    context=Column(String,nullable=False)
    first_message=Column(String,nullable=False)
    response_shape=Column(JSON,nullable=False)
    instructions=Column(String,nullable=False)
    