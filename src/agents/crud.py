import uuid
from sqlalchemy.orm import Session
from agents import models 
from agents.api import schemas 

def create_agent(db: Session,agent: schemas.AgentCreate):
    db_agent=models.Agent(
        id=str(uuid.uuid4()),
        context= agent.context,
        first_message = agent.first_message,
        response_shape=agent.response_shape,
        instructions = agent.instructions
    )
    db.add(db_agent)
    db.commit()
    db.refresh(db_agent)

    return db_agent

