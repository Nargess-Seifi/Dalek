import os
import ujson as js
import time
import network
import machine
import urequests as rq

################### constants #####################
SSID = "Galaxy A73"
key = "00000000"
apiKey = 'lOoRtUsEPgHPxp4ZG5YfocnowXvio4iQupbp9OGb'    
apiUrl = 'https://api.nasa.gov/planetary/apod'

################### functions #####################
def init():
    pin = machine.Pin(2, machine.Pin.OUT)
    pin2 = machine.Pin(16, machine.Pin.OUT)
    pin.value(1)
    pin2.value(1)
    uart = machine.UART(0, baudrate=115200 )


def do_connect():

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        uart.write('connecting to network...')
        wlan.connect(SSID, key)
        while not wlan.isconnected():
            pass
    time.sleep(1)
    uart.write('\nconnected\n')
    pin.value(0)


while(True):
    init()
    do_connect()
    
    uart.write("tryna send a req\n")   
    rurl = apiUrl + '?api_key=' + apiKey 
    try:
        r = rq.get(rurl)
        
        uart.write('req OK\n')
        res = js.loads(r.text)
        for k in res.keys():
            uart.write(k + '\t')
        uart.write('\n')
        
 
        break
        #uart.write(temp + ' - ' + str(time.time()-s) + ' Seconds')
    
    except:
        uart.write("time out\n")
