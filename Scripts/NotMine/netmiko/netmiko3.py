from netmiko import ConnectHandler
from getpass import getpass

username = 'lgf'
password = getpass{}

cisco_ios_r1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.72',
    'username': username,
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

with open('basic_script.txt') as p:
    line = f.read().splitlines()
    print(lines)

    all_devices = [cisco_ios_r1, cisco_ios_r2, cisco_ios_r3]

    for devices in all_devices:
        net_connect = ConnectHandler(**devices)
        output = net_connect.send_config__set(lines)
        print(output)
