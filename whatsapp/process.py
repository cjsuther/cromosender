from schedule import every, repeat, run_pending
import time
from dotenv import dotenv_values
from models import Base, Message
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import crud
import sender
import json

config = dotenv_values(".env")

engine = create_engine('mysql+pymysql://' + config['MYSQL_USER'] + ':' + config['MYSQL_PASSWORD'] + '@' + config['MYSQL_HOST'] + ':' + config['MYSQL_PORT'] + '/' + config['MYSQL_DATABASE'] + '')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

@repeat(every(int(config['RUN_TIME_SECONDS'])).seconds)
def job():
  session = Session()
  messages = crud.get_messages_to_send(session)
  for m in messages:
     if(m.Message.type == 'whatsapp'):
        if(m.Message.template=='custom'):
          result = sender.whatsapp_text(m.Message.variables, m.Message.destination)
        else:
          result = sender.whatsapp_template(m.Message.template, m.Message.destination)
        print(json.dumps(result))
        crud.update_message_status(session, m.Message.id, json.dumps(result))
  session.close()

print("process started")
#job()

while True:
    run_pending()
    time.sleep(10)