# function checks if a year is a leap year
# the function takes in a year as its parameter
def is_leap_year(year):
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 != 0):
                return False
            else:
                return True
        else:
            return True

# asks user for a year and checks if the year is a leap year
year = int(input("Enter a year: "))
if is_leap_year(year): # when the function returns True - the inputted year is a leap year
    print(f"{year} is a leap year.")
else: # when the function returns False - the inputted year is not a leap year
    print(f"{year} is not a leap year.")