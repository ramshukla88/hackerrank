# Date: 04-May-2024
# Author: Ram Shukla
# Location: Hyderabad, India

n = int(input().strip())
if n % 2 != 0:
    print("Weird")
else:
    if n in range(2, 6):
        print("Not Weird")
    elif n in range(6, 21):
        print("Weird")
    else:
        print("Not Weird")
