hostname = "switch-1A"
vendor = 'cisco'
model = 'nexus-9000'
ip_address = "192.168.1.10"
print(hostname)
print(vendor)
print(model)
print(type(hostname))
print("lenth of vendor is ", len(vendor))
print("lenth of model is " , len(model))
print("hostname \t ipaddress")
print("=" * 50)
config = """
configure terminal
interface ethernet1/1
switchport mode access
switchport access vlan 200
no shudown
"""
print(config)
print("=" * 50)



