# Project 1: Birthday
# Chloe Zeller and Allie Economou

import math
# is_leap_year(year) takes a year integer and returns True if it is a leap year and False if it is not
def is_leap_year(year):
    if (year % 4) != 0:
        return False
    elif (year % 100) != 0:
        return True
    elif (year % 400) != 0:
        return False
    else:
        return True
# this function has been checked and has passed all test cases, and appears to have no issues

# is_gregorian_date(year, month, date) takes integer values for year, month and date and returns True of the date falls
# after the start of the Gregorian calendar on September 14, 1752 and False if else
def is_gregorian_date(year, month, date):
    if year < 1752:
        return False
    if year == 1752 and month == 9 and date >= 14:
        return True
    if year == 1752 and month > 9 and 1 <= date <= 31:
        return True
    if year > 1752 and 1 <= month <= 12 and 1 <= date <= 31:
        return True
    else:
        return False
# this function has been checked and has passed all test cases, and appears to have no issues

# is_valid_date(year, month, date) takes integer values for year, month and date and determines whether or not the date
# actually makes sense in terms of normal calendar rules. If it does, the function returns True, else False
def is_valid_date(year, month, date):
   valid = is_gregorian_date(year, month, date)
   if valid == False:
       return False
   if valid == True and month < 1:
        return False
   elif valid == True and month > 12:
       return False
   elif valid == True and 1 <= month <= 12:
        if month == 1 and 1 <= date <= 31:
            return True
        if month == 2 and is_leap_year(year) == True and 1 <= date <= 29:
            return True
        elif month == 2 and is_leap_year(year) == False and 1 <= date <= 28:
            return True
        elif month == 2 and is_leap_year(year) == False and date > 28:
            return False
        elif month == 2 and is_leap_year(year) == False and date < 1:
            return False
        if month == 3 and 1 <= date <= 31:
            return True
        if month == 4 and 1 <= date <= 30:
            return True
        if month == 5 and 1 <= date <= 31:
            return True
        if month == 6 and 1 <= date <= 30:
            return True
        if month == 7 and 1 <= date <= 31:
            return True
        if month == 8 and 1 <= date <= 31:
            return True
        if month == 9 and 1 <= date <= 30:
            return True
        if month == 10 and 1 <= date <= 31:
            return True
        if month == 11 and 1 <= date <= 30:
            return True
        if month == 12 and 1 <= date <= 31:
            return True
        else:
            return False
# this function has been checked, all test cases have passed and appears to be functioning well

def weekday_of(year, month, date):
    a = is_valid_date(year, month, date)
    if a == False:
        return False
    if a == True:
     if month == 1 or month == 2:
        month = month + 12
        year = year - 1
    year = str(year)
    century = year[0:2]
    century = int(century)
    year = year[2:4]
    year = int(year)
    day = int(((date + math.floor((13 * (month + 1)) / 5) + year + math.floor(year / 4) + math.floor(century / 4) + (5 * century)) % 7))
    return day
# this function has been checked, all test cases have passed and appears to be functioning well

# This function is supposed to take a
def weekday_name(a):
    if a == 0:
        return 'Saturday'
    if a == 1:
        return 'Sunday'
    if a == 2:
        return 'Monday'
    if a == 3:
        return 'Tuesday'
    if a == 4:
        return 'Wednesday'
    if a == 5:
        return 'Thursday'
    if a == 6:
        return 'Friday'
# This function has passed all test cases but I'm confused as to why you don't involve or how you use the weekday_of
# function when the input into the weekday_name function has to be a single integer

def main():
    n = str(input('Enter your birthday in YYYY-MM-DD format: '))
    year = n[0:4]
    year = int(year)
    month = n[5:7]
    month = int(month)
    date = n[8:10]
    date = int(date)
    valid = is_valid_date(year, month, date)
    if valid == False:
        return print('The date you entered is invalid.')
    if valid == True:
        day = weekday_of(year, month, date)
        output = weekday_name(day)
        return print('You were born on a', output + '!')
if __name__ == '__main__':
    main()


