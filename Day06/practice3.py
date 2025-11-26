# Write a program to print the multiplication table of any number using a while
# loop.
# (Hint: Start i = 1 and run the loop until i <= 10.)
# Example Output:
# Enter a number: 3
# 3 x1 = 3
# 3×2=6
# 3 × 10 = 30

num = int(input("Enter a number: "))
i  = 1
while(i<=10):
    print(num,"X",i,"=",num*i)
    i = i+1
print("Table of ",num,"is done.")    