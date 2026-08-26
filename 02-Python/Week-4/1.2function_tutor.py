#return vs print
def check_device():
    print("UP")
result =check_device()
print(result)
print()
def check_device():
    return "UP"
result=check_device()
print(result)
print()
##return immediately ends the function
def check_device():
    print("Checking")
    return "UP"
    print("Device check")
result=check_device()
print(result)
print()
##example
def check_device():
    print("Checking ...")
    return "Device is UP"
    print("Finished")
result=check_device()
print(result)
print()
##return inside a loop
devices = ["Leaf01", "Leaf02", "Spine02"]
def fin_device(devices):
    for dev in devices:
        if dev == "Spine01":
            return "Spine01 is found"

    return "Spine01 is not found"
result =fin_device(devices)
print(result)
print()
###Return vs Break
devices = ["Leaf01", "Leaf02", "Spine01"]
def check_devices(devices):
    for dev in devices:
        print(f'Checking {dev}')
        if dev == "Leaf02":
            break
    print("Function continues")
check_devices(devices)
print()
def check_devices(devices):
    for dev in devices:
        print(f'Checking {dev}')
        if dev == "Leaf02":
            return
    print("Function continues")
check_devices(devices)
print()
### example
def check_device(devices):
    for dev in devices:
        print(f'Checking  {dev}')
        if dev == "Leaf02":
            return
    print("All devices checked")
check_device(devices)
print()
##return with a value inside a loop
devices = [
    {"hostname": "Leaf01", "status": "UP"},
    {"hostname": "Leaf02", "status": "DOWN"},
    {"hostname": "Leaf03", "status": "UP"}
]
def check_device(devices):
    for dev in devices:
        if dev["status"]=="DOWN":
            return dev["hostname"]
result=check_device(devices)
print(result)
print()
##What if nothing is found?
devices = [
    {"hostname": "Leaf01", "status": "UP"},
    {"hostname": "Leaf02", "status": "UP"},
    {"hostname": "Leaf03", "status": "UP"}
]
def check_device(devices):
    for dev in devices:
        if dev["status"]=="DOWN":
            return dev["hostname"]
    return "All devices are up"
result=check_device(devices)
print(result)
print()
##First match vs ALL matches
devices = [
    {"hostname": "Leaf01", "status": "UP"},
    {"hostname": "Leaf02", "status": "DOWN"},
    {"hostname": "Leaf03", "status": "DOWN"},
    {"hostname": "Spine01", "status": "UP"}
]

def check_device(devices):
    hostname=[]
    for dev in devices:
        if dev["status"]== "DOWN":
            hostname.append(dev["hostname"])
    return hostname
results=check_device(devices)
for result in results:
 print(result)
print()
##Multiple conditions + return
def check_device(devices):
    for dev in devices:
        if dev["status"]=="UP":
            return f'{dev["hostname"]} is reachable'
        
    return f'No device is not reachable'
result=check_device(devices)
print(result)
print()
##
device = {
    "hostname": "Leaf01",
    "status": "DOWN"
}
def device_check(device):
    if device["status"]== "UP":
        return f'{device["hostname"]} is reachable'
    else:
        return f'{device["hostname"]} is not reachable'
result=device_check(device)
print(result)
print()
## for else
devices = [
    {"hostname": "Leaf01", "status": "UP"},
    {"hostname": "Leaf02", "status": "DOWN"},
    {"hostname": "Leaf03", "status": "DOWN"},
    {"hostname": "Spine01", "status": "UP"}
]

def find_devices(devices):
    for dev in devices:
        if dev["hostname"]== "Spine02":
            return f'Spine02 is found'
    else:
        return f'Spine02 is not found'
result=find_devices(devices)
print(result)
print()
#### return with multiple conditions
device = {
    "hostname": "Leaf01",
    "status": "UP"
}
def check_device(device):
    if device["status"]=="UP":
        return f'{device["hostname"]} is reachable'
    elif device["status"]=="DOWN":
        return f'{device["hostname"]} is not reachable'
    else:
        return f'{device["hostname"]} is unknown status'
result=check_device(device)
print(result)
print()
##list of devices + loop
devices = [
    {"hostname": "Leaf01", "status": "UP"},
    {"hostname": "Leaf02", "status": "DOWN"},
    {"hostname": "Leaf03", "status": "UNKNOWN"},
    {"hostname": "Spine01", "status": "UP"}
]
def device_checks(devices):
    for dev in devices:
        if dev["status"]=="DOWN":
            return f'{dev["hostname"]} is not reachable'
    return f'ALL devices are up'
result=device_checks(devices)
print(result)
print()
##Returning a Dictionary
def get_device():
   device={"hostname":"Leaf01","vendor":"cisco","status":"up"}
   return device
result =get_device()
print(f'{result["hostname"]} : {result["vendor"]} : {result["status"]}')
print()
##Pass parameters → create dictionary inside
def get_device():
    device={"hostname":"Leaf02","vendor":"cisco","status":"up"}
    return device
