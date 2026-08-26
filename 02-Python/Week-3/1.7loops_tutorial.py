###Nested loops
devices = ["Leaf01", "Leaf02", "Spine01"]
interfaces = ["Eth1/1", "Eth1/2"]
for dev in devices:
    #print(dev)
    for interface in interfaces:
        print(dev,":",interface)
print()
##Nested loops with List of Dictionaries
devices = [{"hostname": "leaf01","vendor": "Cisco"},
           {"hostname": "leaf02","vendor": "Cisco"},
           {"hostname": "spine01","vendor": "Arista"}
    ] 
interfaces = ["Eth1/1", "Eth1/2"]
for dev in devices:
    for interface in interfaces:
        print(f'{dev["hostname"]} : {interface}')
print()
###Each Device Has Its Own Interfaces
devices = [
    {
        "hostname": "Leaf01",
        "vendor": "Cisco",
        "interfaces": ["Eth1/1", "Eth1/2"]
    },
    {
        "hostname": "Leaf02",
        "vendor": "Cisco",
        "interfaces": ["Eth1/1", "Eth1/2", "Eth1/3"]
    },
    {
        "hostname": "Spine01",
        "vendor": "Arista",
        "interfaces": ["Eth1/1"]
    }
]
for dev in devices:
    #print(dev)
    for interface in dev["interfaces"]:
        print(f'{dev["hostname"]} -> {interface}')
print()
###Add filtering inside the nested loop
for dev in devices:
    if dev["vendor"] == "Cisco":
        for interface in dev["interfaces"]:
            print(f'{dev["hostname"]} -> {interface}')
print()
### Filtering inside the inner loop with interfaces in dict
devices = [
    {
        "hostname": "Leaf01",
        "vendor": "Cisco",
        "interfaces": [
            {"name": "Eth1/1", "status": "UP"},
            {"name": "Eth1/2", "status": "DOWN"}
        ]
    },
    {
        "hostname": "Leaf02",
        "vendor": "Cisco",
        "interfaces": [
            {"name": "Eth1/1", "status": "UP"},
            {"name": "Eth1/2", "status": "UP"},
            {"name": "Eth1/3", "status": "UP"}
        ]
    }
]
for dev in devices:
    for interface in dev["interfaces"]:
        if interface["status"]=="DOWN":
            print(f'{dev["hostname"]} -> {interface["name"]} -> {interface["status"]}')
print()
## enumerate() inside Nested Loops
for dev in devices:
    for index,interface in enumerate(dev["interfaces"],start=1):
        print(f'{dev["hostname"]} : {index} : {interface["name"]}')
##continue
for dev in devices:
    for interface in dev["interfaces"]:
        if interface["status"]=="DOWN":
            continue
        print(f'{dev["hostname"]}: {interface["name"]}: {interface["status"]}')
print()
##Nested loops + break
for dev in devices:
    for interface in dev["interfaces"]:
        if interface["name"] == "Eth1/1":
            print(f'{dev["hostname"]} : {interface["name"]} : found')
            break
print()
##break + else
search_interface = "Eth1/3"
for dev in devices:
    for interface in dev["interfaces"]:
        if interface["name"] == search_interface:
            print(f'{dev["hostname"]}: {search_interface}: found')
            break
    else:
        print(f'{dev["hostname"]}: {search_interface}: not found')
print()
### MINI project
devices = [
    {
        "hostname": "Leaf01",
        "vendor": "Cisco",
        "interfaces": [
            {"name": "Eth1/1", "status": "UP"},
            {"name": "Eth1/2", "status": "DOWN"}
        ]
    },
    {
        "hostname": "Leaf02",
        "vendor": "Cisco",
        "interfaces": [
            {"name": "Eth1/1", "status": "UP"},
            {"name": "Eth1/2", "status": "UP"},
            {"name": "Eth1/3", "status": "DOWN"}
        ]
    },
    {
        "hostname": "Spine01",
        "vendor": "Arista",
        "interfaces": [
            {"name": "Eth1/1", "status": "UP"}
        ]
    }
]
search_interface = "Eth1/3"
for dev in devices:
    if dev["vendor"]== "Arista":
        continue
    for index,interface in enumerate(dev["interfaces"],start=1):
        print(f'{dev["hostname"]} : Interface {index} : {interface["name"]}: {interface["status"]}')
        if interface["name"] == search_interface:
            print(f'{dev["hostname"]} : {search_interface} found')
            break
    else:
        print(f'{dev["hostname"]} : {search_interface} not found')



