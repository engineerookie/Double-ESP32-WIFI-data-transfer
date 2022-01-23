import network
import socket
import time
from machine import Pin,ADC
# ######### define_Pin_setup ##################################################################################################
def transmitter_channel_setup(pin,num):
   trans_channel[num]=ADC(Pin(pin))                             # claim the adc pin
   trans_channel[num].atten(ADC.ATTN_11DB)                      # magnitude set to 3.3V
   trans_channel[num].width(ADC.WIDTH_10BIT)                    # set output limiting to 10bits(1024)
# ######### Pin_setup ######################################################################################################### 
LED_signal=Pin(2,Pin.OUT)                                       # setting LED as normal
trans_channel=[0]*4                                             # setting the variety for adc pin value
ch1_value=[0]*4                                                 # setting the variety for adc pin value
pin=32                                                           
for num in range(4):                                            # setting adc reading pin
   transmitter_channel_setup(pin,num)                           # trans_channel[0]=Pin34
   pin+=1                                                       # trans_channel[1]=Pin35
   if num == 3:                                                 # trans_channel[2]=Pin36
     pin = 39                                                   # trans_channel[3]=Pin39
     transmitter_channel_setup(pin,num)                         # using for loop to setup 4 channel
print("your Pin have beed setup,here are those Pin")            # it will be delete when hardware is already
for i in range(4):
   print(trans_channel[i])
LED_signal.value(1)                                             # LED warning
time.sleep(2)
LED_signal.value(0)
time.sleep(2)
try:
# ######### wifi_set ##########################################################################################################
   trans_sta=network.WLAN(network.STA_IF)                       # wifi set to station mode
   trans_sta.active(1)                                          # wifi active
   trans_sta.connect("How dare you")                            # wifi connect to access point which is named as "How dare you"
   print(trans_sta.ifconfig())
   print("your wifi has been set up!!!")
# ########## socket set #######################################################################################################
   clie=socket.socket(socket.AF_INET,socket.SOCK_STREAM)        # claim the client socket
   clie.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)     # socket level(isn't important)
   clie.connect(("192.168.4.1",100))                            # socket connect server(IP=192.168.4.1,PORT.NUM=100)
   print("your socket has been set up!!!")
   while True:  
     for adc_pin in range(2):
       LED_signal.value(1)                                      # cause there are 4 channel to deal with so using for loop again
       ch1_value[adc_pin]=str(trans_channel[adc_pin].read())    # store the value of reading from adc pin 
       time.sleep_ms(100)   
       clie.send(ch1_value[adc_pin])
       LED_signal.value(0)
     adc_pin=0                                                  # reset control  flag      
except:                                                         # send it through wifi that is been constructed 
   print("error with try section!!!")                           # if there is anything wrong with "try" section then do nothing

