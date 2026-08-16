hostname = "Leaf01"
vendor = "Cisco"
cpu_usage = 85
memory_usage = 72
interface_up = True

print("=" * 50)
print("Device Health Check")
print("=" * 50)

print()
print(f"Hostname            : {hostname}")
print(f"Vendor              : {vendor}")
print(f"CPU Usage           : {cpu_usage}")
print(f"Memory Usage        : {memory_usage}")
print(f"Interface UP        : {interface_up}")
print()
if cpu_usage > 70:
    cpu_status = "High"
else:
    cpu_status = "Normal"
if memory_usage < 80:
    memory_status = "Normal"
else:
    memory_status = "High"
if interface_up:
    interface_status = "UP"
else:
    interface_status = " Down"
if cpu_status == "High" or interface_status == " Down":
    overall_status = "Attention Required"
else:
    overall_status = "Healthy"
print(f"CPU Status          : {cpu_status}")
print(f"Memory Status       : {memory_status}")
print(f"Interface           : {interface_status}")
print()
print(f"Overall Status      : {overall_status}")
print("=" *50)
print()



hostname = input("Enter the hostname  :  ")
vendor = input("Enter the vendor name :  ")
version = input("Enter the version    :  ")
interface_up = input("Is interface is UP ? : ")

print("#" * 50)
print("Network Validation Decision")
print("#" * 50)
print()
print(f"Hostname :   {hostname}")
print(f"Vendor   :   {vendor}")
print(f"Version  :   {version}")

if vendor == "Cisco":
    vendor_validation = "Cisco"
else:
    vendor_validation = "Not a Cisco"
if interface_up == "Yes":
    Interface_Status = "UP"
else:
    Interface_Status = "DOWN"
if vendor_validation == "Cisco" and Interface_Status == "UP":
    overall_result = "PASS"
else:
    overall_result = "FAILED"
print(f"Vendor Validation :  {vendor_validation}")
print(f"Interface Status  :  {Interface_Status}")
print(f"Overall Result    :  {overall_result}")
print()
print("#" * 50)