print()
devices = {
    "Leaf01": {
        "vendor": "Cisco",
        "interfaces": {
            "Eth1/1": "UP",
            "Eth1/2": "DOWN"
        }
    },
    "Leaf02": {
        "vendor": "Cisco",
        "interfaces": {
            "Eth1/1": "UP",
            "Eth1/2": "UP"
        }
    }
}
for dev,details in devices.items():
    for interface,status in details["interfaces"].items():
        if status == "DOWN":
         print(f"{dev} : {interface} : {status}")


print()
devices = {
    "Leaf01": {
        "vendor": "Cisco",
        "status": "UP",
        "interfaces": {
            "Eth1/1": "UP",
            "Eth1/2": "DOWN"
        }
    },
    "Leaf02": {
        "vendor": "Cisco",
        "status": "DOWN",
        "interfaces": {
            "Eth1/1": "UP",
            "Eth1/2": "DOWN"
        }
    },
    "Spine01": {
        "vendor": "Arista",
        "status": "UP",
        "interfaces": {
            "Eth1/1": "DOWN",
            "Eth1/2": "UP"
        }
    }
}
for dev,details in devices.items():
    if details["status"]=="UP":
        for interface,value in details["interfaces"].items():
            if value == "DOWN":
             print(f'{dev} : {interface} : {value}')

print()
###enumerate() + .items() + tuple unpacking
for dev,details in devices.items():
    if details["vendor"]=="Cisco" and details["status"]=="UP":
            for index,(interface,value) in enumerate(details["interfaces"].items(),start=1):##enumerate() + .items() + tuple unpacking
                if value=="DOWN":
                 print(f'{dev} : Interface {index} : {interface}: {value}')

print()
interfaces = {
    "Eth1/1": "UP",
    "Eth1/2": "DOWN",
    "Eth1/3": "UP"
}
for index,(key,val) in enumerate(interfaces.items(),start=1):
 #if val == "DOWN":
  print(f'{index} : {key} : {val}')

print()
##Network Automation Example
devices = {
    "Leaf01": {
        "vendor": "Cisco",
        "status": "UP",
        "interfaces": {
            "Eth1/1": "UP",
            "Eth1/2": "DOWN"
        }
    },
    "Leaf02": {
        "vendor": "Arista",
        "status": "UP",
        "interfaces": {
            "Eth1/1": "DOWN",
            "Eth1/2": "DOWN"
        }
    },
    "Spine01": {
        "vendor": "Cisco",
        "status": "DOWN",
        "interfaces": {
            "Eth1/1": "DOWN"
        }
    }
}
for dev,details in devices.items():
    if details["vendor"]=="Cisco" and details["status"]=="UP":
        for index,(interface,status)in enumerate(details["interfaces"].items(),start=1):
            if status == "DOWN":
             print(f'{dev} : {index} : {interface} : {status}')
print()
for attempt in range(5, 0,-1):
    print(f"Checking device... attempt {attempt}")
print()

attempt = 1
device = "Leaf01"
while attempt <= 5:
    print(f"Checking {device}... attempt {attempt}")
   
    if attempt ==3:
     print(f"{device} is UP")
     break
    attempt+=1      

print()
attempt =1
device = "Leaf01"
while attempt <=5:
    print(f'Checking... attempt {attempt}')
    if attempt == 4:
        print(f'{device} is UP')
        break
    attempt+=1
else:
    print("Leaf01 did not respond")

print()
devices = [
    {
        "hostname": "Leaf01",
        "vendor": "Cisco",
        "status": "UP",
        "interfaces": {
            "Eth1/1": "UP",
            "Eth1/2": "UP"
        }
    },
    {
        "hostname": "Leaf02",
        "vendor": "Cisco",
        "status": "UP",
        "interfaces": {
            "Eth1/1": "DOWN",
            "Eth1/2": "UP",
            "Eth1/3": "DOWN",
            "Eth1/4": "DOWN"
        }
    },
    {
        "hostname": "Spine01",
        "vendor": "Arista",
        "status": "UP",
        "interfaces": {
            "Eth1/1": "DOWN"
        }
    },
    {
        "hostname": "Leaf03",
        "vendor": "Cisco",
        "status": "DOWN",
        "interfaces": {
            "Eth1/1": "DOWN"
        }
    }
]
for dev in devices:
    #print(dev)
    if dev["vendor"]=="Arista":
        continue
    if dev["status"]!="UP":
        continue
   # print(dev["interfaces"])
    found_down = False
    for index,(interface,status) in enumerate(dev["interfaces"].items(),start=1):
      if status == "DOWN":
          print(f'{dev["hostname"]}: {index} : {interface} : {status}')
          found_down = True
      if interface == "Eth1/3":
          break
    else:
        if not found_down:
         print(f'{dev["hostname"]}: All interfaces UP')
                       
          