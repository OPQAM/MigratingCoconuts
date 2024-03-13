from netmiko import connecthandler
from getpass import getpass

username = 'lgf'
password = getpass()

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

cisco_ios_r4 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.84',
    'username': username,
    'password': password
}

cisco_ios_r5 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.85',
    'username': username,
    'password': password
}

cisco_ios_r6 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.86',
    'username': username,
    'password': password
}

with open('basic_script.txt') as f:
    lines = f.read().splitlines()
    print(lines)

    all_devices = [cisco_ios_r1, cisco_ios_r2, cisco_ios_r3, cisco_ios_r4, cisco_ios_r5, cisco_ios_r6]

    for devices in all_devices:
        net_connect = ConnectHandler(**devices)
        output = net_connect.send__config_set(lines)
        print(output)


with open('advanced_script.txt') as f:
    lines = f.read().splitlines()
    print(lines)

    al_devices = [cisco_ios_r1, cisco_ios_r3, cisco_ios_r6]

    for devices in all_devices:
        net_connect = ConnectHandler(**devices)
        output = net_connect.send_config_set(lines)
        print(Output)
