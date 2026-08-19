##range(stop)
for i in range(5):
    print (i)
print()
##range(start, stop)
for i in range(1,6):
    print(f"Ethernet1/{i}")
print()
##range(start, stop, step)
for i in range(1,10,2):
    print(f"Ethernet1/{i}")
print()
##range() with a negative step
for i in range(5,0,-1):
    print(f"Ethernet1/{i}")
print()
##range() + List Index
devices = ["Leaf01", "Leaf02", "Spine01"]
for i in range(len(devices)):
    print(i,":", devices[i])
print()
####
devices = ["Leaf01", "Leaf02", "Spine01"]
ips = ["10.10.10.11", "10.10.10.12", "10.10.10.21"]
for i in range(len(devices)):
    print(i, devices[i], ":", ips[i])
print()
###enumerate()
ips = ["10.10.10.11", "10.10.10.12", "10.10.10.21"]
for dev,details in enumerate(ips):
    print(f"{dev}  : {details}")
print()
##enumerate() with a Start Value
devices = ["Leaf01", "Leaf02", "Spine01"]
for dev,details in enumerate(devices,start=1):
    print(f"{dev}  : {details}")
print()
##enumerate() with Two Lists
for index,device in enumerate(devices):
    print(f"{index}  :  {device} : {ips[index]}")
print()

devices = ["Leaf01", "Leaf02", "Spine01", "Leaf03"]
for index,device in enumerate(devices):
    if index %2 == 0:
        print(f"{index} :  {device}")
print()
###
devices = ["Leaf01", "Spine01", "Leaf02", "Spine02", "Leaf03"]
for index,device in enumerate(devices,start=1):
    if device.startswith("Leaf"):
     print(index, ":", device)
print()
###Print only DOWN devices
devices = ["Leaf01", "Leaf02", "Spine01", "Leaf03", "Spine02"]
status = ["UP", "DOWN", "UP", "UP", "DOWN"]
for index,device in enumerate(devices,start=1):
    if status[index -1] == "DOWN":
        print(f"{index} : {device} : {status[index-1]}")
print()
##enumerate() with a List of Dictionaries
devices = [
    {"hostname": "Leaf01", "ip": "10.10.10.11", "vendor": "Cisco"},
    {"hostname": "Leaf02", "ip": "10.10.10.12", "vendor": "Cisco"},
    {"hostname": "Spine01", "ip": "10.10.10.21", "vendor": "Arista"}
]
for index,device in enumerate(devices,start=1):
    print(f"{index}  : {device["hostname"]} : {device["ip"]}")