from sqlalchemy import select, update
from models import Message
import hashlib
from dotenv import dotenv_values
import json
import datetime

config = dotenv_values()

def get_messages_to_send(session) -> list[Message]:
    result = session.execute(select(Message).where(Message.status == 'Created', Message.schedule_time < datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))).all()
    return result

def update_message_status(session, id, result):
    session.execute(update(Message).where(Message.id == id).values({'status':'Sent', 'result':result, 'sent_time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}))
    session.commit()
