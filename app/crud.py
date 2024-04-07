from sqlalchemy.orm import Session
from . import models, schemas

def create_user(db: Session, user: schemas.UserCreate):
    role = db.query(models.Role).filter(models.Role.id == user.role_id).first()
    if role is None:
        return None
    
    # Create a new user
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user
