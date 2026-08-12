
Hostname = "Leaf01"
Management_ip= "10.10.10.11"
Vendor = "Cisco"
Vlan_id = "100"
cpu_usage = 75
print("==================================================")
print("Network Device Input")
print("==================================================")
print()
print(f"Hostname      : {Hostname}")
print(f"Management IP : {Management_ip}")
print(f"Vendor        : {Vendor}")
print(f"VLAN ID       : {Vlan_id}")
print(f"CPU USAGE     : {cpu_usage} %")
print(f"CPU > 80%     : {cpu_usage > 80}")
print()
print("==================================================")


Hostname = input("Enter the hostname : ")
Management_IP = input("Enter the ip address : ")
Vendor = input("Enter the vendor name : ")
Platform = input("Enter the platform : ")
VLAN_ID = input("Enter the vlan id : ")
Interface_Count = int(input("Enter the interface count : "))
Available_Interfaces = 48-Interface_Count

print("==================================================")
print("Network Device Registration Tool")
print("==================================================")
print()
print(f"Available Interfaces : {Available_Interfaces} ")