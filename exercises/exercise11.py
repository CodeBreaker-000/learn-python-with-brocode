# Countdown timer

import time

my_time = int(input("Enter the time in secods: "))

# for x in range(0, my_time):
#     print(x)
#     time.sleep(1)

# print("Time's UP")

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hour = int(x / 3600)
    print(f"{hour:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time's UP")















