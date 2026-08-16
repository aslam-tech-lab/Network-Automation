print("=" * 50)
cpu_usage = 85
if cpu_usage > 80:
    print("High cpu usage")

interface_status = "down"
if interface_status == "down":
    print("Interface requires attention")

cpu_usage = 65
if cpu_usage > 80:
    print("High cpu usage")
else:
  print("Cpu is normal")

interface_up = True
if interface_up:
    print("Interface is up")
else:
    print("Interface is down")

cpu_usage = 75
if cpu_usage > 90:
    print("critical")
elif cpu_usage > 80:
    print("High")
else:
    print("normal")

cpu_usage = 95
if cpu_usage > 80:
    print("High")
elif cpu_usage > 90:
    print("critical")

if cpu_usage > 90:
    print("Critical")
elif cpu_usage > 80:
    print(" High")
else:
    print("Normal")

cpu_usage = 75
memory_usage =70

if cpu_usage <=80 and memory_usage <=80:
    print("Device is healthy")
else:
    print("Please check the device health")

interface_status = "Down"
power_status = "failed"
if interface_status == "Down" or power_status == "failed":
    print("device reqquired attention")

interface_up = "False"
if not interface_up:
    print("device is down")
print("=" * 50)

hostname = "Leaf01"
cpu_usage = 75
memory_usage = 65
interface_up = True
if cpu_usage > 75:
    print(f"{hostname} cpu is high")
elif memory_usage > 75:
    print(f"{hostname} memory is high")
elif not interface_up:
    print(f"{hostname} interace was down")
else:
    print(f"{hostname} is healthy")


vendor = "Cisco"
interface_up = False
if vendor == "Cisco":
    if not interface_up:
        print("Ineteface was down")
