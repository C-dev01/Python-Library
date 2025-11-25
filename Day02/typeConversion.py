# Implicit Conversion (Done automatically)
x = 5       #int
y = 4.5     #float
z = x + y   #Python itsself converted it into float
print(z)
print(type(z))

# Explicit Conversion (Done by developer)
x = "49"    #string
y = int(x)   #string -> float


# Take num as input 
# convert to float and print both values before conversion and converted value
#  with their datatypes

num = input("Enter a number : ")
convertedValue = float(num)

print("Original Value : ", num , "Datatype is :",type(num))
print("Converted Value : ",convertedValue, "Datatype is :",type(convertedValue))
