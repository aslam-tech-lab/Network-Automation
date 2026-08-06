print("=" * 50)
hostname = "Leaf01"
print(hostname[0])
print(hostname[3])
print(hostname[-1])
print(hostname[-3])
print("=" * 50)
print(hostname[0:3])
print(hostname[2:5])
print(hostname[:5])
print(hostname[2:])
print(hostname[::-1])
print("=" * 50)

vendor = "Cisco"
platform = "Nexus9000"
version = "10.3(5)"
ip = "10.10.10.11"
print("=" * 50)
print('Network Automation Inventory')
print("=" * 50)

print("Hostname  :", hostname)
print("Vendor    :", vendor)
print("Platform  :", platform)
print("Version   :", version)
print("IP        :", ip)

print("Hostname Length  :", len(hostname))
print("Vendor Length    :", len(vendor))
print("First Character  :", hostname[0])
print("Last Character   :", hostname[5])
print("Reverse Hostname :", hostname[::-1])
print("=" * 50)

print("=" * 50)
print('Network Device Summary')
print("=" * 50)
hostname = "Spine01"
ip = "192.168.100.10"
vendor = "Cisco"
platform = "Nexus9504"
Software = "10.4(2)"
print("Hostname             :", hostname)
print("Management IP        :", ip)
print("Vendor               :", vendor)
print("Platform             :", platform)
print("Software              :", Software)


print("Hostname Length      :", len(hostname))
print("Software Length      :", len(Software))

print("First Letter         :", hostname[0])
print("Last Letter          :", hostname[6])

print("Platform First 5 Characters :", platform[0:5])
print("Platform Last 4 Characters  :", platform[5:])

print("Reverse Vendor     :", vendor[::-1])
print("=" * 50)