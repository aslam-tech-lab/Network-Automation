#Loop through Dictionary Keys
devices = {
    "Leaf01": "10.10.10.11",
    "Leaf02": "10.10.10.12",
    "Spine01": "10.10.10.21"
}
for dev in devices.keys():
    print(dev)
print()
##Loop through Dictionary Values
for dev in devices.values():
    print(dev)
print()
##Loop through Dictionary Key + Value
for dev,ip in devices.items():
    print(f"{dev}  :  {ip}")
print()
##Nested Dictionary: Accessing Values Using the Key
devices = {
    "Leaf01": {"ip": "10.10.10.11", "vendor": "Cisco"},
    "Leaf02": {"ip": "10.10.10.12", "vendor": "Cisco"},
    "Spine01": {"ip": "10.10.10.21", "vendor": "Cisco"}
}
print()
for dev,details in devices.items():
    print(f"{dev}  : {details["ip"]}")
print()
##Nested Dictionary: Outer Loop + Inner Loop
for dev,details in devices.items():
    for key,val in details.items():
        print(f"{dev}  : {val}")
print()
##Nested Dictionary + Inner key filtering
for dev,details in devices.items():
    for key,val in details.items():
        if key == "vendor":
         print(f"{dev}  : {val}")
print()
##Nested Dictionary + Filtering by Value
devices = {
    "Leaf01": {"ip": "10.10.10.11", "vendor": "Cisco"},
    "Leaf02": {"ip": "10.10.10.12", "vendor": "Arista"},
    "Spine01": {"ip": "10.10.10.21", "vendor": "Cisco"}
}
for dev,details in devices.items():
    for key,val in details.items():
        if val == "Cisco":
            print(f"{dev}  : {val}")
print()
##Filter Using Both Key AND Value
for dev,details in devices.items():
    for key,val in details.items():
        if key == "vendor" and val == "Cisco":
            print(f"{dev}  : {val}")
print()
##Fetching a Specific Value Without Inner Loop
devices = {
    "Leaf01": {"ip": "10.10.10.11", "vendor": "Cisco", "platform": "Nexus9000"},
    "Leaf02": {"ip": "10.10.10.12", "vendor": "Arista", "platform": "7050"},
    "Spine01": {"ip": "10.10.10.21", "vendor": "Cisco", "platform": "Nexus9000"}
}
for dev,details in devices.items():
    print(f"{dev}  {details["platform"]}")
print()
##One Loop vs Two Loops
for dev,details in devices.items():
    for key,val in details.items():
        print(f"{dev}  : {key} : {val}")
print()
##Nested Dictionary + Condition on a Specific Field
for dev,details in devices.items():
    if details["vendor"]=="Cisco":
     for key,val in details.items():
      print(f"{dev}  : {key} : {val}")
print()
##Inner-item filtering
for dev,details in devices.items():
    for key,val in details.items():
        if key == "platform":
         print(f"{dev} : {key} : {val} ")
print()
##Outer Filtering with Multiple Conditions
for dev,details in devices.items():
    if details["vendor"]=="Cisco" and details["platform"]=="Nexus9000":
     for key,val in details.items():
      print(f"{dev}  : {key} : {val}")
print()
##Counting Matching Devices
inventory = {
    "Leaf01": {"ip": "10.10.10.11", "vendor": "Cisco", "platform": "Nexus9000"},
    "Leaf02": {"ip": "10.10.10.12", "vendor": "Arista", "platform": "7050"},
    "Leaf03": {"ip": "10.10.10.13", "vendor": "Cisco", "platform": "Nexus3000"},
    "Spine01": {"ip": "10.10.10.21", "vendor": "Cisco", "platform": "Nexus9000"}
}
count = 0
for dev,details in inventory.items():
   if details["vendor"] == "Cisco":
      count+=1
print(f"Cisco devices: {count}")
print()
##Counting by Inner Item
count = 0
for dev,details in inventory.items():
   if details["vendor"] == "Cisco" and details["platform"] == "Nexus9000":
      count+=1
print(f"Nexus9000 devices: {count}")
print()
##Inner Loop + Counting
count = 0
for dev,details in inventory.items():
   for key,val in details.items():
      count+=1
print("Total fields :", count)
print()
##Inner Loop + Conditional Counting
count = 0
for dev,details in inventory.items():
   for key,val in details.items():
    if val == "Cisco":
       count+=1
print("Cisco fields:", count)
print()
##Inner Loop + Conditional Output
for dev,details in inventory.items():
   for key,val in details.items():
      if val == "Cisco":
         print(f"{dev} : {key} : {val}")
