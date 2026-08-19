
devices = {
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
#print(devices)
for device,details in devices.items():
    print(device)
    for key,value in details.items():
        if key == "ip":
            print(value)

for device,details in devices.items():  
    if details["vendor"] == "Cisco":
        print(device)
        print(f"IP      : {details["ip"]}")
        print(f"Version : {details["version"]}")
print()
for device in devices.keys():
    print(device)
for device in devices.values():
    if device["vendor"] == "Cisco":
     print(device["ip"], ":",  device["platform"])
for device,values in devices.items():
    if values["vendor"] == "Cisco":
        print(device, ":", values["ip"], ":", values["platform"])
        
