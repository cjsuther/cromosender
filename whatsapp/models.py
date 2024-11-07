from sqlalchemy import Column, Integer, String, ForeignKey, types, DateTime, Text
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
from datetime import date
from typing import List

class Base(DeclarativeBase):
  pass

class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True)
    type = Column(String(10))
    destination = Column(String(50))
    variables = Column(Text)
    template = Column(Text)
    creation_time = Column(DateTime)
    schedule_time = Column(DateTime)
    sent_time = Column(DateTime)
    status = Column(String(10))
    result = Column(Text)

    #def getValue(self):
    #    message = {
    #        'id': self.id,
    #        'type': self.type,
    #        'destination': self.destination,
    #        'variables': self.variables,
    #        'template': self.template,
    #        'creation_time': self.creation_time,
    #        'schedule_time': self.schedule_time,
    #        'sent_time': self.sent_time,
    #        'status': self.status,
    #        'result': self.result
    #    }
    #    return message
