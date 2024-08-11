from datetime import datetime 
from typing import List,Optional
from pydantic import BaseModel

class AgentBase(BaseModel):
    context:str
    first_message:str
    response_shape:str
    instructions:str

class AgentCreate(AgentBase):
    pass

class Agent(AgentBase):
    id:str
    timestamp:datetime = datetime.utcnow()

    class Config:
        orm_mode = True
        
