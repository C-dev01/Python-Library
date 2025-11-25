# Store multiple data in multiple datatypes
# But are immutable

tup = (34,56,78,89,90)
print(tup[0])

studentTuple = ("Chanchal", "Nisha", "Aarush")
# studentTuple[1] = "Kallo"  can't be changed IMMUTABLE

# Empty Tuples
emptyTuple = ()
singleTuple = (1,)      #without comma treat as int type
print(type(emptyTuple))
print(type(singleTuple))

# Methods
print(studentTuple.index("Nisha"))
print(studentTuple.count("Aarush"))
print(studentTuple.count("Ankit"))


