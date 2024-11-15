from sqlalchemy import BigInteger, String, DateTime
from sqlalchemy.orm import DeclarativeBase, mapped_column
from pytz import timezone 
from datetime import datetime

class Base(DeclarativeBase):
    pass

def get_ist_datetime():
    return datetime.now(timezone("Asia/Kolkata"))

class DbTable(Base):
    __tablename__ = 'db_table'
    
    id = mapped_column(BigInteger(), primary_key=True)
    
    name = mapped_column(String(20), nullable=False, unique=True, index=True)
    
    email = mapped_column(String(320), nullable=False, unique=True)
    
    password = mapped_column(String(256), nullable=False)
    
    created_at = mapped_column(DateTime, default=get_ist_datetime)
    
    updated_at = mapped_column(DateTime, default=get_ist_datetime, onupdate=get_ist_datetime)

    def __repr__(self):
        return f"<DbTable(id={self.id}, name='{self.name}', email='{self.email}')>"