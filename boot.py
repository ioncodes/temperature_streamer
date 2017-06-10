import network
import webrepl
import ujson
import time

configuration_file = open('network.json', 'r')
configuration = ujson.loads(configuration_file.read())
configuration_file.close()
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(configuration['name'],configuration['password'])
while(wifi.isconnected() == False):
    time.sleep_ms(1)
print('Connected!')
print('My IP is: {0}'.format(wifi.ifconfig()[0]))
print('Starting WebREPL...')
webrepl.start()
print('Started WebREPL!')
