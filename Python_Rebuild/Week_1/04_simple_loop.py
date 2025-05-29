# Loop through the list and print "I use {tool}". Bonus points if 'Tech' instead returns " Tech. Yeah, right..."

my_work_list = ["Love", "Happiness", "Sensitivity", "Tech", "Patience"]

for item in my_work_list:
    if item == "Tech":
        print(f"I love {item}. Yeah, right...")
    else:
        print(f"I love {item}. And that's no joke!")
