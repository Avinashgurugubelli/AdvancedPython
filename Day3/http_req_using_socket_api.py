'''
An example script to make a http req using socket api
'''

import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # address = ('www.ntu.edu.sg', 80)
    # using proxy
    addr = ('165.225.96.34', 9480)
    client.connect(addr)
    req = 'GET /home/ehchua/programming/ http/1.1'
    req += '\r\nHost: www.ntu.edu.sg'
    req += '\r\nAccept: text/html'
    req += '\r\nConnection: close\r\n\r\n'

    client.send(req.encode())
    output = ''
    while True:
        resp = client.recv(1024)
        if not resp: break
        output += resp.decode()
    print(output)
if __name__ == '__main__':
    main()
    