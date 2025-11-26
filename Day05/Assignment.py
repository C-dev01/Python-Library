# 1. Create a dictionary storing meanings of 3 English words.
# 2. Create a set of numbers and show union and intersection with another set.
# 3. Try to add both integer 9 and float 9.0 to a set and observe what happens
# (Hint: You can convert one into a string to make both unique.)

## 1
wordMeaning = {
    "Perplex" : "To confuse deeply",
    "Profound" : "Deep or meaningful",
    "Ubiquitous" : "Present, appearing, or found everywhere",
} 
print(type(wordMeaning))
print(wordMeaning)

print("Qustion 1 completed!\n")

## 2

set1 = {2,4,6,8,10,11}
set2 = {1,3,5,7,9,11}

union = set1.union(set2)
print(union)

intersection = set1.intersection(set2)
print(intersection)

print("Question 2 completed!\n")


## 3

# set = {1,2,3,4,5}
# set.add(9)
# print(f"Set after adding 9 :",{set})
# print(type(set))

my_set = set()

# Adding the integer 9
my_set.add(9)
print(f"Set after adding 9: {my_set}")

# Adding the float 9.0
my_set.add(9.0)
print(f"Set after adding 9.0: {my_set}")

print(f"Final set contents: {my_set}")
print(f"Length of the set: {len(my_set)}")

print("Question 3 completed!")






