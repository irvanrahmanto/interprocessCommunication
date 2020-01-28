# import library socket karena menggunakan IPC socket
import socket

# definisikan IP untuk binding
IP = "127.0.0.1"
# Koneksi 2 komputer
# "172.20.10.2"

# definisikan port untuk binding
PORT = 5004

# definisikan ukuran buffer untuk menerima pesan
BUFFER_SIZE = 1024

# langkah 1: buat socket (bertipe UDP atau TCP?)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# langkah 2: lakukan binding ke IP dan port
socket.bind((IP, PORT))

# langkah 3: lakukan listen
socket.listen()

#  langkah 4: siap menerima koneksi
c, addr = socket.accept()

print('Connection address:', addr)

# buka/buat file bernama hasil_upload.txt untuk menyimpan hasil dari file yang dikirim server
# masih hardcoded nama file, bertipe byte
f = open('ggg.jpeg', 'wb', BUFFER_SIZE)


# server akan loop forever menerima pesan dari client
while 1:
    # terima pesan dari client
    data = c.recv(BUFFER_SIZE)

    # tulis pesan yang diterima dari client ke file yang diinginkan yaitu hasil_upload.txt
    f.write(data)

    # berhenti jika sudah tidak ada pesan yang dikirim
    if not data:
        break

# tutup file result.txt
f.close()

# tutup socket
socket.close()

# tutup koneksi
c.close()
