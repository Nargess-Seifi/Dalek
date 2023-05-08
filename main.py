import machine
import time
import network
import os
import urequests as rq

SSID = "Galaxy A73"
key = "00000000"


parameters = {
    "appid": "66ZDSC4P4ZMS"
}


uart = machine.UART(0, baudrate=115200 )


def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        uart.write('connecting to network...')
        wlan.connect(SSID, key)
        while not wlan.isconnected():
            pass
    uart.write('\nconnected\n')


pin = machine.Pin(2, machine.Pin.OUT)
pin2 = machine.Pin(16, machine.Pin.OUT)

do_connect()

while(True):
    uart.write("tryna send a req\n")
#    response_API = rq.request(method = GET, 'http://api.timezonedb.com/v2.1/list-time-zone', key = '66ZDSC4P4ZMS')
 #   response_API = rq.get('http://api.timezonedb.com/v2.1/list-time-zone')
  #  response = urequests.get('https://dog.ceo/api/breeds/image/random')
 #   uart.write("request submited")
#    uart.write(str(type(response)))
    
    
    s=time.time()

    try:
        uart.write("inja\n")
        r = rq.get('https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY')
    except rq.exceptions.Timeout as err: 
        uart.write(str(err))
        time.sleep(1)

    uart.write('injaaaaaaaa')
    
    temp = r.text
    uart.write(temp + ' - ' + str(time.time()-s) + ' Seconds')    
