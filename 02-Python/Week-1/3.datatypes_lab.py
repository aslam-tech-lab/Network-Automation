device_hostname = "Switch-1"
management_ip = '192.168.1.2'
platorm = 'nexus-9000'
vlan = 300
cpu_usage = 22.5
interface_up = True
gateway = None

print("=" * 50)

print(type(device_hostname))
print(type(management_ip))
print(type(platorm))
print(type(vlan))
print(type(cpu_usage))
print(type(interface_up))
print(type(gateway))

print("=" * 50)

print(id(management_ip))
print(id(vlan))

print("=" * 50)
hostname = 'Leaf-'
hostname1 = '1A'
device_name = hostname + hostname1
print(device_name)
vlan = 400
print(vlan + 1)
print("=" * 50)


