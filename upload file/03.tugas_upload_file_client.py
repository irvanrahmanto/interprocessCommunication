# mengirimkan file ke server
# idenya adalah tidak mengirimkan file langsung secara keseluruhan tetapi per bagian
# contoh: file ukuran 1 MB, buffer ukuran 1KB maka client akan mengirimkan 1KB sebanyak 1000 kali

# import library socket karena menggunakan IPC socket
import socket
import io

# definisikan IP server tujuan file akan diupload
IP = "127.0.0.1"

# Koneksi 2 komputer
# IP = "172.20.10.2"

# definisikan port number proses di server
PORT = 5004

# definisikan ukuran buffer untuk mengirim
BUFFER_SIZE = 1024

# langkah 1: buatlah socket (apakah bertipe UDP atau TCP?)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# langkah 2: lakukan koneksi ke server
socket.connect((IP, PORT))

# langkah 3: buka file yang akan diupload
# buka file bernama "file_diupload.txt gunakan tipe byte ketika membuka file
# masih hard code, file harus ada dalam folder yang sama dengan script python
f = open("ggg.jpeg", 'wb')


try:
        # langkah 4: setelah file dibuka, baca isi dari file tersebut sebesar buffer
    byte = f.read(BUFFER_SIZE)

    # langkah 5: selama masih ada yang bisa dibaca dari file maka kirimkan part dari file tersebut ke server
    # selama tidak END OF FILE; pada pyhton EOF adalah b''
    while byte != b'':
        # kirim hasil pembacaan file
        socket.send(byte)

        # baca sisa file hingga EOF
        byte = f.read(BUFFER_SIZE)

        # print(byte)
finally:
    print("end sending")

    # langkah 6: tutup file jika semua file telah  dibaca
    f.close()


# langkah 7: tutup koneksi setelah file terkirim
socket.close()
