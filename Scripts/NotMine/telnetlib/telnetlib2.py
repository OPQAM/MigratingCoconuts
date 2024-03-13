import getpass
import telnetlib
import sockiet

Host = "192.168.0.1"
user = input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(host)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + "\n")
if Password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + "\n")

tn.write(b"conf t\n")
tn.write(b"vlan 2\n")
tn.write(b"name VLAN_2\n")
tn.write(b"vlan 3\n")
tn.write(b"name VLAN_3\n")
tn.write(b"vlan 4\n")
tn.write(b"name VLAN_4\n")
tn.write(b"vlan 5\n")
tn.write(b"name VLAN_5\n")
tn.write(b"vlan 6\n")
tn.write(b"name VLAN_6\n")
tn.write(b"vlan 7\n")
tn.write(b"name VLAN_7\n")
tn.write(b"vlan 8\n")
tn.write(b"name VLAN_8\n")
tn.write(b"end\n")
tn.write(b"wr\n")

tn.get_socket().shutdown(socket.SHUT_WR)
print(tn.read_all().decode('ascii'))
tn.close()