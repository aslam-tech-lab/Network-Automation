count =1
while count <=5:
    print(count)
    count+=1
print()
##while with a Network Device List
devices = ["Leaf01","Leaf02","Leaf03","Spine01","Spine02"]
index =0
while index < len(devices):
    print(devices[index])
    index+=1
print()
##while with a Condition
index =0
while index < len(devices) and devices[index]!= "Spine01":
    print(devices[index])
    index+=1
print("device found")
print()
## device attemts
attempt = 1
while attempt <=5:
    print(f"checking device ..... atempt {attempt}")
    attempt+=1
print()
###List-based while:
statuses = ["DOWN", "DOWN", "DOWN", "UP"]
index=0
while statuses[index]!="UP":
    print("Checking ....")
    index+=1
print("Device is UP")
##Counter/state-based while
status ="DOWN"
attempt = 1
while status =="DOWN" and attempt <=3:
    print(f"Checking device... attempt {attempt}")
    attempt+=1
print("Maximum attempts reached")
print()
##while with a Changing State
status ="DOWN"
attempt = 1
while status == "DOWN" and attempt <=3:
    print(f"Checking device... attempt {attempt}")
    if attempt == 3:
        status = "UP"
    attempt+=1
print("Device is UP")
print()
##########Mini Project — Device Reachability Retry##########
device ="Leaf1"
status = "DOWN"
attempt = 1
while status == "DOWN" and attempt <=5:
    print(f"Checking device... attempt {attempt}")
    if attempt == 4:
      status = "UP"
    attempt+=1
print(f"{device} is UP ..")
print()
########break with forloop
devices = ["Leaf01", "Leaf02", "Spine01", "Leaf03"]
for dev in devices:
    if dev == "Spine01":
        print("Device found :", dev)
        break
    print(dev)
print()
### break with for,if,else
for dev in devices:
    if dev == "Spine03":
        print("Device found :", dev)
        break
else:
 print(f"Spine03 is not found")
 print()
 ###continue
 for dev in devices:
     if dev.startswith("Spine"):
         continue
     print(f"checking {dev}")
print()
## pass  Do nothing. Just continue normally.
for dev in devices:
    if dev.startswith("Spine"):
        pass
    print(f"checking {dev}")
print()
### while else
#inventory = ["Leaf01", "Leaf02", "Spine01", "Leaf03"]
attempt=1
while attempt <= 3:
      print(f"Checking... {attempt}")
      attempt+=1
else:
    print("Maximum attempts completed")
print()
## above same with if 
attempt=1
while attempt <=3:
    print(f"Checking... {attempt}")
    if attempt == 3:
        print("This is the final attempt")
    attempt+=1
print()
###combine while + if + break + else ##
device = "Leaf01"
status = "DOWN"
attempt = 1
while attempt <=5:
    print(f"Checking {device}... attempt {attempt}")
    if attempt ==4:
        status = "UP"
        print(f"{device} is {status}")
        break
    attempt+=1
else:
    print(f"{device} did not respond")
print()
###Final Mini Project### Find the FIRST Cisco device that is UP
dev_details = [
    {"hostname": "Leaf01", "vendor": "Cisco", "status": "DOWN"},
    {"hostname": "Spine01", "vendor": "Cisco", "status": "DOWN"},
    {"hostname": "Leaf02", "vendor": "Arista", "status": "UP"},
    {"hostname": "Leaf03", "vendor": "Cisco", "status": "UP"},
]    
for dev in dev_details:
    if dev["vendor"].startswith("Arista") or dev["status"] != "UP":
        continue
    print(f'Found: {dev["hostname"]} : {dev['vendor']} : {dev["status"]}')
    break
else:
    print("NO cisco device is found")
print()
### one more mini project###find the FIRST Cisco device that is UP
devices = [
    {"hostname": "Leaf01", "vendor": "Cisco", "status": "DOWN"},
    {"hostname": "Leaf02", "vendor": "Cisco", "status": "DOWN"},
    {"hostname": "Spine01", "vendor": "Arista", "status": "UP"},
    {"hostname": "Spine02", "vendor": "Cisco", "status": "UP"},
    {"hostname": "Leaf03", "vendor": "Cisco", "status": "UP"},
]
for dev in devices:
    if dev["vendor"] == "Arista":
        continue
    if dev["vendor"] == "Cisco" and dev["status"]=="DOWN":
        pass
        print(f'Cisco device found but currently DOWN: {dev["hostname"]}')
        continue
    if dev["vendor"] == "Cisco" and dev["status"]=="UP": 
     print(f'Found : {dev["hostname"]} : {dev["vendor"]} : {dev["status"]}')
    break
else:
    print("No Cisco UP device found")

