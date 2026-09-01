devices = [
    {"hostname": "Leaf01", "status": "UP"},
    {"hostname": "Leaf02", "status": "DOWN"},
    {"hostname": "Leaf03", "status": "UP"},
    {"hostname": "Spine01", "status": "DOWN"}
]
def get_up_devices(devices):
    up_devices=[]
    for dev in devices:
        if dev["status"]=="UP":
            up_devices.append(dev["hostname"])
    return up_devices
result =get_up_devices(devices)
print(result)
print()
### creating mutliple function
device = {
    "hostname": "Leaf01",
    "vendor": "Cisco",
    "status": "UP"
}
def check_status(device):
    return device["status"]=="UP"

def check_vendor(device):
    return device["vendor"]=="Cisco"
def validate_device(device):
    status_ok=check_status(device)
    vendor_ok=check_vendor(device)
    return status_ok and vendor_ok

result=validate_device(device)
print(result)
print()
devices = [
    {"hostname": "Leaf01", "vendor": "Cisco", "status": "UP"},
    {"hostname": "Leaf02", "vendor": "Cisco", "status": "DOWN"},
    {"hostname": "Spine01", "vendor": "Arista", "status": "UP"}
]
def show_device(device):
    print(f'{device["hostname"]} : {device["vendor"]} : {device["status"]}')
for device in devices:
    show_device(device)
print()
##aovoid duplicate
inventory = [
    {"hostname": "Leaf01", "vendor": "Cisco", "status": "UP"},
    {"hostname": "Leaf02", "vendor": "Cisco", "status": "DOWN"},
    {"hostname": "Spine01", "vendor": "Arista", "status": "UP"}
]
def format_device(device):
    return f'{device["hostname"]} : {device["vendor"]} : {device["status"]}'
for device in inventory:
    result =format_device(device)
    print(result)
print()
####### function calling another function
device = {
    "hostname": "Leaf02",
    "vendor": "Cisco",
    "status": "DOWN"
}
def device_status(device):
    return device["status"]=="DOWN"
def device_vendor(device):
    return device["vendor"]=="Cisco"
def validate_device(device):
    status_ok=device_status(device)
    vendor_ok=device_vendor(device)
    return status_ok and vendor_ok
result=validate_device(device)
print(result)
print()
###building a small function pipeline with multiple devices,
inventory = [
    {"hostname": "Leaf01", "vendor": "Cisco", "status": "UP"},
    {"hostname": "Leaf02", "vendor": "Cisco", "status": "DOWN"},
    {"hostname": "Leaf03", "vendor": "Cisco", "status": "UP"},
    {"hostname": "Spine01", "vendor": "Arista", "status": "UP"},
    {"hostname": "Spine01", "vendor": "Arista", "status": "UP"}
]
def switch_status(inventory):
    return inventory["status"]=="UP"
def switch_vendor(inventory):
    return inventory["vendor"]=="Cisco"
def switch_validation(inventory):
    status=switch_status(inventory)
    vendor=switch_vendor(inventory)
    return status and vendor
for dev in inventory:
    result=switch_validation(dev)
    print(f'{dev["hostname"]} : {result}')
print()
##Designing Functions That Return Useful Data
def get_down_devices(inventory):
    down_devices=[]
    for dev in inventory:
        if dev["status"]=="DOWN":
            down_devices.append(dev)
    return down_devices
result=get_down_devices(inventory)
print(result)
print()
###one function's returned result becoming another function's input
def get_device():
    return {"hostname":"Leaf01","vendor":"Cisco","status":"UP"}
def check_device(device):
    return device["status"]=="UP"
device=get_device()
result=check_device(device)
print(result)
print()
  ##one more exampple
def get_devices():
    return [
        {"hostname": "Leaf01", "status": "UP"},
        {"hostname": "Leaf02", "status": "DOWN"},
        {"hostname": "Leaf03", "status": "UP"}
    ]
def check_devices(devices):
    down_devices=[]
    for dev in devices:
        if dev["status"]=="DOWN":
            down_devices.append(dev)
    return down_devices
devices=get_devices()
result=check_devices(devices)
print(result)
print()
### Example 
inventory_details = {
    "Leaf01": {
        "status": "UP",
        "vendor": "Cisco",
        "ip": "10.10.10.11"
    },
    "Leaf02": {
        "status": "DOWN",
        "vendor": "Cisco",
        "ip": "10.10.10.12"
    },
    "Leaf03": {
        "status": "UP",
        "vendor": "Cisco",
        "ip": "10.10.10.13"
    },
    "Spine01": {
        "status": "UP",
        "vendor": "Arista",
        "ip": "10.10.10.21"
    }
}
def device_status(details):
    if details["status"]=="UP":
        return True
    else:
        return False
def device_vendor(details):
    if details["vendor"]=="Cisco":
        return True
    else:
        return False
