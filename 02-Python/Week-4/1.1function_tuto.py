def show_device(hostname,ip):
    print(f"{hostname}  : {ip}")
show_device("Leaf01","10.10.10.11")
print()
##Keyword arguments
def show_device(hostname,ip):
    print(f"{hostname}  : {ip}")
show_device(ip="10.10.10.11",hostname="Leaf01")
print()
##Default Parameter
def check_device(hostname,status="UP"):
    print(f'{hostname} : {status}')
check_device("Leaf01")
check_device("Leaf02","DOwn")
print()
##Local Variable
def check_device():
    status="UP"
    print(status)
check_device()
print()
##    Global Variable
status="UP"
def check_device():
    print(status)
check_device()
print()
##Same variable name
status="UP"
def check_device():
    status = "DOWN"
    print(status)
check_device()
print(status)
print()
##global syntax
device_status = "DOWN"
def change_status():
    global device_status
    device_status = "UP"
change_status()
print(device_status)
print()
#example
status = "DOWN"
def check_device():
    global status
    print(status)
    status = "UP"
    print(status)
check_device()
print(status)
print()