print()
##Inner Loop + Multiple Conditions
for dev,details in inventory.items():
   for key,val in details.items():
      if key =="platform" and val == "Nexus9000":
         print(f"{dev} : {key} : {val}")
print()
##Outer Filtering + Inner Loop
for dev,details in inventory.items():
   if details["vendor"]== "Cisco":
      for key,val in details.items():
         if key == "platform": 
          print(f"{dev} : {val}")
print()
for dev,details in inventory.items():
   if details["vendor"]== "Cisco":
      for key,val in details.items():
         if key == "ip" or key == "platform": 
          print(f"{dev} : {key} : {val}")
print()
##.get() Inside Dictionary Loops
devices = {
    "Leaf01": {"ip": "10.10.10.11", "vendor": "Cisco"},
    "Leaf02": {"ip": "10.10.10.12"},
    "Spine01": {"ip": "10.10.10.21", "vendor": "Cisco"}
}
for dev,detail in devices.items():
    vendor = detail.get("vendor", "NA")
    print(dev,vendor)
print()
##Dictionary with Missing Keys
devices = {
    "Leaf01": {
        "ip": "10.10.10.11",
        "vendor": "Cisco",
        "platform": "Nexus9000"
    },
    "Leaf02": {
        "ip": "10.10.10.12",
        "vendor": "Cisco"
    },
    "Spine01": {
        "ip": "10.10.10.21",
        "platform": "Nexus9000"
    }
}
for dev, details in devices.items():
   vendor = details.get("vendor","NA")
   print(f"{dev}  : {vendor}")
print()
##Missing Keys with Different Fields
devices = {
    "Leaf01": {"ip": "10.10.10.11", "vendor": "Cisco", "platform": "Nexus9000"},
    "Leaf02": {"ip": "10.10.10.12", "vendor": "Cisco"},
    "Spine01": {"ip": "10.10.10.21", "platform": "Nexus9000"},
    "Spine02": {"ip": "10.10.10.22"}
}
for dev, details in devices.items():
   vendor = details.get("vendor","NA")
   plat = details.get("platform","NA")
   print(f"{dev}  : {vendor} : {plat}")
print()
##Missing Keys with condition
for dev, details in devices.items():
   vendor = details.get("vendor","NA")
   plat = details.get("platform","NA")
   if vendor == "Cisco":
      print(f"{dev}  : {vendor} : {plat}")
print()
##Nested Dictionary + Missing Data
devices = {
    "Leaf01": {"ip": "10.10.10.11", "vendor": "Cisco", "platform": "Nexus9000"},
    "Leaf02": {"ip": "10.10.10.12", "vendor": "Cisco"},
    "Leaf03": {"ip": "10.10.10.13", "platform": "Nexus3000"},
    "Spine01": {"ip": "10.10.10.21", "vendor": "Cisco", "platform": "Nexus9000"}
}
for dev,details in devices.items():
   vendor = details.get("vendor","NA")
   plat = details.get("platform","NA")
   ip = details.get("ip","NA")
   if vendor == "Cisco":
     print(f"{dev}  : {ip} : {plat}") 
print()
##Create a New Dictionary Using for
devices = {
    "Leaf01": {"vendor": "Cisco"},
    "Leaf02": {"vendor": "Arista"},
    "Spine01": {"vendor": "Cisco"}
}
new_devices = {}
for dev,details in devices.items():
    if details["vendor"]== "Cisco":
       new_devices[dev]= details
print(new_devices)
print()
##Simple Dictionary Comprehension
devices = {
    "Leaf01": {"vendor": "Cisco"},
    "Leaf02": {"vendor": "Arista"},
    "Spine01": {"vendor": "Cisco"}
}
new_devices = {
   dev:details
   for dev,details in devices.items()
   if details["vendor"]== "Cisco"
}
print(new_devices)
  ##one more exampple
inventory = {
    "Leaf01": {"ip": "10.10.10.11", "vendor": "Cisco", "platform": "Nexus9000"},
    "Leaf02": {"ip": "10.10.10.12", "vendor": "Cisco","platform": "900"},
    "Leaf03": {"ip": "10.10.10.13", "platform": "Nexus3000"},
    "Spine01": {"ip": "10.10.10.21", "vendor": "Cisco", "platform": "Nexus9000"}
}
new_inventory={
   dev:details
   for dev,details in inventory.items()
   #if details.get("platform","NA").startswith("Nexus")## this one you can remove platform details in leaf02
   if details["platform"].startswith("Nexus")
}
print(new_inventory)

