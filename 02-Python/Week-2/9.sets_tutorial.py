## A set is a python collection used to store unique values.
vendors = {"cisco","cisco","Juniper","cisco","Juniper","Dell","HPE","Dell"}
print(vendors)

## LIST vs SET  ##
vendors = {"cisco","cisco","Juniper","cisco","Juniper","Dell","HPE","Dell"}
print(vendors)

vendors = ["cisco","cisco","Juniper","cisco","Juniper","Dell","HPE","Dell"]
print(vendors)

##Why Sets Are Useful in Network Automation
#Imagine you collect vendor information from 20 switches:
vendors = [
    "Cisco",
    "Cisco",
    "Cisco",
    "Arista",
    "Cisco",
    "Juniper",
    "Arista"
]
#Instead of manually removing duplicates:
new_vendors= set(vendors)
print(new_vendors)

##Creating a Set
devices = {"leaf01","leaf02","leaff03"}
print(devices)
# empty set
devices = set()

##Sets Don't Use Indexes Because sets are unordered collections and don't support positional indexing
devices = {"leaf01","leaf02","leaff03"}
#print(devices[0]) ##TypeError: 'set' object is not subscriptable

#Sets Automatically Remove Duplicates
interfaces = {"Et1/1","Et1/2","Et1/1","Et1/3","Et1/4","Et1/2"}
print(interfaces)

#Adding to a Set — add()
devices = {"Spine01","Spine02"}
devices.add("Spine03")
print(devices)

##Adding Multiple Values — update()
devices = {"leaf01","leaf02","leaf03"}
devices.update({"spine01","spine02"})
print(devices)
  # You can also update from a list:
devices.update(["Tor1","Tor2"])
print(devices)

##Removing from a Set
devices = {"leaf01","leaf02","leaf03"}
devices.remove("leaf01")
print(devices)
devices = {"leaf01","leaf02","leaf03"}
devices.difference_update({"leaf02","leaf03"})
print(devices)

#remove() vs discard()
devices = {"leaf01","leaf02","leaf03"}
#devices.remove("leaf0") #If Leaf99 doesn't exist, Python raises an error.
devices.discard("leaf01")
print(devices)
devices.discard("leaf")
print(devices)

#in With Sets
allowed_vendors = {"Cisco","Juniper","Dell"}
print("Juniper" in allowed_vendors)

#Union
site_a = {"Leaf01","Leaf03","Leaf04","Spine01"}
site_b = {"Leaf02","Leaf04","Spine02"}
print(site_a | site_b)
print(site_a.union(site_b))## anotherway of union
 ## Intersection
print(site_a & site_b) # Values that exist in both sets.
common = site_a & site_b
print(common)
##Difference  Values that exist in the first set but not the second.
diff = site_a - site_b
print(diff)
##Symmetric Difference  Give me devices that are present in only one of the two sets, excluding common devices.
difference = site_a ^ site_b
print(difference)


