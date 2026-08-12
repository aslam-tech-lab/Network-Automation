#hostname = input("Enter the hostname   :  ")
#print(hostname)

#age = input("Enter the age  :  ")
#print(type(age))

#ports = input("Enter number of ports: ")
#print(ports + 10)

#ports = int(input("Enter number of ports: "))
#print(ports + 10)

#vlan = int(input("Enter the vlan id  "))
#print(vlan)
#print(type(vlan))

#thersold = float(input("Enter the utilization thersold  "))
#print(thersold)
#print(type(thersold))

cpu_usage = int(input("Enter the usage : "))
print(f"cpu usage is {cpu_usage} %")
print(f"cpu > 80 % is {cpu_usage > 80}")

vlan = 200
print("Vlan ID is : vlan " + str(vlan))

print(f"vlan {vlan}")

hostname = input("Enter the Hostname: ")
management_ip = input("Enter the management ip: ")
vendor = input("Enter the vendor: ")

print()
print("========================================")
print("Network Device")
print("========================================")
print()
print(f"Hostname is              :  {hostname}")
print(f"Management ip address is :  {management_ip}")
print(f"Vendor name is           :  {vendor}")
