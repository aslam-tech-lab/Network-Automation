devices = {
    "Leaf01": {
        "IP": "10.10.10.11",
        "Vendor": "Cisco",
        "Platform": "Nexus9000",
        "Version": "10.3(5)"
    },
    "Leaf02": {
            "IP": "10.10.10.12",
            "Vendor": "Cisco",
            "Platform": "Nexus9000",
            "Version": "10.3(5)"
        },
    "Spine01": {
            "IP": "10.10.10.12",
            "Vendor": "Cisco",
            "Platform": "Nexus9000",
            "Version": "10.4(5)"
        }
     
}

print("=" * 50)
print("Network Device Inventory")
print("=" * 50)
print()
print(f"Device Count :   {len(devices)}")
print()
for device,values in devices.items():
    print(device)
    for key,value in values.items():
       print(f"{key:<10}  : {value}")
print()
print("=" * 50)