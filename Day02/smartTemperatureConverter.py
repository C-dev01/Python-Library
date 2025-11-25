# Take input in Celsius and print its equivalent Fahrenheit and Kelvin
#(Use explicit type conversion and arithmetic operators)
# Formula:      * Fahrenheit  = (C * 9/5) + 32
#               * Kelvin = C + 273.15

celsius = int(input("Enter your temperature in Celsius : "))

tempInFahren = (celsius * 9/5) + 32
tempInKelvin = celsius + 273.15

print("Temperature in Celsius : ",tempInFahren)
print("Temperature in Kelvin : ",tempInKelvin)

