def is_leap_year(year):
    # Write your code here. 
    # Don't change the function name.
    if(year % 4 == 0):
        if(year % 400 == 0):
            return True
    return False
is_leap_year(2024)
