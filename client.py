import socket #for networking
import sys #commandline args
from rsa import * #ecryption/decryption
from PLcrypto import * #encryption/decryption
import no_bytecode #bytecode
import threading #allow multiple threads of the same program to run

#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
#     host = 'server ip address..' port = 6666 
# try: s.bind((host, port)) 
# except socket.error as e: print(str(e)) 
#     s.connect((host, port)) 
#     print(s.recv(1024)) s.close()


def connect(server):
    host = '127.0.0.1'
    port = 6666
    server.connect((host, port))
    server.sendall("Client connecting")

def recv():
    response = rsadecrypt(server.recv(1024), key)
    if response == "Goodbye":
        server.close()
        sys.exit()
    else:
        while True:
            print(response)
            data = raw_input()
            
            if data:
                server.sendall(rsaencrypt(data, serverkey))
                break

# check if signature was verified
def checkVerification(server, message):
    if not message: #shutdown connection
        server.shutdown(socket.SHUT_RDWR)
        server.close()
        sys.exit(1)
    else:
        return message

if __name__ == '__main__':
    server = socket.socket()
    connect(server)

    pubkeyfile = 'client.pem'
    key = gen_privkey()
    save_pubkey(pubkeyfile, gen_pubkey(key))
    serverkey = get_pubkey(str(server.recv(1024)))
    server.sendall(pubkeyfile)
    aeskey = rsadecrypt(server.recv(1024), key)
    if not aeskey:
        sys.exit(1)
    # server sends client a nonce (a new one is created each time connection is made)
    # client can only access nonce with session key
    # client sends back modified nonce to confirm that the session key has been received
    nonce = checkVerification(server, PLdecrypt(server.recv(1024), serverkey, aeskey))
    server.sendall(PLencrypt(str(float(nonce)-1), key, aeskey))

    while True:
        response = checkVerification(server, PLdecrypt(server.recv(1024), serverkey, aeskey))
        if response == "see you when you see me":
            server.shutdown(socket.SHUT_RDWR)
            server.close()
            sys.exit()
        else:
            while True:
                print(response)
                data = raw_input()         
                if data:
                    server.sendall(PLencrypt(data, key, aeskey))
                    break
