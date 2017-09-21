# server.py
import socket
import time
import thread
import signal

def process_remote_conn(conn,addr):
    print("Got a connection from %s" % str(addr))
    while True:
        currentTime = time.ctime(time.time()) + "\r\n"
        conn.send(currentTime.encode('ascii'))
    #clientsocket.close()


def server():
    # create a socket object
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # get local machine name
    #host = socket.gethostname()
    host = "127.0.0.1"
    port = 9999
    # bind to the port
    serversocket.bind((host, port))
    # queue up to 5 requests
    serversocket.listen(5)
    print "listening for connect..."
    while True:
    # establish a connection
        clientsocket,addr = serversocket.accept()
        thread.start_new_thread(process_remote_conn,(clientsocket,addr))
def sig_handler(sig,frame):
    print "Got a signal: " + str(sig)

if __name__ == "__main__":
    signal.signal(signal.SIGPIPE,sig_handler)
    server();
