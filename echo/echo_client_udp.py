import socket

# initialize the ip to be addressed
udp_ip = '127.0.0.1'

# initialize the port to be addressed
udp_port = 5004

print("Target IP :", udp_ip)

print("Target port: ", udp_port)

# step1 : Create Socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set Time out, so that can't happen deadlock
s.settimeout(3)

while True:
    data = input("Masukan Pesan >")

    # step2 : client can immediately send message; if server not ready, message will be dropped
    s.sendto(data.encode('utf-8'), (udp_ip, udp_port))
    data, address = s.recvfrom(2048)
    text = data.decode('utf-8')
    print('Menerima dari server %s : %s' % (address, text))
