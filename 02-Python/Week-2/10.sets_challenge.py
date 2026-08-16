site_a = {
    "Leaf01",
    "Leaf02",
    "Leaf03",
    "Spine01"
}

site_b = {
    "Leaf02",
    "Leaf03",
    "Spine01",
    "Spine02"
}
print("=" * 50)
print("Network Inventory Comparison")
print("=" * 50)
print()
print(f"Site A Devices :    {len(site_a)}")
print(f"Site B Devices :    {len(site_b)}")
print()
print(f"Common devices :")
common= site_a & site_b
for com in common:
 print(com)
print(f"Only Site A:")
only_siteA = site_a - site_b
for only in only_siteA:
 print(only)
print(f"Only Site B:")
only_siteB = site_b - site_a
for only in only_siteB:
 print(only)
print(f"All Unique Devices:")
unique_devices = site_a | site_b
for uniq in unique_devices:
 print(uniq)
print()
print("=" * 50)