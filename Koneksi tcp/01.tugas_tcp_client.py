# import library socket karena akan menggunakan IPC socket
import socket

# definisikan tujuan IP server
# local IP
TCP_IP = '127.0.0.1'
#koneksi 2 komputer
# TCP_IP = '172.20.10.2'

# definisikan port dari server yang akan terhubung
TCP_PORT = 5005

# definisikan ukuran buffer untuk mengirimkan pesan
BUFFER_SIZE = 1024

# definisikan pesan yang akan disampaikan
PESAN = b"Hello World!"

# buat socket TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# lakukan koneksi ke server dengan parameter IP dan Port yang telah didefinisikan
s.connect((TCP_IP, TCP_PORT))

# kirim pesan ke server
s.send(PESAN)

# terima pesan dari server
data = s.recv(BUFFER_SIZE)

# tampilkan pesan/reply dari server
print("Data diterima: ", data)

# tutup koneksi
s.close()
