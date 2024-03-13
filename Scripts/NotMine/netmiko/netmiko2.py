from netmiko import ConnectHandler
from getpass import getpasS

username = 'lgf'
password = getpass()

cisco_ios_r1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.72',
    'username': usermane,
    'password': password
}

cisco_ios_r2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.82',
    'username': username,
    'password': password
}

cisco_ios_r3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.83',
    'username': username,
    'password': password
}

all_devices = (cisco_ios_r1, cisco_ios_r2, cisco_ios_r3)

for devices in all__devices:
    net_connect = ConnectHandler(**devices)
    for n in range (1,4):
        print ("Creating interface loopback " + str(n))
        config_commands = ['interface loopback ' + str(i), f'ip address {n}.{n}.{n}.{n} 255.255.255.255']
        output = net_connect.send_config_set(config_commands)
        print(output) 
