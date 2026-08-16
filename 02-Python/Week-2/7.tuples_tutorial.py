# A tuple is like a list, but you normally use it when the collection should not be changed,
#  Once this information is created, you may want to pass it around your program without allowing accidental modification.
# This is one reason tuples exist 

## Creating a Tuple ##
device = ("Leaf01", "192.168.1.0", "Cisco")
print(device)
print(device[0])
print(device[1])

##List vs Tuple list you can modify it but tuple you cant ##
device = ["leaf01",'leafo2','leafo3']
print(device)
device[0] = "Spine01"
print(device)

devices = ("Leaf01", "192.168.1.0", "Cisco")
#devices[0]= "Spine01"
print(devices) ## TypeError: 'tuple' object does not support item assignment

## Tuple Indexing and slicing ##
device = ("Leaf01", "192.168.0.1", "Cisco", "10.2(3)")
print(device[1])
print(device[0:2])
print(device[-2:])

##len() Works With Tuples ##
device = ("Leaf01", "192.168.0.1", "Cisco", "10.2(3)")
print(len(device))

##in Works With Tuples ##
vendors = ("Cisco","Juniper", "Atista", "HPE")
print("HPE" in vendors)
print("HP" in vendors)

##Tuple Methods Tuples have fewer methods than lists because you cannot modify them ##
vendors = ("Cisco","Juniper", "Atista", "HPE","Dell")
print(vendors.count("Cisco"))
print(vendors.index("HPE"))

##Tuple Packing  Even though you didn't write parentheses, Python creates a tuple. ##
device = "Spine01", "192.168.1.20", "Cisco"
print(device)

## Tuple Unpacking ##
## Suppose
device = ("Spine01", "192.168.20.10", "Juniper")
## you can do
hostanme,ip,vednor = device
print(hostanme)
print(ip)

##The Single-Element Tuple Trap ##
device = ("Leaf01")
print(type(device)) ## it is a string not a tuple
device = ("spine01",) ## To create a tuple containing one element, you need the comma
print(type(device))

