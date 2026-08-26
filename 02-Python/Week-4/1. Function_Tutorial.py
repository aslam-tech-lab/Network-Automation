#Basic function
def device_statu():
    print(f'switch status is up')
device_statu()
print()
##One parameter outside data → argument → parameter
hostname = "Leaf01"
def check_device(hostname):
    print(f"{hostname} : UP")
check_device(hostname)
print()
###Multiple parameters
hostname = "Leaf01"
vendor = "Cisco"
def check_device(hostname,vendor):
    print(f"{hostname} : {vendor} : UP")
check_device(hostname,vendor)
print()
##passing the whole dictionary
device = {
    "hostname": "Leaf01",
    "ip": "10.10.10.11",
    "vendor": "Cisco",
    "status": "UP"
}
def show_device(device):
    print(f'Hostname : {device["hostname"]}')
    print(f'IP       : {device["ip"]}')
    print(f'vendor   : {device["vendor"]}')
    print(f'status   : {device["status"]}')
show_device(device)
print()
##Same function, multiple devices
device1 = {
    "hostname": "Leaf01",
    "ip": "10.10.10.11",
    "vendor": "Cisco",
    "status": "UP"
}

device2 = {
    "hostname": "Leaf02",
    "ip": "10.10.10.12",
    "vendor": "Cisco",
    "status": "DOWN"
}

device3 = {
    "hostname": "Spine01",
    "ip": "10.10.10.21",
    "vendor": "Arista",
    "status": "UP"
}
def show_device(device):
    print(f'{device["hostname"]} : {device["vendor"]} : {device["status"]}')

show_device(device1)  
show_device(device2)
show_device(device3)
print()
##List + Function + Loop.
devices = [
    {"hostname": "Leaf01", "vendor": "Cisco", "status": "UP"},
    {"hostname": "Leaf02", "vendor": "Cisco", "status": "DOWN"},
    {"hostname": "Spine01", "vendor": "Arista", "status": "UP"}
]
def show_device(device):
    for dev in device:
        print(f'{dev["hostname"]} : {dev["vendor"]} : {dev["status"]}')

show_device(devices)
print()
##Logic challenge prints only Cisco devices that are UP
def show_device(device):
    for dev in device:
        if dev["vendor"]== "Cisco" and dev["status"]=="UP":
            print(f'{dev["hostname"]} : {dev["vendor"]} : {dev["status"]}')
show_device(devices)
print()
### return 
def get_status():
    return "UP"
result = get_status()
print(result)
print()
###
def check_status(status):
    if status == "UP":
        return "Device is reachable"
    else:
        return "Device is not reachable"
result = check_status("UP")
print(result)
print()
##Return a dictionary
def get_device():
    dev = {"hostname": "Leaf01", "vendor": "Cisco", "status": "UP"}
    return dev
result=get_device()
print(f'{result["hostname"]} : {result["status"]}')
print()
##Return based on a condition
device = {"hostname": "Leaf01","vendor": "Cisco","status": "UP"}
def check_device(device):
    if device["status"] =="UP":
        return f'{device["hostname"]} is reachable'
    return f'{device["hostname"]} is not reachable'
result =check_device(device)
print(result)
print()
###Return wiht multiple dictonary-advance concept
device = [{"hostname": "Leaf01","vendor": "Cisco","status": "UP"},{"hostname": "Leaf02","vendor": "Cisco","status": "UP"}]
def check_device(device):
    results = []
    for dev in device: 
     if dev["status"] =="UP":
        results.append(f'{dev["hostname"]} is reachable')
     else:
        results.append(f'{dev["hostname"]} is not reachable')
    return results
result =check_device(device)
for res in result: 
    print(res)
print()