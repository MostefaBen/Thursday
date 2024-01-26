# Taking kilometers input from the user
kilometers = float(input("Enter value in kilometers: "))

# conversion factor
CONV_FACT = 0.6213711234567890

# calculate miles
miles = kilometers * CONV_FACT
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))
