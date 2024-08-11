from typing import List
from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session

import agents.api.schemas
import agents.models
from agents.database import SessionLocal,engine

from agentsfwrk import integrations,logger

import agents.crud

log=logger.get_logger(__name__)

agents.models.Base.metadata.create_all(bind=engine)

router=APIRouter(
    prefix="/agents",
    tags=["Chat"],
    responses={404: {"description":"Not found"}}
)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
async def agents_root():
    return {"message":"Hello there conversational ai!"}

@router.post("/create-agent",response_model=agents.api.schemas.Agent)
async def create_agent(agent : agents.api.schemas.AgentCreate,db: Session = Depends(get_db)):
    log.info(f"Create agent")
    db_agent=agents.crud.create_agent(db,agent)
    log.info(f"Agent created with id: {db_agent.id}")

    return db_agent
