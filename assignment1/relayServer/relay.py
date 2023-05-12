import socket
import selectors
import sys
import struct
import json
import traceback

class Message:
    def __init__(self, selector, sock, addr):
        self.selector = selector
        self.sock = sock
        self.addr = addr
        self._recv_buffer = b""
        self._send_buffer = b""
        self._jsonheader_len = None
        self.jsonheader = None
        self.request = None
        self.response_created = False

    def process_protoheader(self):
        hdrlen = 2
        if len(self._recv_buffer) >= hdrlen:
            self._jsonheader_len = struct.unpack(
                ">H", self._recv_buffer[:hdrlen]
            )[0]
            self._recv_buffer = self._recv_buffer[hdrlen:]
    
    def handle_push(self,jsonheader,length):
        jsonheader_bytes=json.dumps(self.jsonheader, ensure_ascii=False).encode()
        message_hdr = struct.pack(">H", len(jsonheader_bytes))

        message = message_hdr + jsonheader_bytes + self._recv_buffer
        try:
                # Should be ready to write
                sent = dumpSocket.send(self._send_buffer)
        except BlockingIOError:
            pass
        else:
            self._send_buffer = self._send_buffer[sent:]
            # Close when the buffer is drained. The response has been sent.
            if sent and not self._send_buffer:
                self.close()



    def process_jsonheader(self):
        hdrlen = self._jsonheader_len
        if len(self._recv_buffer) >= hdrlen:
            self.jsonheader = json.load(self._recv_buffer[:hdrlen]     ) #space left out to comeback for utf-8 issue in future if required
            self._recv_buffer = self._recv_buffer[hdrlen:]
            for reqhdr in (
                "byteorder",
                "lengthofdata",
                "request",
                # "user",
            ):
                if reqhdr not in self.jsonheader:
                    raise ValueError(f"Missing required header '{reqhdr}'.")
            if self.jsonheader["request"]=="push":
                length=self.jsonheader["lengthofdata"]
                self.handle_push(self.jsonheader,length)

    def service_connection(self,mask):
        if mask & selectors.EVENT_READ:
            # recv_data = sock.recv(1024)  # Should be ready to read
            # def _read(self):
            try:
                # Should be ready to read
                data = self.sock.recv(4096)
            except BlockingIOError:
                # Resource temporarily unavailable (errno EWOULDBLOCK)
                pass
            else:
                if data:
                    self._recv_buffer += data
                else:
                    raise RuntimeError("Peer closed.")

            # if recv_data:
            #     data.outb += recv_data
            # else:
                # print(f"Closing connection to {data.addr}")
                # sel.unregister(self.sock)
                # self.sock.close()

            if self._jsonheader_len is None:
                self.process_protoheader()

            if self._jsonheader_len is not None:
                if self.jsonheader is None:
                    self.process_jsonheader()

if len(sys.argv) != 5:
    print(f"Usage: {sys.argv[0]} <host> <port> <dumpHost> <dumpPort>")
    sys.exit(1)

sel=selectors.DefaultSelector()

# taking hosts and ports of the relay server and dump server as
# command line arguments
host=sys.argv[1]
port=int(sys.argv[2])
dumpHost=sys.argv[3]
dumpPort=int(sys.argv[4])


# function that accepts connections from client server
def accept_wrapper(sock):
    conn, addr = sock.accept()  # Should be ready to read
    print(f"Accepted connection from {addr}")
    conn.setblocking(False)
    message = Message(sel, conn, addr)
    sel.register(conn, selectors.EVENT_READ, data=message)




#function that receives and sends data to the client server

    # if mask & selectors.EVENT_WRITE:
    #     if data.outb:
    #         print(f"Echoing {data.outb!r} to {data.addr}")
    #         sent = sock.send(data.outb)  # Should be ready to write
    #         data.outb = data.outb[sent:]
    



#function that receives and sends data to the client server


#binding the relay server with client
relaySocket= socket.socket()
relaySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
relaySocket.bind((host,port))
relaySocket.listen()
print(f"listening on {(host,port)}")
relaySocket.setblocking(False)
sel.register(relaySocket, selectors.EVENT_READ, data=None)

#creating socket for relay server to dump server
dumpSocket= socket.socket()
dumpSocket.connect((dumpHost,dumpPort))
dumpSocket.setblocking(False)
sel.register(dumpSocket, selectors.EVENT_WRITE,data=None)

# checking if the objects have been connected already
# if not connected, then making the connection
# if connected, then receiving data
try:
    while True:
        events = sel.select(timeout=None)
        for key, mask in events:
            if key.data is None:
                accept_wrapper(key.fileobj)
            else:
                message = key.data
                try:
                    message.service_connection(mask)

                except Exception:
                    print(
                        f"Main: Error: Exception for {message.addr}:\n"
                        f"{traceback.format_exc()}"
                    )
                   
except KeyboardInterrupt:
    print("Caught keyboard interrupt, exiting")
finally:
    sel.close()









