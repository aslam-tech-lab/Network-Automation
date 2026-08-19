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
print("=" * 50)
print("Network Device Inventory")
print("=" * 50)
print()
print(f"Total Devices    :  {len(devices)}")
print("Devices:")
for device,values in devices.items():
    print(device)
print("=" * 50)
print("Cisco Devices:")
for device,values in devices.items():
    if values["vendor"] == "Cisco":
     print(device)
print("=" * 50)
print("Cisco Devices:")
cisco_count = 0
for device,values in devices.items():
    if values["vendor"] == "Cisco":
       cisco_count += 1
       print(device)
print(f"Cisco Devices Count :   {cisco_count}")
print("=" * 50)
expected_version = "10.4(2)"
for device,values in devices.items():
   if values["version"] != expected_version:
      print(device)
print()
print("=" * 50)
print("Network Device Validation Report")
print("=" * 50)
print()
total_devices = len(devices)
count =0
expected_version = "10.4(2)"
print(f"Total Devices          :  {total_devices}")
for device,values in devices.items():
   if values["vendor"] == "Cisco":
      count +=1
print(f"Cisco Devices          :  {count}")
print(f"Expected Version       :  {expected_version}")
print()
print("Devices Requiring Check:")
for device,values in devices.items():
   if values["version"]!= expected_version:
      print(device)
      