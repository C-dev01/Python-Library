# Practice Questions
# 1. Write a Python program to print numbers from 1 to 10 using a while loop.
# 2. Write a program to print numbers from 10 down to 1 using a while loop.
#    (Hint: start from 10 and decrease the counter each time.)
#    Example Output: 10 9 8 ... 1
# 3. Write a program to print all even numbers between 1 and 50 using a while
#    loop.
#    (Hint: Use the modulus operator % to check for even numbers.)
#    Example Output: 2 4 6 8 ... 50
# 4. Write a program that prints the sum of first n natural numbers.
#    For example, if n = 5, then output should be 1 + 2 + 3 + 4 + 5 = 15.
#    (Hint: Keep a running total inside the loop.)
# 5. Write a program to print this pattern using a while loop:
#    *
#    * *
#    * * *
#    * * * *
#    * * * * *


## 1
num = 1
while num <= 10:
    print(num)
    num = num+1
print("Question 1 completed!")    

## 2
num = 10
while num >= 1:
    print(num)
    num = num-1
print("Question 2 completed!")

## 3
num = 1
while num <= 50:
    if num % 2 == 0:
        print(num)    
    num = num+1
print("Question 3 completed!")  

## 4
i = 0
total = 0

while i <= 5:
    total = total + i
    i = i+1
print("Sum of first ", i,"natural numbers:",total)        
print("Question 4 completed!")

## 5
rows = 5
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print("* ", end="")
        j = j+1 
    print(" ")
    i = i+1   
    
print("Question 4 completed!")
print("We have successfully done our practice sheet!")




