def isLeap(year):
    if (year % 4 == 0):
        if (year % 100):
            if (year % 400):
                return True
        return True
    return False

year = input("Enter a year: ")

if isLeap(int(year)):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")