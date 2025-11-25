# Set is a collection of unordered and unique items.
# Set automatically removes duplicate items.
# Written using curly braces.

# Unordered (no indexing)
# Unique
# Mutable
# Can't contain mutable elemnts like lists and dictinaries

food = {"Roti", "Dal", "Rice", "Paneer", "Roti"}
print(type(food))
print(food)

# Empty set
emptySet = set()
nums = {1,2,3,4}
print(emptySet)
print(nums)

# Add/Remove
food.add("Kunafa")
print(food)
food.remove("Roti")

# Methods

