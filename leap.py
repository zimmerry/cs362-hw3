def isLeap(year):
    if (year % 4 == 0):
        if (year % 100):
            if (year % 400):
                return True
        return True
    return False

def getYear():
    year = input("Enter a year: ")
    if (not year.isdigit()):
        return getYear()
    return year

year = getYear()

if isLeap(int(year)):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")