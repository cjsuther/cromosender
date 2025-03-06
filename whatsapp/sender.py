from whatsapp import WhatsApp, Message
from dotenv import dotenv_values

config = dotenv_values(".env")

messenger = WhatsApp(token=config['WHATSAPP_TOKEN'], 
                     phone_number_id={1:config['WHATSAPP_PHONE_NUMBER_ID'], 2:config['WHATSAPP_PHONE_NUMBER_ID_2']})

def whatsapp_text(message, to):
  msg = Message(instance=messenger, content=message, to=to)
  return msg.send()

def whatsapp_template(template, to, components=[]):
  return messenger.send_template(template, recipient_id=to, components=components, lang="en_US")
