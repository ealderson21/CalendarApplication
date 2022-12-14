
import pickle

from Model.calendar import Calendar
from View.calendar_view import CalendarView


class MenuView:
    """Represents the UI view of the main menu
    """
    def __init__(self):
        pass

    @staticmethod
    def display():
        """ Displays the main menu UI
        """
        selectingOption = True
        while(selectingOption):

            print(f'Welcome to the calendar menu!')
            print(f'a) Create a Calendar')
            print(f'b) Load a Calendar')
            print(f'c) Exit Program.')
            
            option = input('Select an option (a, b, c): ')
        
            if option != 'a' and option != 'b' and option != 'c':
                print('Invalid option, select again.')

            else:
                selectingOption = False
            
        # create a calendar
        if option == 'a':
            
            # get name input and check validity
            gettingName = True
            while(gettingName):
                name = (input('Name your calendar to get started (only letters and _): '))
                
                ACCEPTABLECHARS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '_']

                badName = False
                for char in name:

                    if char.lower() not in ACCEPTABLECHARS:
                        print('Invalid calendar name, try again.')
                        badName = True
                
                if badName == False:
                    gettingName = False
            
            # get first year in the range
            first = int(input('Input the first year in your calendar: '))

            #  get the last year in the range
            gettingRangeSecond = True 
            while(gettingRangeSecond):

                last = int(input('Input the last year in your calendar: '))

                if last < first:
                    print('Second year cannot be less than first year, try again.')
                else:
                    gettingRangeSecond = False
                
            calendar = Calendar(name, first, last)
            calendarViewer = CalendarView(calendar)
            calendarViewer.handle_calendar_options()
        
        # load the calendar with the given name
        if option == 'b':
                
            gettingName = True
            while(gettingName):
                name = (input('Name the calendar you\' d like to load (only letters and _): '))
                
                ACCEPTABLECHARS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '_']

                badName = False
                for char in name:

                    if char.lower() not in ACCEPTABLECHARS:
                        print('Invalid calendar name, try again.')
                        badName = True
                
                if badName == False:
                    gettingName = False

            with open(name + '.txt', 'rb') as f:
                calendar = pickle.load(f)

            calendarViewer = CalendarView(calendar)
            calendarViewer.handle_calendar_options()

        if option == 'c':
            exit()

