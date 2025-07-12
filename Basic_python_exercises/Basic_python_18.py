#Exercise 18: Check if a given year is a leap year
def check_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return("True")
            else:
                return("False")
        else:
            return("True")
    else:
        return("False")
print(check_leap_year(2024))

