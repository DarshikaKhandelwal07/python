# who will pay the bill tonight?
import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")paint_area_calculator.py
random_choice = random.randint(0,len(names)-1)
print(f"{names[random_choice]} is going to buy the meal today!")