# Create a program that asks the user for a distance in kilometers and converts it to miles.
#- 1 mile is approximately 1.60934 kilometers.

#Your program should:
#- Ask the user to input a distance in kilometers
#- Convert the input to a number
#- Calculate the equivalent distance in miles
#- Print the result in a user-friendly format (e.g., "X kilometers is Y miles.")
#- Include error handling for invalid input (e.g., if the user enters text instead of a number)

#This task will allow practice of:
#- input() for user data
#- print() for displaying information
#- Type conversion (e.g., float())
#- Basic arithmetic operations
#- try-except for error handling
#- Variable assignment

print("Welcome to the Distance Converter!")

input_km = input("Input distance in kilometers:")

km = float(input_km)

# Convert km to miles
miles = km / 1.60934

# Print the result


parsed_input_km = int(input_km)

miles =parsed_input_km* 0.60934



print(f"{km} km is {miles:.2f} miles")







