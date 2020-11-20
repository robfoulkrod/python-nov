
import os

# results = os.system('ipconfig /all')
# print("Here are the results")
# print(results)

for line in os.popen("ipconfig /all"):
    if "IPv4 Address" in line:
        print(line)
