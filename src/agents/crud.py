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

def get_agent(db: Session, agent_id: str):
    """
    Get an agent by its id
    """

    return db.query(models.Agent).filter(models.Agents.id==agent_id).first()

def get_conversation(db: Session, conversation_id: str):
    """
    Get a conversation by its id
    """
    return db.query(models.Conversations).filter(models.Conversation.id==conversation_id).first()

def create_conversation(db: Session, conversation: schemas.ConversationCreate):
    """
    Create a conversation
    """
    db_conversation = models.Conversation(
        id = str(uuid.uuid4()),
        agent_id = conversation.agent_id,
    )
    db.add(db_conversation)
    db.commit()
    db.refresh(db_conversation)

    return db_conversation