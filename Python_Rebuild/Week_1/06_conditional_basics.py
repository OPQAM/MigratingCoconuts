'''Ask the user for the hour of the day (0–23) and greet them appropriately:

    "Good morning" if before 12

    "Good afternoon" if 12–18

    "Good evening" if after 18

    Bonus: Check if the input is a number at all'''
while True:
    try:
        hour_day = int(input("Hi, please input the hour of the day (0-23): "))
    except ValueError:    # we're in fact trying to catch value errors
        print(f"I'm sorry, but that isn't a valid integer. Try again")
        continue
    
    if hour_day > 23 or hour_day < 0:
        print(f"{hour_day}? Really... please follow the rules.")
    elif hour_day < 12:
        print("Good morning, user.")
    elif hour_day < 19:
        print("Good afternoon, user.")
    else:
        print("Good evening , user.")
    break
