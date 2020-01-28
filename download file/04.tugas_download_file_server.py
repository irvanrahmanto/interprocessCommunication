# import library socket karena menggunakan IPC socket
import socket

# definisikan IP untuk binding
IP = '172.20.10.2'

# definisikan port untuk binding
PORT = 5004

# definisikan ukuran buffer untuk menerima pesan
BUFFER_SIZE = 1024

# buat socket (bertipe UDP atau TCP?)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# lakukan binding ke IP dan port
socket.bind((IP, PORT))

# lakukan listen
socket.listen()

#  siap menerima koneksi
c, addr = socket.accept()

# buka file bernama "file_didownload.txt
# masih hard code, file harus ada dalam folder yang sama dengan script python
f = open('tes.jpeg', 'rb')

try:
    # baca file tersebut sebesar buffer
    byte = f.read(BUFFER_SIZE)

    # selama tidak END OF FILE; pada pyhton EOF adalah b''
    while byte != b'':
        # kirim hasil pembacaan file dari server ke client
        c.send(byte)

        # baca sisa file hingga EOF
        byte = f.read(BUFFER_SIZE)


finally:
    print("end sending")

    # tutup file jika semua file telah  dibaca
    f.close()


# tutup socket
socket.close()


# tutup koneksi
c.close()
