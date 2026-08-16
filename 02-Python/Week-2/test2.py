import pandas as pd
devices = pd.read_csv("list.csv")
print(devices)
for _, device in devices.iterrows():
    print(device["ip"])


word = "sumendusushisukarsms"
count = 0
for i in word:
    if i == "s":
        count = count + 1
print(count)