"""
    Brandon Herford
    Discussion Post 5: Lists
    Comment - 2
    5/6/2016

"""
# This code is taken from Luke Ang.
def highest_temperature(temp_list):
    """Determine and print the highest temperature in list temperatures."""
    highest = temp_list[0]
    for i in range(len(temp_list)):
        if temp_list[i] > highest:
            highest = temp_list[i]
    return highest

# I wrote this main() to call the highest_temperature function above.
def main():
    """Create a list of temperatures and call a function to find the highest."""

    # Initialize the temperature list.
    some_temps = ["", "", "", "", "", ""]

    # For each index in 'some_temps' get a temperature from the user.
    for i in range(len(some_temps)):
        some_temps[i] = float(input("Give me a random temperature from the last few weeks: "))

    # Set highest_temp equal to the returned value from
    # the highest_temperature function.
    highest_temp = highest_temperature(some_temps)

    # Print the highest temperature.
    print(highest_temp)

main()
