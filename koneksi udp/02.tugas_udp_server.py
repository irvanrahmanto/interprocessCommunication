# import library socket karena akan menggunakan IPC socket
import socket

# definisikan alamat IP bind dari server
UDP_IP = '127.0.0.1'
# Koneksi 2 komputer
# '172.20.10.2'

# definisikan port number untuk bind dari server
UDP_PORT = 5005

# step 1: create socket# buat socket bertipe UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# step 2: binding
# lakukan bind
sock.bind((UDP_IP, UDP_PORT))
print("Binding berjalan")

# loop forever
y = 1
while True:
    # step 3: start receive message
    # terima pesan dari client
    data, addr = sock.recvfrom(1024)
    # print("xxx")
    print(data.decode())

    # step 4: do something with it
    # menampilkan hasil pesan dari client
    # print(addr)
    print("Pesan diterima:", data.decode())
    # y = y+1
