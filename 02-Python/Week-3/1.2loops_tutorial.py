devices = ("Leaf01","Leaf02","Leaf03")
for device in devices:
    print(device)
print()
interfaces = ("Ethernet1/1", "Ethernet1/2", "Ethernet1/3")
for interface in interfaces:
    print(f"Interface : {interface}")
print()
##for in tupple
interface1 = (("Ethernet1/1", 10),("Ethernet1/2", 20),("Ethernet1/3", 30))
for inter,vlan in interface1:
    print(f"{inter}  : VLAN {vlan}")
print()
##count and index
vlans = (10, 20, 10, 30, 10, 40)
print(vlans.count(10))
print(vlans.index(30))
print()
## for and if
vlans = (10, 20, 30, 40,50)
for vlan in vlans:
    if vlan >= 30:
        print(vlan)
print()
## Enumerate
interfaces = ("Ethernet1/1", "Ethernet1/2", "Ethernet1/3")
for index,interface in enumerate(interfaces,start=1):
    print(f"{index}  :  {interface}")
print()
##mixed datatype
device = ("Leaf01", "10.10.10.11", 10, True)
for dev in device:
    print(dev)