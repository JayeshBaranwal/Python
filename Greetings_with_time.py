import time
name = input("Enter the name: ")
current_time = time.strftime('%H: %M: %S')
print(current_time)

hour = int(time.strftime('%H'))
if hour >= 6 and hour < 12:
    print("Good Morning ", name)
elif hour >= 12 and hour < 16:
    print("Good Afternoon ", name)
elif hour >= 16 and hour < 20:
    print("Good Evening ", name)
else:
    print("Good Night ", name)
