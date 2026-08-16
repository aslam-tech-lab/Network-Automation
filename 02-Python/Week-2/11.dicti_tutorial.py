#A dictionary stores data as key : value pairs.
device = {"hostname": "Leaf01","ip":"192.168.1.1","vendor":"cisco"}
print(device["hostname"])
print(device["ip"])

##Keys Must Be Unique
device = {
       "hostname": "Leaf01",
       "ip":"192.168.1.1",
       "vendor":"cisco",

       "hostname": "Leaf02", 
       "ip":"192.168.1.21",
       "vendor":"cisco",

       "hostname": "Leaf03", 
       "ip":"192.168.1.22",
       "vendor":"cisco"
    }
print(device["hostname"])
print(device["ip"])

#Adding a New Key
device = {"hostname": "Leaf01","ip":"192.168.1.1"}
device["vendor"] = "Cisco"
print(device)
#Updating a Value
device["ip"]= "19.168.2.1"
print(device)
#Checking Whether a Key Exists
print("hostname" in device)

#get() Method If the key doesn't exist, Python returns: none
print(device["hostname"])  # direct access
#print(device["serial"]) #If the key doesn't exist:Python raises a KeyError.
print(device.get("ip"))
print(device.get("serial")) #Python returns: none
print(device.get("serial", "Not available"))#Python returns:Not available

#Removing a Key
device.pop("vendor") #removes and can return the value
print(device)
del device["ip"] #This removes the key-value pair.
print(device)

#Get all dictionary keys:
device = {"hostname": "Leaf01","ip":"192.168.1.1","vendor":"cisco"}
print(device.keys())
#Get the values:
print(device.values())
#Get the Items:
print(device.items())
#Dictionary Length
print(len(device))

##Nested Dictionaries
device = {
    "switch01":{
       "hostname": "Leaf01",
       "ip":"192.168.1.1",
       "vendor":"cisco"
    },
   "switch02": {
       "hostname": "Leaf02", 
       "ip":"192.168.1.21",
       "vendor":"cisco"   
    }}
print(device)
print(device["switch01"]["ip"])
print(device["switch02"]["hostname"])

##Dictionary + List
device = {
    "hostname":"leaf01",
    "ip":"10.10.10.10",
    "vendor":"cisco",
    "interfaces":["Eth1","Eth2","Eth3"]
}
print(device)
print(device["interfaces"])
print(device["interfaces"][0])

#Dictionary + Tuple
device = {
    "hostname":"leaf01",
    "location":("DC1","Rack1","Row1")
}
print(device)
print(device["location"])
print(device["location"][1])

