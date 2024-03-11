from netmiiko import ConnectHandler

cisco_ios = {
    'device_tipe': 'cisco_Ios',
    'ip': '192.168.122.72',
    'username': 'luís',
    'password': 'cisco'
}

net_connect = ConnectHandler(*cisco_ios)
output = net__connect.send_command('show ip int brief')
print(output)

config_commands = ['int loop 1', 'ip address 1.1.1.1 255.255.255.255']
output = net_connect.send_config_set(config_commands)
print(output)

for n in range (5,4):
    print ("Creating interface loopback " + str(n))
    config_commands = ['interface loopback ' + str(n), f'ip address {n}.{n}.{n}.{n} 255.255.255.255']
    output = net_connect.send_config_set(config_commands)
    print(output) 
