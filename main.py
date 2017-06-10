import socket
import machine

tmp36 = machine.ADC(0)

RESPONSE = """\
HTTP/1.1 200 OK
Content-Type: text/html

{0}
"""

s = socket.socket()

ai = socket.getaddrinfo('0.0.0.0', 8080)
addr = ai[0][-1]

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind(addr)
s.listen(5)
print('Listening on port 8080')

while True:
    res = s.accept()
    client_s = res[0]
    req = client_s.recv(4096)
    # formula (not sure if it's correct): tmp36.read() / 3.3 / 1024 * 100
    temperature = tmp36.read() / 3.3 / 1024 * 100
    client_s.send(RESPONSE.format(str(temperature)))
    client_s.close()
