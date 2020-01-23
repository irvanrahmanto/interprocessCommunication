# import library socket karena menggunakan IPC socket
import socket

# definisikan IP server tujuan file akan diupload
IP = "127.0.0.1"

# definisikan port number proses di server
PORT = 5004

# definisikan ukuran buffer untuk mengirim
BUFFER_SIZE = 1024

# buat socket (apakah bertipe UDP atau TCP?)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# lakukan koneksi ke server
socket.connect((IP, PORT))

# buka file bernama "hasil_download.txt bertipe byte
# masih hard code, file harus ada dalam folder yang sama dengan script python
f = open('hasil_download.txt', 'w')

# client loop forever menerima kiriman file dari server
while 1:
    # terima pesan dari client
    data = socket.recv(BUFFER_SIZE)

    # tulis pesan yang diterima dari server ke file kita (hasil_download.txt)
    f.write(data.decode('utf-8', 'strict'))

    # berhenti jika sudah tidak ada pesan yang dikirim
    if not data:
        break

# tutup file_hasil_download.txt
f.close()

# tutup socket
socket.close()
