from ..database import Base
from sqlalchemy import Column, Integer, String, text
from sqlalchemy.sql.sqltypes import TIMESTAMP


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    role = Column(String, nullable=False, server_default="user")
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))