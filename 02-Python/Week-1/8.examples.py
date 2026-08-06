print("*" * 50)
interface = "Ethernet1/48"
print("Interface Name  :", interface)
print("Length : ?", len(interface))
print("first character :", interface[0])
print("Last character  :", interface[11])
print("Technology :", interface[0:8])
print("Port no :", interface[-4:])
print("Port no:", interface.split("Ethernet")[1])
print(interface.split())
interface = "Ethernet10/24"
print(interface.split("Ethernet"))
print("Reverse Interface :", interface[::-1])
print("Upper case :", interface.upper())
print("lower case :", interface.lower())
print("*" * 50)

ip = "192.168.100.10"
print("IP Address :", ip)
print("Number of Characters :", len(ip))
print("IP Octets", ip.split('.'))
print("First Octet :", ip.split('.')[0])
print("second Octet :", ip.split('.')[1])
print("Thirdt Octet :", ip.split('.')[2])
print("Fourth Octet :", ip.split('.')[3])
print("#" * 50)

config = """ 
================================
Interface Configuration
================================

interface Ethernet1/10
 description Connected to Spine01
 no shutdown

================================
"""
print(f'switch configuration is .{config}')
print("#" * 50)

hostname = "Leaf10"
print("Hostname startswith L" , hostname.startswith('L'))
print(" found ", hostname.find('1'))