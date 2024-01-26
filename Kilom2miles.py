# Taking kilometers input from the user
kilometers = float(input("Enter value in kilometers: "))

# conversion factor
conv_fac = 0.621371456921;# conversion factor

# calculate miles
miles = kilometers * CONV_FACT
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))
