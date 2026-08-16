
devices = ["Leaf01","Leaf02","Leaf03"]
devices.append("Spine01")
devices.append("Spine02")

total_devices = len(devices)

print("="  * 50)
print("Network Device Inventory")
print("="  * 50)
print()

print(f"Total Devices    :  {total_devices}")
#print(f"Devices : {device}")
print("Devices         : ")
for device in devices:
 print(f" {device}" )
print(f"First Device   :  {devices[0]}")
print(f"Last Device    :  {devices[-1]}")
print(f"Leaf02 Present :  {"Leaf02" in devices}") 