def validate_device(details):
    status=device_status(details)
    vendor=device_vendor(details)
    if status and vendor:
        return "PASS"
    else:
        return "FAIL"
def all_device_validation(inventory_details):
    result={}
    for dev,details in inventory_details.items():
        result[dev]=validate_device(details)
    return result
results=all_device_validation(inventory_details)
print(results)
print()
## practice
servers = {
    "Server01": {"status": "UP"},
    "Server02": {"status": "DOWN"},
    "Server03": {"status": "UP"}
}
def validation_server(details):
    if details["status"]=="UP":
        return True
    else:
        return False
    
result={}
for dev,details in servers.items():
    result[dev]=validation_server(details)
print(result)
print()
### practice
servers = {
    "Server01": {"status": "UP", "os": "Linux"},
    "Server02": {"status": "DOWN", "os": "Linux"},
    "Server03": {"status": "UP", "os": "Windows"}
}
def check_status(details):
    if details["status"]=="UP":
        return True
    else:
        return False
def check_os(details):
    if details["os"]=="Linux":
        return True
    else:
        return False
def validation_server(details):
    server_status=check_status(details)
    server_os=check_os(details)
    if server_status and server_os:
        return "PASS"
    else:
        return "FAIL"

result={}
for server,details in servers.items():
    result[server]=validation_server(details)
print(result)
print()
##Practice — Switch Validation
switches = {
    "Leaf01": {"status": "UP", "vendor": "Cisco"},
    "Leaf02": {"status": "DOWN", "vendor": "Cisco"},
    "Spine01": {"status": "UP", "vendor": "Arista"},
    "Leaf03": {"status": "UP", "vendor": "Cisco"}
}
def switch_status(details):
    if details["status"]=="UP":
        return True
    else:
        return False
def switch_vendor(details):
    if details["vendor"]=="Cisco":
        return True
    else:
        return False
def validation_switch(details):
    status=switch_status(details)
    vendor=switch_vendor(details)
    if status and vendor:
        return "PASS"
    else:
        return "FAIL"
switch_detail={}
for switch,details in switches.items():
    switch_detail[switch]=validation_switch(details)
    #print(switch, validation_switch(details))
print(switch_detail)
print()
###Passing a List to a Function
devices = ["Leaf01", "Leaf02", "Leaf03", "Spine01"]
def show_devices(device_list):
    count=0
    for device in device_list:
        print(device)
        count+=1
    print(count)
show_devices(devices)
print()
## return count
def show_count(device_list):
    count=0
    for dev in device_list:
        count+=1
    return count
total=show_count(devices)
print(f'Total count is {total}')

### pass the dict in function
inventory = {
    "Leaf01": {"vendor": "Cisco"},
    "Leaf02": {"vendor": "Arista"},
    "Leaf03": {"vendor": "Cisco"}
}
def device_checks(inventory):
    switch={}
    for dev,details in inventory.items():
        if details["vendor"]=="Cisco":
            switch[dev]=details
    return switch
result=device_checks(inventory)
print(result)
print()
### function retun a list
inventory = {
    "Leaf01": {"vendor": "Cisco", "status": "UP"},
    "Leaf02": {"vendor": "Arista", "status": "UP"},
    "Leaf03": {"vendor": "Cisco", "status": "DOWN"},
    "Spine01": {"vendor": "Cisco", "status": "UP"}
}
def get_cisco_device(inventory):
    dev_list=[]
    for dev,details in inventory.items():
        if details["vendor"]=="Cisco" and details["status"]=="UP":
            dev_list.append(dev)
    return dev_list
result=get_cisco_device(inventory)
print(result)
print()
## function return a dict
inventory = {
    "Leaf01": {
        "vendor": "Cisco",
        "status": "UP",
        "ip": "10.10.10.11"
    },
    "Leaf02": {
        "vendor": "Cisco",
        "status": "DOWN",
        "ip": "10.10.10.12"
    },
    "Leaf03": {
        "vendor": "Cisco",
        "status": "UP",
        "ip": "10.10.10.13"
    },
    "Spine01": {
        "vendor": "Arista",
        "status": "UP",
        "ip": "10.10.10.21"
    }
}
def get_up_cisco_devices(inventory):
    up_devices={}
    for dev,details in inventory.items():
        if details["vendor"]=="Cisco" and details["status"]=="UP":
            up_devices[dev]=details["ip"]
    return up_devices
result=get_up_cisco_devices(inventory)
print(result)
print()
##Function → Dictionary → Validation Results
def validate_device(details):
    if details["vendor"]=="Cisco" and details["status"]=="UP":
        return "PASS"
    else:
        return "FAIL"
def all_device_validation(inventory):
    results={}
    for dev,details in inventory.items():
        results[dev]=validate_device(details)
    return results
result=all_device_validation(inventory)
print(result)
    
