# Write a program that prints the multiplication table of any number entered
# the user using a for loop.

num = int(input("Enter a number: "))
print("Table of ",num,)
for i in range(1,11,):
    print(num,"X",i,"=",num*i)
    