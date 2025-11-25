# List is built-in datatype that can store multiple data in a variable
# List can store multiple datatype 
# Lists are mutable

food = ["Poha", "Upma","Pizza", "Idli", "Burger", 20]
print(len(food)) #length
print("First value of the list: ",food[0]) #indexing for access elements

# Modifying Elements

marks = [99, 100, 98, 95]
print(marks[1])

marks[2] = 90
print(marks) 

# Slicing

print(marks[1:])
print(marks[:3])
print(marks[1:3])
print(marks[-1:-3])

print(min(marks))
print(max(marks))

# Methods
marks.append(92)
print(marks)

marks.sort()
print(marks)

marks.pop(2)
print(marks)

marks.remove(90)
print(marks)

marks.insert(2,93)
print(marks)
