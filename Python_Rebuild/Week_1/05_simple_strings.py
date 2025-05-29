# Ask the user for their full name (no controls). Then print only: the first name, the last surname, number of actual characters in the full name, and the uppercase version of the full name

username = input("Hello, user. Please tell me your name: ")

split_list = username.split()
first_name = split_list[0]
last_name = split_list[-1]

screamed_username = username.upper()

# Counting by hand...
local_counter = 0

for character in username:
    if character != " ":
        local_counter += 1

# Smarter counting

usercount = len(username.replace(" ", ""))
print(usercount)

print("Thank you, user.")
print(f"Or rather, thank you {first_name}. Or is {last_name} more polite?")
print(f"BYE BYE, {screamed_username}. Your full name has {local_counter} characters.")
