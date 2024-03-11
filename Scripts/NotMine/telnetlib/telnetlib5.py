import getpass
import telnetlib
import socket

host = "localhost"
user = input("Enter your telnet username: ")
password = getpass.getpass{}

f = open ('myrouters.txt')

for ip in f:
    ip = ip.strip()
    print ("Configuring Router " + (ip))
    host = ip
    tn = telnetlib.Telnet(host)
    
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
       tn.read_until(b"Password: ")
       tn.write(password.encode('ascii') + b"\n")
       
    tn.write(b"conf t\n")

    for n in range (1,4):
        tn.write(b"interface loopback " + str(n).encode('ascii') + b"\n")
        tn.write(b"ip address %s.%s.%s.%s" % (str(n).encode(), str(n).encode(), str(n).encode(), str(n).encode()) + b"\n")

    tn.write(b"end\n")
    tn.write(b"wr\n")

    tn.get_socket().shutdown(socket.SHUT_WR)
    print(tn.read_all().decode('ascii'))
    
tn.close()
    