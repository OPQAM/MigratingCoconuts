import getpass
import telnetlib
import socket

host = "127.0.0.1"
password = getpass.getpass()

f = open ('myrouters.txt')

for ip in f:
    ip = ip.strip()
    print ("Configuring Router " + (ip))
    host = ip
    tn = telnetlib.Telnet(host)
    
    if password:
       tn.read_until(b"Password: ")
       tn.write(password.encode('ascii') + b"\n")
       
       tn.write(b"conf t\n")
       tn.write(b"router ospf 1\n")
       tn.write(b"network 0.0.0.0 255.255.255.255 area 0\n")
       tn.write(b"end\n")
       tn.write(b"wr\n")
    
    tn.get_socket().shutdown(socket.SHUT_WR)
    print(tn.read_all().decode('ascii'))

tn.close()