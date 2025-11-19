from machine import Pin
from time import sleep

from ir_rx import NEC_16

pin_relay1=Pin(14, Pin.OUT)
pin_relay1.off()

pin_relay2=Pin(27, Pin.OUT)
pin_relay2.off()

pin_relay3=Pin(16, Pin.OUT)
pin_relay3.off()

pin_relay4=Pin(17, Pin.OUT)
pin_relay4.off()


def telecomanda(data, addr, ctrl):
    if data>0:
        print("Valoarea generata este ", data)
        if data==9:
            #activare relay 1
            pin_relay1.on()
            pin_relay2.off()
            pin_relay3.off()
            pin_relay4.off()
        if data==29:
            #activare relay 1
            pin_relay1.off()
            pin_relay2.on()
            pin_relay3.off()
            pin_relay4.off()
        if data==31:
            #activare relay 1
            pin_relay1.off()
            pin_relay2.off()
            pin_relay3.on()
            pin_relay4.off()
        if data==13:
            #activare relay 1
            pin_relay1.off()
            pin_relay2.off()
            pin_relay3.off()
            pin_relay4.on()
        if data==77:
            #dezactivare relay 1 
            pin_relay1.off()
            pin_relay2.off()
            pin_relay3.off()
            pin_relay4.off()

pin_ir=Pin(5, Pin.IN)

var=NEC_16(pin_ir, telecomanda)

while True:
    sleep(1)
