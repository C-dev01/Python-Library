print("\U0001F603") # Prints 😃
print("\U0001F60A") # Prints 😊
print("\U0001F609") # Prints 😉
print('\u2639') #
print("☹️")

msg = input("Enter your message: ")
msg = msg.replace(":)","\U0001F60A")
msg = msg.replace(":(","\u2639")
msg = msg.replace(":D","\U0001F603")
msg = msg.replace(";)","\U0001F609")
print(msg)





