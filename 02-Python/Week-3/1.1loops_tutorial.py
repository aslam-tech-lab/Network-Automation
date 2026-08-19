#loops through list
devices = ["Leaf01","Leaf02","Leaf03","Spine01"]
for device in devices:
    print(device)

interfaces = ["Etherent1/1","Etherent1/2","Etherent1/3"]
for interface in interfaces:
    print(f"Interface   :  {interface}")

vlans = [10,20,30,40,100]
for vlan in vlans:
    print(f"VLAN  : {vlan}")
print()

devices = ["Leaf01","Leaf02","Leaf03","Spine01","Spine02","Leaf04"]
for device in devices:
    if device.startswith("Leaf"):
        print(device)
print()

interfaces = ["Etherent1/1","Etherent1/2","Etherent1/3","Etherent1/4"]
count = 0
for interface in interfaces:
    count+=1
print(f"Total interfaces is    :  {count}")
print()

interfaces = ["Etherent1/1 is up","Etherent1/2 is down","Etherent1/3 is up","Etherent1/4 is down","Etherent1/5 is up"]
up_count = 0
for interface in interfaces:
    if "up" in interface:
        up_count+=1
print(f"Total up interfaces   :  {up_count}")
print()
for interface in interfaces:
    if "down" in interface:
        print(interface)
print()
devices = [
    "Leaf01 Cisco",
    "Leaf02 Cisco",
    "Spine01 Arista",
    "Leaf03 Cisco",
    "Spine02 Arista"
]
for device in devices:
    if "Cisco" in device:
        print(device)
print()
cisco_devices=[]
for device in devices:
    if "Cisco" in device:
        cisco_devices.append(device)
print(f"Cisco device list is : {cisco_devices}")
print()
arista_devices=[]
for device in devices:
    if "Arista" in device:
        arista_devices.append(device)
print(f"Arista device list is : {arista_devices}")
print()
uppercase_devices = []
for device in devices:
    uppercase_devices.append(device.upper())
print(uppercase_devices)
print()
interfaces = [
    "ethernet1/1",
    "ethernet1/2",
    "ethernet1/3"
]
interface_names = []
for interface in interfaces:
    interface_names.append(interface.upper())
print(interface_names)
print()

## enumerate
for number,interface in enumerate(interfaces,start=1):
    print(number, ":",interface)
print()
### range()
for i in range(len(interfaces)):
    print(i, interfaces[i])
print()

## for else
device1 = ["Leaf01","Leaf02","Leaf03","Spine01","Spine02","Leaf04"]
for device in device1:
    print(f"Checking   {device}")
else:
    print(f"Validation completed")
print()
## for els break
for device in device1:
    if device == "Spine02":
        print(f"{device} is found")
        break
else:
    print("Spine02 is not found")
print()
##continue inside a loop Use continue to skip all Spine devices and print:
for device in device1:
    if "Spine" in device:
        continue
    print(f"Checking  {device}")
print()
#### range() one more example
interfaces = ["Eth1/1", "Eth1/2", "Eth1/3"]
for i in range(len(interfaces)):
    print(f"Interface {i+1} : {interfaces[i]}")
print()
#### enumerate() one more example
for number,interface in enumerate(interfaces,start=1):
    print(f"{number} : {interface}")
print()
### ZIP() function
hostnames = ["Spine01", "Spine02", "Leaf01"]
mgmt_ips = ["10.10.10.21", "10.10.10.22", "10.10.10.11"]
for name,ip in zip(hostnames,mgmt_ips):
    print(f"{name}  : {ip}")
  ## To see the pairs:
new = zip(hostnames,mgmt_ips)
print(list(new))
print()
interfaces = ["Ethernet1/1", "Ethernet1/2", "Ethernet1/3"]
vlans = [10, 20, 30]
for interface,vlan in zip(interfaces,vlans):
    print(f"{interface}  : VLAN {vlan}")
print()
devices = ["Leaf01", "Leaf02", "Spine01"]
ips = ["10.10.10.11", "10.10.10.12", "10.10.10.21"]
platforms = ["Nexus9000", "Nexus9000", "Nexus9000"]
for device,ip,platform in zip(devices,ips,platforms):
    print(f"{device} : {ip}  : {platform}")
  #
  # zip () unequal list lengths  spine01 it wont print
devices = ["Leaf01", "Leaf02", "Spine01"]
ips = ["10.10.10.11", "10.10.10.12"]
for device,ip in zip(devices,ips):
    print(f"{device}  : {ip}")
print()
##zip_longest() — Handling Unequal Lists
from itertools import zip_longest
devices = ["Leaf01", "Leaf02", "Leaf03", "Spine01"]
ips = ["10.10.10.11", "10.10.10.12"]
for device,ip in zip_longest(devices,ips,fillvalue="N/A"):
    print(f"{device}  : {ip}")