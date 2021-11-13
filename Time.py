
# A Time class that will be utilized to create a schedule/calendar
# that includes assignments and class times
class Time():

    # Initializing a Time variable
    # inputs are initialized using setter functions
    # day -> int value from 1-31
    # month -> int value from 1 to 12
    # year -> int value like 2021
    # hour -> int value from 0 to 23
    # minutes -> int value from 0 - 59
    def __init__(self, day, month, year, hour, minutes):
        self.setTime(day, month, year, hour, minutes)
    
    # Second type of initializing a Time variable
    # Not using hour and minutes
    # day, month, year are all int values
    # set using the setter functions of the class
    def __init__(self, day, month, year):
        self.setTime(day, month, year)
        self.hour = -1
        self.minutes = -1

    # setter function that initializes/changes 
    # all variables and sets whether this year 
    # is a leap year
    def setTime(self, day, month, year, hour, minutes):
        self.isLeapYear = self.isLeapYear()
        self.setMonth(month)
        self.setDay(day, month)
        self.setMonth(month)
        self.setYear(year)
        self.setHour(hour)
        self.setMinutes(minutes)
    
    # Setter function for day, month, year 
    # to be modified in times where hours 
    # and minutes are not applicable
    # sets whether this year is a leap year
    def setTime(self, day, month, year):
        self.isLeapYear = self.isLeapYear()
        self.setMonth(month)
        self.setDay(day, month)
        self.setMonth(month)
        self.setYear(year)
        self.hour = -1
        self.minutes = -1

    # getter function returns the day
    def getDay(self):
        return self.day
    
    # getter function that returns the month
    def getMonth(self):
        return self.month
    
    # getter function that returns the year
    def getYear(self):
        return self.year

    # getter function that returns the hour
    def getHour(self):
        if self.hour != -1:
            return self.hour
        return None

    # getter function that returns the minutes
    def getMinutes(self):
        if self.minutes != -1:
            return self.minutes
        return None

    # setter function that sets the day
    def setDay(self, day, month):
        # isMonth_31: variable that checks
        # whether the month has 31 days
        isMonth_31 = (month < 8 and month % 2 == 1) or (month >= 8 and month % 2 == 0)

        # isMonth_30: variable that if month is not 31 days,
        # is set to True 
        isMonth_30 = not isMonth_31

        # if the month is february, check if it is a leap year.
        if (month == 2):
            if (self.isLeapYear and day > 0 and day <= 29):
                self.day = day
            elif (not self.isLeapYear and day > 0 and day <= 28):
                self.day = day

        elif (isMonth_31 and day > 0 and day <= 31):
            self.day = day
        elif (isMonth_30 and day > 0 and day <= 30):
            self.day = day

    # setter function that sets the month
    def setMonth(self, month):
        if (type(month) == int) and month <= 12 and month > 0:
            self.month = month
    
    # setter function that sets the year
    def setYear(self, year):
        if (year > 0):
            self.year = year

    # setter function that sets the hour
    def setHour(self, hour):
        if (hour <= 23 and hour >= 0):
            self.hour = hour
    
    # setter function that sets the minutes
    def setMinutes(self, minutes):
        if (minutes <= 59 and minutes >= 0):
            self.minutes = minutes

    # function that returns a bool value on whether year
    # is a leap year.
    def isLeapYear(self, year):
        if (year % 4 == 0 or (year % 100 == 0 and year % 400 == 0)):
            return True


    