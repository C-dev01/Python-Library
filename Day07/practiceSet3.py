# Write a function show_age(name, age) that prints: "(your name) is (your age)
# years old."

def show_age(name, age):
    print(f"{name} is {age} years old.")

show_age("Chanchal Sharma", 19)

# Create a function add_numbers(a, b) that prints both the sum and
# difference.

def add_numbers(a, b):
    sum = a + b
    print("Sum is: ",sum)

    diff = a - b
    print("Difference is: ",diff)

add_numbers(10,5)    

# Write a function fav_food(food) that prints "Saumya loves <food>".

def fav_food(food):
    print(f"Chanchal loves {food}")

fav_food("Dal-Bati")