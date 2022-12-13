
from .month import Month

class Year:
    """Represents a year, with a list of months
    """
    def __init__(self, calendarYear):

        self.calendarYear = calendarYear
        self.months = []

        # define a dictionary of the months and their lengths to initialize the year
        MONTHSDICT = { 'January' : 31,
        'February' : 28,
        'March' : 31,
        'April' : 30,
        'May' : 31,
        'June' : 30,
        'July' : 31,
        'August' : 31,
        'September' : 30,
        'October' : 31,
        'November' : 30,
        'December' : 31 }


        # define Months
        counter = 1
        for name, numberOfDays in MONTHSDICT.items():
            self.months.append(Month(name, calendarYear, counter, numberOfDays))
            counter = counter + 1