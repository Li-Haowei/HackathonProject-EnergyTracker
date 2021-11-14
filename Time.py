'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''

# A Time class that will be utilized to create a schedule/calendar
# that includes assignments and class times
class Time():

    __month_names_short = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", \
             "Aug", "Sep", "Oct", "Nov", "Dec"]

    __month_names = ["January", "February", "March", "April", "May", "June", \
            "July", "Aug", "September", "October", "November", "December"]
    # Initializing a Time variable
    # inputs are initialized using setter functions
    # date_unsplit: contains string dd/mm/yyyy
    # time_unsplit: contains hh:mm
    def __init__(self, date_unsplit, time_unsplit):
        date_split = date_unsplit.split("/")
        time_split = time_unsplit.split(":")
        self.setDate(date_split)
        
        if (time_unsplit == None):
            self.hour = -1
            self.minute = -1
        else:
            self.setTime(time_split)
    
    def __cmp__(self, otherTime):
        isLater = True
        isLaterYear = True
        isLaterMonth = True
        isLaterDay = True
        isLaterHour = True
        isLaterMin = True
        
        if (self.year < otherTime.year):
            isLaterYear = False
        elif (self.monthNum < otherTime.monthNum):
            isLaterMonth = False
        elif (self.day < otherTime.day):
            isLaterDay = False
        elif (self.hour < otherTime.hour):
            isLaterHour = False
        elif (self.minutes < otherTime.minutes):
            isLaterMin = False

        isLaterDate = isLaterYear and isLaterMonth and isLaterDay
        isLaterTime = isLaterHour and isLaterMin

        isLater = isLaterDate and isLaterTime
        return isLater
        


    # setter function that initializes/changes 
    # all variables and sets whether this year 
    # is a leap year
    # date input: list of three components,
    # day, month, year
    def setDate(self, date):
        year_success = self.setYear(int(date[2]))
        self.isLeapYear = self.isLeapYear(self.year)
        month_success = self.setMonth(date[1])
        day_success = self.setDay(int(date[0]), date[1])
        return year_success and month_success and day_success

    # setter function that sets up the time,
    # hours and minutes.
    # time input: list of two components, hrs and mins
    def setTime(self, time):
        hour_success = self.setHour(int(time[0]))
        minute_success = self.setMinutes(int(time[1]))
        return hour_success and minute_success

    # getter function returns the day
    def getDay(self):
        return self.day
    
    # getter function that returns the monthNum
    def getMonthNum(self):
        return self.monthNum
        
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
        if (len(month) > 3):
            month = Time.__month_names.index(month) + 1
        elif (len(month) == 3):
            month = Time.__month_names_short.index(month) + 1

        success = False
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
                success = True
            elif (not self.isLeapYear and day > 0 and day <= 28):
                self.day = day
                success = True

        elif (isMonth_31 and day > 0 and day <= 31):
            self.day = day
            success = True
        elif (isMonth_30 and day > 0 and day <= 30):
            self.day = day
            success = True
        return success

    # setter function that sets the month
    def setMonth(self, month):

        success = False
        if (len(month) == 2) and month <= 12 and month > 0:
            self.month = Time.__month_names[month-1]
            self.monthNum = month
            success = True
        elif(len(month )>= 3):
            if (month in Time.__month_names):
                    self.monthNum = Time.__month_names.index(month) +  1
                    self.month = month
                    success = True
            elif (month in Time.__month_names_short):
                self.monthNum = Time.__month_names_short.index(month) + 1
                self.month = Time.__month_names[self.monthNum]
                success = True

        return success
    
    # setter function that sets the year
    def setYear(self, year):
        success = False
        if (year > 0):
            self.year = year
            success = True
        return success

    # setter function that sets the hour
    def setHour(self, hour):
        success = False
        if (hour <= 23 and hour >= 0):
            self.hour = hour
            success = True
        return success
    
    # setter function that sets the minutes
    def setMinutes(self, minutes):
        success = False
        if (minutes <= 59 and minutes >= 0):
            self.minutes = minutes
            success = True
        return success

    # function that returns a bool value on whether year
    # is a leap year.
    def isLeapYear(self, year):
        if (year % 4 == 0 or (year % 100 == 0 and year % 400 == 0)):
            return True
    
    def isLater(self, otherTime):
        """Compares two Time objects and returns True
           If the self object is later compared to the otherTime
           Else, returns False
        """
        isLater = self.__cmp__(otherTime)
        return isLater

def isLaterString(timeA, timeB):
    """Take in two strings, timeA and timeB, comparing which one of them is later.
        If timeA is later, return True, else False. 
        For instance, isLater(10/Jan/2021,11/Jan/2021), return False"""
    dateA_split = timeA.split(" ")
    dateB_split = timeB.split(" ")
    timeA_instance = Time(dateA_split[0], dateA_split[1])
    timeB_instance = Time(dateB_split[0], dateB_split[1])
    return timeA_instance.isLater(timeB_instance)

