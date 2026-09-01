inventory = {
    "Leaf01": {
        "vendor": "Cisco",
        "status": "UP",
    },
    "Leaf02": {
            "vendor": "Cisco",
            "status": "DOWN",
    },
    "Leaf03": {
            "vendor": "Arista",
            "status": "UP",
    },
    "Spine01": {
            "vendor": "Cisco",
            "status": "UP",
    }
}
def check_status(details):
    if details["status"]=="UP":
        return True
    else:
        return False
def check_vendor(details):
    if details["vendor"]=="Cisco":
        return True
    else:
        return False
def validate_device(details):
    status=check_status(details)
    vendor=check_vendor(details)
    if status and vendor:
        return "PASS"
    else:
        return "FAIL"
def validate_all_devices(inventory):
    device_list={}
    for dev,details in inventory.items():
        device_list[dev]=validate_device(details)
    return device_list
result=validate_all_devices(inventory)
print(result)
###
def get_cisco_device(inventory):
    up_device=[]
    for key,val in inventory.items():
        if val["vendor"]=="Cisco" and val["status"]=="UP":
            up_device.append(key)
    return up_device
result=get_cisco_device(inventory)
print(result)
print()
###Nested Dictionaries + Functions
inventory = {
    "Leaf01": {
        "management": {
            "ip": "10.10.10.11",
            "gateway": "10.10.10.1"
        },
        "status": "UP"
    },

    "Leaf02": {
        "management": {
            "ip": "10.10.10.12",
            "gateway": "10.10.10.1"
        },
        "status": "DOWN"
    },

    "Spine01": {
        "management": {
            "ip": "10.10.10.21",
            "gateway": "10.10.10.1"
        },
        "status": "UP"
    }
}
def get_management_ips(inventory):
  ip_list={}
  for dev,details in inventory.items():
    ip_list[dev]=details["management"]["ip"] 
  return ip_list
result=get_management_ips(inventory)
print(result)
print()
#### Combining Collections + Functions
dev_inventory = {
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
            "vendor": "Arista",
            "status": "UP",
            "ip": "10.10.10.13"
    },
    "Spine01": {
            "vendor": "Cisco",
            "status": "UP",
            "ip": "10.10.10.21"
    }
}
def get_up_device(dev_inventory):
    up_devices=[]
    for dev,details in dev_inventory.items():
        if details["status"]=="UP":
          up_devices.append(dev)
    return up_devices
result=get_up_device(dev_inventory)
print(result)
print()
def get_cisco_ip(dev_inventory):
    ip_list={}
    for dev,details in dev_inventory.items():
        if details["vendor"]=="Cisco":
            ip_list[dev]=details["ip"]
    return ip_list
result=get_cisco_ip(dev_inventory)
print(result)
print()
def validate_device(details):
    if details["vendor"]=="Cisco" and details["status"]=="UP":
       return "PASS"
    else:
        return "FAIL"
def validate_all_devices(dev_inventory):
    results={}
    for dev,details in dev_inventory.items():
        results[dev]=validate_device(details)
    return results
result=validate_all_devices(dev_inventory)
print(result)
