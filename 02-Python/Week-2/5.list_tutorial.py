## without a list ##
device1 = "Leaf01"
device2 = "Leaf02"
device3 = "Leaf03"
device4 = "Leaf04"

## With List ##
devices = ["Leaf01","Leaf02","Leaf03","Leaf04"]
ips = ["192.168.1.1","192.168.1.2","192.168.1.3","192.168.1.4"]
vlans = [10,20,300,400]
print(devices)

### Creating a List###
devices = ["Leaf01","Leaf02","Leaf03","Leaf04"]
device_info = ["Leaf01",'192.168.1.1',300,True]
print(device_info)

##Lists Are Ordered##
devices = ["Leaf01","Leaf02","Leaf03","Leaf04"]
print(devices[0])

##Negative Indexing##
print(devices[-1])
print(devices[-2])

##Changing a List Element Lists are mutable##
devices = ["Leaf01", "Leaf02", "Leaf03"]
devices[1] = "Leaf02-new"
print(devices)

##Adding Elements##
devices = ["Leaf01", "Leaf02", "Leaf03"]
devices.append("Leaf04")
print(devices)
  ##Network example:
device=[]
device.append("Spine01")
device.append("Spine02")
device.append("Spine03")
print(device)

##insert()  list.insert(index, value) ##
device = ["Agg1","Agg2","Agg3"]
device.insert(3,"Tor1")
print(device)

##extend() list.extend(new list name)
inventory = ["Tor1","Tor2"]
new_inventory = ["Tor3","Tor4"]
inventory.extend(new_inventory)
print(inventory)

##append() vs extend()##
inventory = ["Tor1","Tor2"]
inventory.append(["Tor3","Tor4"])
inventory.append("Tor3")
inventory.extend(["Tor3","Tor4"])
print(inventory)

##Removing Elements##
inventory = ["Tor1","Tor2"]
inventory.remove("Tor1")
print(inventory)

##pop() Remove by index: ##
device = ["Agg1","Agg2","Agg3"]
device.pop(2)
print(device)
removed_device = device.pop(1)
print(removed_device)

##len()##
inventory = ["Tor1","Tor2"]
print(len(inventory))

##Checking Whether Something Exists##
device = ["Agg1","Agg2","Agg3"]
print("Agg3" in device)
allowed_vlans = [10, 20, 30, 40]
vlan = 20
print(vlan in allowed_vlans)

##Slicing ##
devices = ["Leaf01", "Leaf02", "Leaf03", "Leaf04", "Leaf05"]
print(devices[1:4])
print(devices[:4])
print(devices[1:])
print(devices[-2:])

##Sorting##
devices = ["Leaf03", "Leaf01", "Leaf02"]
devices.sort()
print(devices)
devices.sort(reverse=True) ## it will print Descending
print(devices)
devices.sort(reverse=False) ## it will print Ascending
print(devices)

##count()##
vlans = [10,20,300,400,300,20,40,10,30,20]
count = vlans.count(10)
count1 = vlans.count(20)
print(count)
print(count1)

##index()
devices = ["Leaf01", "Leaf02", "Leaf03", "Leaf04", "Leaf05"]
print(devices.index("Leaf03"))

