from plyer import notification
import time
title = 'Hi, My name is Debasmita !'

message= 'I am bored'

notification.notify(title= title,
                    message= message,
                    timeout= 20,
                    toast= False)

time.sleep(60*60)