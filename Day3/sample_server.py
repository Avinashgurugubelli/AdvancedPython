'''
module sample_server

Waits for a client to connect, gets a message , and sends it back in upper case version of the same
'''
import socket

def main():
    server = socket.socket()
    addr = ('', 9999)
    server.bind(addr)
    server.listen(5)

    # end less loop
    while True:
        print('waiting for connection..')
        (client, clientAddr) = server.accept()
        print('got a new connection')
        text = client.recv(1024)
        text = text.decode()
        # print('[SERVER] recd: from {}: {}'.format(clientAddr, text))
        client.send(text.upper())
        client.close()
        if text == 'QUIT': break
    server.close()

if __name__ == "__main__":
    main()