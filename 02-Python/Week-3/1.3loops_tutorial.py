vlans = {10,20,30,40}
print(vlans)
##Convert it to a set and use a for loop to print the unique VLANs.
vlans = [10, 20, 10, 30, 20, 40, 30]
new_vlans = set(vlans)
print(new_vlans)
for vlan in new_vlans:
    print(vlan)
print()
## using if
allowed_vlans = {10, 20, 30, 40}
if 30 in allowed_vlans:
    print("vlan 30 is allowed")
print()
## counting
vlans = {10, 20, 30, 40, 50}
count = 0
for vlan in vlans:
    if vlan >=30:
        count+=1
print(f"VLANs >= 30:  : {count}")
print()
## startswith
interfaces ={"Ethernet1/1","Ethernet1/2","Ethernet2/1","Ethernet2/2"}
for interface in interfaces:
    if interface.startswith("Ethernet1"):
        print(interface)
print()
##nested structure containing a set
devices = {"Leaf01" :{10,20,30},
           "Leaf02" :{20,30,40}
           }
for dev,vlans in devices.items():
    for vlan in vlans:
        print(f"{dev}  : {vlan}")
print()
inventory = {
    "Leaf01": {"SSH", "SNMP", "NTP"},
    "Leaf02": {"SSH", "NTP"},
    "Spine01": {"SSH", "BGP"}
}
for dev,protocol in inventory.items():
    for proto in protocol:
        print(f"{dev}  : {proto}")