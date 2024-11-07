from whatsapp import WhatsApp, Message
from dotenv import dotenv_values

config = dotenv_values(".env")

messenger = WhatsApp(token=config['WHATSAPP_TOKEN'], 
                     phone_number_id={1:config['WHATSAPP_PHONE_NUMBER_ID']})

def whatsapp_text(message, to):
  msg = Message(instance=messenger, content=message, to=to)
  return msg.send()

def whatsapp_template(template, to):
  return messenger.send_template(template, recipient_id=to, components=[], lang="en_US")
