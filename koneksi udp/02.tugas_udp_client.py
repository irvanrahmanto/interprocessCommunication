# import library socket karena akan menggunakan IPC socket
import socket

# definisikan target IP server yang akan dituju
UDP_IP = '127.0.0.1'

# definisikan target port number server yang akan dituju
UDP_PORT = 5005

PESAN = "Hello World!"

#print ("target IP:", UDP_IP)
print("target IP: ", UDP_IP)

#print ("target port:", UDP_PORT)
print("target port: ", UDP_PORT)

#print ("pesan:", PESAN)
print("pesan: ", PESAN)

# step 1: create socket
# buat socket bertipe UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Internet & UDP

# step 2: client can immediately send message; if server not ready, message will be dropped
# lakukan loop 10 kali
for x in range(10):
    # definisikan pesan yang akan dikirim
    sock.sendto(PESAN.encode(), (UDP_IP, UDP_PORT))
    # kirim pesan
