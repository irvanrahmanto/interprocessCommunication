# import library socket karena akan menggunakan IPC socket
import socket

# definisikan alamat IP binding  yang akan digunakan
TCP_IP = '127.0.0.1'

# definisikan port number binding  yang akan digunakan
TCP_PORT = 5005

# definisikan ukuran buffer untuk mengirimkan pesan
BUFFER_SIZE = 1024

# buat socket bertipe TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Berhasil membuat koneksi socket di", TCP_IP)

# lakukan bind
s.bind((TCP_IP, TCP_PORT))

# server akan listen menunggu hingga ada koneksi dari client
s.listen()
print("server running", TCP_PORT)

# lakukan loop forever
while 1:
    # menerima koneksi
    conn, addr = s.accept()
    # menampilkan koneksi berupa IP dan port client yang terhubung menggunakan print
    print("Alamat: ", addr)

    # menerima data berdasarkan ukuran buffer
    data = conn.recv(BUFFER_SIZE)

    # menampilkan pesan yang diterima oleh server menggunakan print
    print("data diterima:", str(data))

    # mengirim kembali data yang diterima dari client kepada client
    conn.send(data)

# tutup koneksi
s.close()
