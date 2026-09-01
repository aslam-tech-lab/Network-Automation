###Local variable
def device_check():
    hostname="leaf01"
    vendor = "Cisco"
    print(hostname)
    print(vendor)
device_check()
print()
### outside variable/gloabl
hostanme ="Spine01"
vendor ="Arista"
def check_device():
    print(hostanme)
    print(vendor)
check_device()
print()
##local and gloabl
status = "UP"
def change_status():
    status = "DOWN"
    print(status)
change_status()
print(status)
print()
### global command variable  it will moify the global variable
status = "UP"
def change_status():
    global status
    status = "DOWN"
change_status()
print(status)
print()
#### enclose from lebg rule first it will check inner function if not find then check the outer and print
vendor = "Cisco"
def outer():
    vendor = "Arista"
    def inner():
        print(vendor)
    inner()
outer()
print()
### nonlocal- similar to global but it wil be used in nested function
def outer():
    vendor = "Cisco"
    def inner():
        nonlocal vendor
        vendor = "Arista"
    inner()
    print(vendor)
outer()
print()
### example
def validate_devices():
    count =0
    def validate_device(status):
        nonlocal count
        if status =="DOWN":
            count+=1
    validate_device("DOWN")
    validate_device("DOWN")
    validate_device("DOWN")
    validate_device("UP")
    return count
result=validate_devices()
print(result)