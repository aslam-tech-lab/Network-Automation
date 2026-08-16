device = (
    "Leaf01",
    "10.10.10.11",
    "Cisco",
    "Nexus9000",
    "10.3(5)"
 )
hostname,ip,vendor,platform,version = device

print("=" *50)
print("Network Device Information")
print("=" *50)
print()
print(f"Hostname       :  {device[0]}")
print(f"IP             :  {device[1]}")
print(f"Vendor         :  {device[2]}")
print(f"Platform       :  {device[3]}")
print(f"Version        :  {device[4]}")
print()
print(f"Total Information Fields :  {len(device)}")
print(f"Cisco Device             :  {"Cisco" in device}")
print("=" *50)