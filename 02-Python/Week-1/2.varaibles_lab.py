print('=' * 60)
print(' Variables Lab ')
print('=' * 60)

device_hostname = " Leaf1"
device_vendor = "Cisco"
device_platform = "Nexus 9000"
device_os_version = "NXOS-10.2"
device_management_ip = '192.168.1.2'
vlan_id = "200"
bgp_ASN_ID = "65535"

print("Hostname = ", device_hostname)
print("Vendor = ", device_vendor)
print("Platform = ", device_platform)
print("Version = ", device_os_version)
print("IP address = ", device_management_ip)
print("Vlan number = ", vlan_id)
print("ASN = ", bgp_ASN_ID)


interace_status = True
vlan_num = 300
print(id(bgp_ASN_ID))
print(id(vlan_id))
print(vlan_num)
print(type(vlan_num))
print(type(device_management_ip))
print(type(interace_status))
