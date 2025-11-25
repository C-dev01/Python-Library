# You are given a list of programming languages:
# ["Python"
# "Java"
# "C++"
# "Python"
# "Java"
# "C"1
# Convert it into a set and print how many unique languages Divya knows.

programList = ["Python", "Java", "C++", "Python","Java","C"]
print(programList)
print(type(programList))
convertedSet = set(programList)
print("Converted to set :",convertedSet)
print(type(convertedSet))

print("Unique languages Divya knows : ",convertedSet)