result =get_device()
print(f'{result["hostname"]} : {result["vendor"]} : {result["status"]}')
print()
### above example with differnt way
def get_device(hostname,vendor,status):
    device={"hostname":hostname,"vendor":vendor,"status":status}
    return device
result =get_device("Spine01","Arista","UP")
print(f'{result["hostname"]} : {result["vendor"]} : {result["status"]}')
print()
##Return multiple values from a loop
devices = [
    {"hostname": "Leaf01", "vendor": "Cisco", "status": "UP"},
    {"hostname": "Leaf02", "vendor": "Cisco", "status": "DOWN"},
    {"hostname": "Spine01", "vendor": "Arista", "status": "UP"}
]
def check_device(devices):
    for dev in devices:
        if dev["status"]=="DOWN":
            return dev["hostname"],dev["vendor"]
hostname,vendor=check_device(devices)
print(hostname,vendor)
print()
##Nested loop + return
devices = [
    {
        "hostname": "Leaf01",
        "interfaces": [
            {"name": "Eth1/1", "status": "UP"},
            {"name": "Eth1/2", "status": "DOWN"}
        ]
    },
    {
        "hostname": "Leaf02",
        "interfaces": [
            {"name": "Eth1/1", "status": "UP"},
            {"name": "Eth1/2", "status": "UP"}
        ]
    }
]
def check_interfaces(devices):
    for dev in devices:
        for interface in dev["interfaces"]:
            if interface["status"]=="DOWN":
                return f'{dev["hostname"]} : {interface["name"]}'
result=check_interfaces(devices)
print(result)
print()
##List of dictionaries + conditions + return
devices = [
    {"hostname": "Leaf01", "vendor": "Cisco", "status": "UP"},
    {"hostname": "Leaf02", "vendor": "Cisco", "status": "DOWN"},
    {"hostname": "Leaf03", "vendor": "Arista", "status": "DOWN"},
    {"hostname": "Spine01", "vendor": "Arista", "status": "UP"}
]
def check_interfaces(devices):
    for dev in devices:
        if dev["vendor"]=="Arista" and dev["status"]=="DOWN":
            return f'{dev["hostname"]} : {dev["vendor"]} : {dev["status"]}'
result=check_interfaces(devices)
print(result)
print()
##Function returns a collected result.
devices = [
    {"hostname": "Leaf01", "vendor": "Cisco", "status": "UP"},
    {"hostname": "Leaf02", "vendor": "Cisco", "status": "DOWN"},
    {"hostname": "Leaf03", "vendor": "Arista", "status": "DOWN"},
    {"hostname": "Spine01", "vendor": "Arista", "status": "UP"}
]
def check_devices(devices):
    hostnames=[]
    for dev in devices:
        if dev["status"]=="DOWN":
            hostnames.append(dev["hostname"])
    return hostnames
result=check_devices(devices)
print(result)
print()
##return vs break vs flag Goal: Find Leaf02.
devices = [
    {"hostname": "Leaf01", "status": "UP"},
    {"hostname": "Leaf02", "status": "DOWN"},
    {"hostname": "Leaf03", "status": "UP"}
]
  ###Method 1 — return
def device_check(devices):
    for dev in devices:
        if dev["status"]=="DOWN":
            return f'{dev["hostname"]} is found'
result=device_check(devices)
print(result)
print()
   ###Method 2 — break
def device_check(devices):
    for dev in devices:
        if dev["status"]=="DOWN":   
            print(f'{dev["hostname"]} is found')
            break
    print("Checking completed")
device_check(devices)
print()
   ###Method 3 — Flag
def device_check(devices):
    device_found=False
    for dev in devices:
        if dev["hostname"]=="Leaf02":
            device_found=True
            break
    if device_found:
        print("Leaf02 is  found")
    else:
        print("Leaf02 is not found")
device_check(devices)
print()
  ####Method 3 — Flag without break
def device_check(devices):
    device_found=False
    for dev in devices:
        if dev["hostname"]=="Leaf03":
            device_found=True
    if device_found:
        return "Leaf03 is found"
    
    return "Leaf03 is not found"
result=device_check(devices)
print(result)
print()
##########Network-Automation Example#############
device_inventory = [
    {"hostname": "Leaf01", "vendor": "Cisco", "status": "UP"},
    {"hostname": "Leaf02", "vendor": "Cisco", "status": "DOWN"},
    {"hostname": "Leaf03", "vendor": "Arista", "status": "DOWN"},
    {"hostname": "Spine01", "vendor": "Arista", "status": "UP"}
]
def get_down_devices(device_inventory):
    down_list=[]
    for dev in device_inventory:
        if dev["status"]=="DOWN":
            down_list.append((dev["hostname"],dev["vendor"]))
    return down_list
result=get_down_devices(device_inventory)
print(result) ## result is tuple inside the list
for hostname,vendor in result:  ### looping the result to split
    print(f'{hostname} : {vendor}')