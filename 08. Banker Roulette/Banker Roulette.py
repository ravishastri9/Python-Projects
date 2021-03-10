"It will choose a random person from a list of person to pay the bill."

import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

name_as_Csv = input("Give me all the name, separated by comma ")
names = name_as_Csv.split(", ")
num_items = len(names)
random_choice = random.randint(0, num_items - 1)
person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to pay for me")
