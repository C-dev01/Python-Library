#Take your favourite food as input and print:
# Middle 3 characters
# Last 2 characters

str = input("Enter your favourite food name : ")
mid = len(str)//2
print("Middle 3's are :",str[mid-1:mid+2])
print("Last 2's are :",str[-2:])

