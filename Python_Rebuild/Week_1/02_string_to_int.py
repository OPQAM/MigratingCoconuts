# declare a number as a string, then your age as an int, convert the string to int and then add them into a result. Take your fake age and convert it into a float through division.

some_number = "8"
my_age = 46
number_converted = int(some_number)
older_me = my_age + number_converted

older_me = older_me/2

print(f"My unreal age is {older_me}")
print(type(older_me))
