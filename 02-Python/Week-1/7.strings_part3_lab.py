
hostname = " Leaf01 "
vendor = "Cisco"
interface = "Ethernet1/1"
version = "10.4(2)"
ip = "192.168.100.10"
words = ["Network","Automation","Toolkit"]

print(hostname.strip())
print(vendor.upper())
print(vendor.lower())
print(interface.replace("Ethernet", 'Eth'))
print(version.find('4'))
print(ip.split("."))
print(interface.startswith("Ether"))
print(interface.endswith("1/1"))
print(" ".join( words))

print(f"hostname  :  {hostname.strip()}")
print(f'vendor   :  {vendor.upper()}')


print("=" * 50)
print("Device Health Report")
print("=" * 50)
hostname = "LEAF01"
vendor = "Cisco"
platorm = "Nexus9504"
IP_Address = "192.168.100.10"
print("Hostname      :", hostname)
print("Vendor        :", vendor)
print("Platform      :", platorm)
print("IP Address    :", IP_Address)

print("IP Octets     :", IP_Address.split("."))

print("Starts With N ? :", platorm.startswith('N'))

print("Ends With 04 ? :",  platorm.endswith('04'))

print('Hostname Found "01" :', hostname.find("01"))

print("=" * 50)





