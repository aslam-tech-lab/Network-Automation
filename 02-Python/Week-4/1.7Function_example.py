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
def get_validation_result(details):
    status=check_status(details)
    vendor=check_vendor(details)
    if status and vendor:
        overall="PASS"
    else:
        overall="FAIL"
    result={"status":status,"vendor":vendor,"overall":overall}
    return result
#result=get_validation_result(inventory["Leaf01"])
#print(result)   

def print_validation_report(results):
    for dev,devices in results.items():
        if devices["status"]:
            status_result="PASS"
        else:
            status_result="FAIL"
        if devices["vendor"]:
            vendor_result="PASS"
        else:
            vendor_result="FAIL"
        overall_restlt=devices["overall"]
        print(f'{dev} -> Status: {status_result} | Vendor: {vendor_result} | Overall:{overall_restlt}')

def get_validation_summary(results):
    pass_count=0
    fail_count=0
    for dev,details in results.items():
        if details["overall"]=="PASS":
            pass_count+=1
        else:
            fail_count+=1
    total_count =pass_count+fail_count
    print(f'Total Devices :{total_count}')
    print(f'Passed        :{pass_count}')
    print(f'Failed        :{fail_count}')
    
def validate_all_device(inventory):
    status={}
    for dev,details in inventory.items():
        status[dev]=get_validation_result(details)
    return status
results=validate_all_device(inventory)
#print(results)
print_validation_report(results)
get_validation_summary(results)


