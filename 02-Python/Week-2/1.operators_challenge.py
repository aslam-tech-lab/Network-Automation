total_ports = 48
used_ports= 20

available_ports= total_ports-used_ports
utilization_of_ports= used_ports / total_ports * 100

print(f"Total switch ports is  {total_ports}")
print(f"Total used ports is    {used_ports}")
print(f'Available switch ports is  {available_ports}')
print(f'Utilization of switch ports is {used_ports}%')

print("ports available is ", available_ports > 0)
print("High utilization is ", utilization_of_ports > 80)

print("-" * 50)

hostname = "Leaf01"
vendor = "Cisco"
cpu_usage = 85
memory_usage = 72
interface_up = True

cpu_high = cpu_usage > 80
memory_high = memory_usage > 80
cisco_device = vendor = "Cisco"

healthy_device = (
    cpu_usage <= 80 and memory_usage <= 80 and interface_up == True
)

print("==================================================")
print("Device Status")
print("==================================================")
print()
print(f"Hostname is       : {hostname}")
print(f"vendor is         : {vendor}")
print(f"CPU > 80 % is     : {cpu_high}")
print(f"Memory > 80%      : {memory_high}")
print(f"Interface up is   : {interface_up}")
print(f"cisco device is   : {cisco_device}")
print(f'Healthy device is : {healthy_device}')

print("==================================================")


output = " Interface ethernet1/1 is up"
print("Ethernet" in output)
print("ethernet" in output)
print("down" not in output)