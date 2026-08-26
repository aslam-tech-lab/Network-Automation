##multiple parameters
def check_device(hostname,ip,status):
    print(f'{hostname} : {ip} : {status}')
check_device("Leaf02","10.10.10.12","DOWN")
print()
##multiple parameters with return
def check_device(hostname,ip,status):
     return f'{hostname} : {ip} : {status}'
result=check_device("Leaf02","10.10.10.12","DOWN")
print(result)
print()
###Positional Arguments  Python matches the arguments by position:
def check_device(hostname,ip,status):
    print(f'{hostname} : {ip} : {status}')
check_device("10.10.10.12","Leaf02","DOWN")
print()
  ## one more example
check_device("Spine01","10.10.10.21","UP")
print()
##Keyword Arguments
def check_device(hostname,ip,status):
    print(f'{hostname} : {ip} : {status}')
check_device(ip="10.10.10.21",hostname="Spine01",status="UP")
print()
###Mixing positional + keyword arguments
def check_device(hostname,ip,status,):
    print(f'{hostname} : {ip} : {status}')
check_device("Spine01",status="UP",ip="10.10.10.2")
print()
###default parameters.
def check_device(hostname,status,ip="10.10.20.10"):
    print(f'{hostname} : {ip} : {status}')
check_device("Spine01",status="UP")
print()
###*args  it doesn't mean "list".Collect any number of positional arguments into a tuple
## *args → tuple
def check_device(*devices):
    for dev in devices:
     print(f'checking {dev}')
check_device("Leaf01","Leaf02","Spine01")
print()
def add_values(*numbers):
    total =0
    for num in numbers:
        total+=num
    return total
result =add_values(10,20,30,40)
print(result)
print()
##
def check_devices(*devices):
    checked_devices=[]
    for dev in devices:
        checked_devices.append(dev)
    return checked_devices
result=check_devices("Leaf01","Leaf02","Spine01")
print(result)
print()
##**kwargs  This is the dictionary counterpart to *args.
## **kwargs → dictionary.
def check_device(**device):
    for key,val in device.items():
        print(f'{key}  : {val}')
check_device(hostname="Spine01",ip="10.10.10.21",vendor="Arista",status="UP")
print()
## few examples
def check_devices(*devices):
    for dev in devices:
        print(f'Checking ..  {dev}')
check_devices("Leaf01", "Leaf02", "Leaf03", "Spine01")
print()
 ###**kwargs
def device_checking(**devices):
    for key,val in devices.items():
        print(f'{key:<10}      :  {val}')
device_checking(hostname ="Border leaf",ip="192.168.1.1",vendor="Dell",status="UP")
print()
## both args and kwargs
def device_check(*device,**details):
    for dev in device:
        print(dev)
    for key,val in details.items():
        print(f'{key} : {val}')
device_check("Leaf01","leaf02","Leaf03",vendor="Cisco",status="UP")
print()
##*args vs **kwargs
def test(*devices, **details):
    print(devices)
    print(details)

test(
    "Leaf01",
    "Leaf02",
    vendor="Cisco",
    status="UP"
)
print()
##Multiple return values + tuple unpacking:
def device_info(hostname, vendor):
    return hostname,vendor
result = device_info("Leaf01", "Cisco")
print(result)  
hostname,vendor =result
print(hostname,vendor)
print()
##Parameters + Collections.
devices = [
    {"hostname": "Leaf01", "status": "UP"},
    {"hostname": "Leaf02", "status": "DOWN"},
    {"hostname": "Spine01", "status": "UP"}
]
def get_down_devices(devices):
    hostname=[]
    for dev in devices:
        if dev["status"]=="DOWN":
            hostname.append(dev["hostname"])
    return hostname
result=get_down_devices(devices)
print(result)
print()
###Final Practice:
devices = [
    {"hostname": "Leaf01", "vendor": "Cisco", "status": "UP"},
    {"hostname": "Leaf02", "vendor": "Cisco", "status": "DOWN"},
    {"hostname": "Leaf03", "vendor": "Arista", "status": "DOWN"},
    {"hostname": "Spine01", "vendor": "Arista", "status": "UP"}
]
def get_devices_by_vendor(devices,vendor):
    device_list=[]
    for dev in devices:
        if dev["vendor"]==vendor:
         device_list.append(dev["hostname"])
    return device_list
result=get_devices_by_vendor(devices,"Cisco")
print(result)
print()
##vendor + status together.
def get_up_devices_by_vendor(devices, vendor):
    device_list=[]
    for dev in devices:
        if dev["vendor"]==vendor and dev["status"]=="UP":
            device_list.append(dev["hostname"])
    return device_list
result=get_up_devices_by_vendor(devices, "Arista")
print(result)
print()
##Return device information
def get_device_info(devices, hostname):
    #device_list=[]
    for dev in devices:
        if dev["hostname"]==hostname:
            return dev["hostname"],dev["vendor"]
result=get_device_info(devices,"Leaf03")
print(result)



