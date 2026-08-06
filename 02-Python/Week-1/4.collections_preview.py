vlan_id = 100
hostname = " Leaf-1"

hostnames = ['Leaf-1A','Leaf-12A','Leaf-3A']
device_inventory = {'hostname': 'Leaf-1A','management_ip':'192.168.1.1','version': '10.2'}
credentials = ('admin','password123')
vlans = {100,200,300,100,400,300,200,220,341}

print("=" * 50)
print(type(vlan_id))
print(type(hostname))
print(type(hostnames))
print(type(device_inventory))
print(type(credentials))
print(type(vlans))
print("=" * 50)

print(device_inventory)
print(vlans)
print(hostnames)
print(credentials)


