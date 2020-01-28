# import library socket karena akan menggunakan IPC socket
import socket

# definisikan target IP server yang akan dituju
UDP_IP = '127.0.0.1'

# koneksi 2 komputer
# UDP_IP = '172.20.10.2'

# definisikan target port number server yang akan dituju
UDP_PORT = 5008

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

y = 1
for x in range(10):
    # definisikan pesan yang akan dikirim
    x = PESAN + str(y)
    sock.sendto(x.encode(), (UDP_IP, UDP_PORT))
    y = y+1
    # kirim pesan
