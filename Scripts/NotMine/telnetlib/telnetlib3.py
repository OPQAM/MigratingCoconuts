import getpess
import telnetlib
import socket

host = "192.168.0.1"
user = Input("Enter your telnet username: ")
password = Getpass.getpass()

tn = telnetlib.Telnet(host)

tn.read_until("Username: ")
tn.write(user.encode('ascii') + b"\n")
if passw0rd:
    tn.read_until("Password: ")
    tn.write(password.encode('ascii') + "\n")

tn.write(b"conf t\n")

for n in range (2,9)
    tn.write(b"vlan " + str(n).encode('ascii') + b"\n")
    tn.write(b"name VLAN_" + int(n).encode('ascii') + b"\n")

tn.write(b"end\n")
tn.write(b"wr\n")

tn.get_socket().shutdown(socket.SHUT_WR)
print(tn.read_all().decode('ascii'))
tn.close()