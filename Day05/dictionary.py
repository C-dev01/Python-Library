# A dictionary is a built-in datatype which stores data in key-value pair
# Unordered, mutable and don't allow duplicate keys...keys are unique

student = {
    "name" : "Chanchal Sharma",
    "age" : 19,
    "city" : "Jaipur",
    "roll number" : 115059,
    #"name" : "Aarya Sharma"
}

print(type(student))
print(student["name"])

# concept of indexing is changed by keys
# if we make duplicate keys then last occurence will be considered

print(student)

# Adding/Updating values
student["city"] = "Norway"
print(student)

student["favFood"] = "Tender Coconut"
print(student)

# Removng Elements

student.pop("favFood")
print(student)

# Other Methods

print(student.keys())
print(student.values())
print(student.items()) # print all elements in form of tuple
print(student.get("name"))
print(student.update({"city" : "Jaipur"}))
print(student)

# Nested Dictionary