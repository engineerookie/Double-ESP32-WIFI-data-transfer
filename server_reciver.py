import socket
import network
import time
from machine import Pin,PWM
# ########################################################################################################################################
ID="How dare you"                                                        # "How dare you" ID
LED_warning=Pin(2,Pin.OUT)                                               
pwm_pin=[0]*4                                                            # pwm_pin setting
pwm_data=[0]*4
for num in range(4):                                                     # do the same as we do it with client
   pin=21
   pwm_pin[num]=PWM(Pin(pin),freq=250,duty=256)                          # pwm_pin[0]=Pin32 
   pin+=1                                                                # pwm_pin[1]=Pin33 
   if num==3:                                                            # pwm_pin[2]=Pin34
     pin=25                                                              # pwm_pin[3]=Pin35
     pwm_pin[num]=PWM(Pin(pin),freq=250,duty=256)
print("your pin have been set up,here are those PWM pins")
for j in range(4):
   print(pwm_pin[j])
# ########### main section ###############################################################################################################
try:  
   wifi=network.WLAN(network.AP_IF)                                      # wifi set to access point mode for the client or station
   wifi.active(1)                                  
   wifi.config(essid=ID, channel=1)
   server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)              # set server socket as client's setting
   server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)          # the same
   server.bind(("192.168.4.1",100))                                      # server need to bind the configuration(IP,port) with itself
   server.listen(2)                                                      # the max number of requisting
# ########################################################################################################################################
   LED_warning.value(1)
   time.sleep(2)
   LED_warning.value(0)
   while True:  
     print("waiting")
     conn,addr=server.accept()                                           # server will create another new socket object 
     print('client message address is',addr)                             # to recieve the date from client,the new object is connect
# ####### main loop ######################################################################################################################
     while True:
       for pwm in range(2):
         pwm_data[pwm]=conn.recv(1024)
         pwm_data[pwm]=int(pwm_data[pwm])+1000
         print(rec_data)
except:
   print("error")                                                        # the situation that we don't expect will trigger this "expect"
