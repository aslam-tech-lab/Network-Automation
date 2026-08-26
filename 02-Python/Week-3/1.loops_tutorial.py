devices = ["Leafo1","Leaf02","Leaf03"]
for device in devices:
    print(device)

devices = ["Leaf01", "Leaf02", "Leaf03", "Spine01", "Spine02"]
print("=" * 50)
print("Network Devices")
print("=" * 50)
for device in devices:
    print(device)
print("=" * 50)
print()
for device in devices:
    print(f'Device  :  {device}')
print()
for device in devices:
    print(f"Current device   :  {device}")
    print(f"Length of device :  {len(device)}")
print("=" * 50)
count = 0
for device in devices:
    count+=1
    print(f"{count} . {device}")

###enumerate()
print()
for number,device in enumerate(devices):# starting number is 0
    print(f"{number} . {device}")
print()
for number,device in enumerate(devices,start=1):# starting number is 1
    print(f"{number} . {device}")

print()
print("=" * 50)
print("Network Device Inventory")
print()
for number,device in enumerate(devices,start=1):# starting number is 1
    print(f"{number:02} . {device}")
print()
print("=" * 50)
print(f"Total Devices :  {len(devices)}")
print()

print("=" * 50)
devices = ["Leaf01", "Leaf02", "Leaf03", "Spine01", "Spine02"]
print("Leaf Devices:")
print()
leaf_count =0
for device in devices:
    if device.startswith("Leaf"):
        print(device)
        leaf_count+=1
print(f"Total Leaf Devices : {leaf_count}")
print("=" * 50)
print()

##Nested Loops
inventory = {
    "Leaf01": {
        "ip": "10.10.10.11",
        "vendor": "Cisco",
        "platform": "Nexus9000",
        "version": "10.3(5)"
    },

    "Leaf02": {
        "ip": "10.10.10.12",
        "vendor": "Cisco",
        "platform": "Nexus9000",
        "version": "10.3(5)"
    },
    "Leaf03": {
            "ip": "10.10.10.13",
            "vendor": "Cisco",
            "platform": "Nexus9000",
            "version": "10.4(2)"
        },
    
        "Spine01": {
            "ip": "10.10.10.21",
            "vendor": "Cisco",
            "platform": "Nexus9500",
            "version": "10.4(2)"
        },
    
        "Spine02": {
            "ip": "10.10.10.22",
            "vendor": "Arista",
            "platform": "7280",
            "version": "4.30"
        }

}
for device,details in inventory.items():
    print(device)
print()
for device,details in inventory.items():
    print(device)
    for key,value in details.items():
        print( key, ":" ,value)
print()
print("=" * 50)
for device,details in inventory.items():
    print(device)
    for key,value in details.items():
     if key == "ip":
      print(f"IP : {value}")
print()
print("=" * 50)
print("Cisco Devices:")
for device,details in inventory.items():
    if details["vendor"] == "Cisco":
     print(device)
     for key,value in details.items():
          if key == "ip" or key == "platform":
           #print(f"IP : {value}")
            print(key.upper(), ":" ,value)
          
print()
for device,details in inventory.items():
    print(device,details)
    for key,value in details.items():
        print(key,value)

print()
for device, details in inventory.items():
    for key, value in details.items():
        if key == "vendor" and value == "Cisco":
            print(device)

