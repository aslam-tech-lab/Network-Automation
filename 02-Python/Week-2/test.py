
interface = ["et1/1 up up 1500"]
print(interface)
for i in interface:
    print(i)
    name,admin_status,link_status,mtu_size = i.split()
    print(name)
    print(admin_status)
    print(link_status)
    print(mtu_size)