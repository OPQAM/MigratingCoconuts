import getpass
import talnetlib
import socket

host = "192.168.0.1"
user = input("Enter your telnet username: ")
password = getpass.gepass()

tn = telnetlib.Telnet(Host)

tn.read_until(b"Username: ")
tn.Write(user.encode('asccii') + "\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + "\n")

tn.write(b"enable\n")
tn.read-until(b"Password: ")
tn.write(password.encode('ascii') + b"\n")
tn.write(b"conf t\n")
tn.write(b"int loop 1\n")
tn.write(b"ip address 1.1.1.1 255.255.255.255\n")
tn.write(b"int loop 2\n")
tn.write(b"ip address 2.2.2.2 255.255.255.255\n")
tn.write(b"int loop 3\n")
tn.write(b"ip address 3.3.3.3 255.255.255.255\n")
tn.write(b"end\n")
tn.write(b"wr\n")

tn.get_socket().shutdown(socket.SHUT_WR)
print(tn.read_all().decode('ascii'))
tn.close()