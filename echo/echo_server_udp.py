import socket

# initialize the ip to be addressed
udp_ip = '127.0.0.1'

# koneksi 2 komputer
# 172.20.10.2

# initialize the port to be addressed
udp_port = 5004

# step1 : create socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#step2 : binding
s.bind((udp_ip, udp_port))
print('Mendengarkan di {}'.format(s.getsockname()))

while True:
    msg_bytes, address = s.recvfrom(1024)
    msg_str = msg_bytes.decode('utf-8')
    print('Menerima dari client {} : {}'.format(address, msg_str))
    s.sendto(msg_str.encode(), address)
