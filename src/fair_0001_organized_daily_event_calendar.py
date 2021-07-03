'''
Ezra S. Brooker
2021

Source: reddit.com/r/DailyProgrammer 2012-02-10
https://www.reddit.com/r/dailyprogrammer/comments/pihtx/intermediate_challenge_1/


Create a program that will allow you to enter events organizable by hour.
There must be menu options of some form, and you must be able to easily edit, 
add, and delete events without directly changing the source code.

(note that by menu I don't necessarily mean GUI. As long as you can easily access
the different options and receive prompts and instructions telling you how to use
the program, it will probably be fine)

'''
import sys
if sys.version[0] != '3':
    raise Exception("Python 2 is no longer supported, please use Python 3")
from numpy import argsort as np_argsort
from datetime import date

class EventOrganizerConsole:


    def __init__(self, filename=None):
        
        if filename is None:
            self.event_names = []
            self.event_times = []
            self.event_nums  = 0
            self._sort_time  = []
        else:
            self.LoadEventsFromFile(filename)


    def Run(self):

        while True:
            self.PrintMenu()
            choice = int(input(" # Enter option number: "))

            if choice == 0:
                save = input("# Exiting Event Organizer, would you like to save your Calender? [y/N] ")
                if save.lower in ('y', 'yes'):
                    self.SaveCalendarToFile()
                sys.exit()

            elif choice == 1:
                self.AddEvent()
            elif choice == 2:
                self.EditEvent()
            elif choice == 3:
                self.DeleteEvent()
            elif choice == 4:
                self.ViewCalendar()
            elif choice == 5:
                self.LoadEventsFromFile()
            elif choice == 6:
                self.SaveCalendarToFile()
            else:
                print(f" # Did not recognize option {choice}, please choose a valid option.")


    def PrintMenu(self):

        print("")
        print(" #--- MENU ---#")
        print(" # 1. Add event")
        print(" # 2. Edit event")
        print(" # 3. Delete event")
        print(" # 4. View calendar")
        print(" # 5. Load events from file")
        print(" # 6. Save calendar to file")
        print(" # 0. Exit")


    def LoadEventsFromFile(self):
        pass


    def SaveCalendarToFile(self):
        pass


    def AddEvent(self):

        print("\nEnter CANCEL to stop adding a new event...")
        
        while True:            
            name = input("Enter event name: ")
            name = name.strip()
            if name.lower() == 'cancel': return
            
            time = input("Enter event time (HH:MM) military time: ")
            time = time.strip().replace(' ', '')
            if time.lower() == 'cancel': return

            self.event_names.append(name)
            self.event_times.append(time)
            self._sort_time.append(self._getTime(time.lower()))


    def EditEvent(self):
        print("\nEnter CANCEL to stop editing an event...")

        while True:
            eid  = input("Enter the ID number of the event you would like to edit: ")
            if len(eid) == 0: 
                print("You did not enter a valid ID number")
                return
            eid = int(eid)
            
            name = input("Enter event name or leave blank to skip: ")
            name = name.strip()
            if name.lower() == 'cancel': return
            
            time = input("Enter event time (HH:MM) military time or leave blank to skip: ")
            time = time.strip().replace(' ', '')
            if time.lower() == 'cancel': return

            if len(name) > 0: self.event_names[eid] = name
            if len(time) > 0: 
                self.event_times[eid] = time
                self._sort_time[eid]  = self._getTime(time.lower())


    def DeleteEvent(self):
        print("\nEnter CANCEL to stop editing an event...")

        while True:
            eid  = input("Enter the ID number of the event you would like to delete: ")
            if name.strip().lower() == 'cancel': return
            if len(eid) == 0: 
                print("You did not enter a valid ID number")
                return

            eid = int(eid)
            self.event_names.pop(eid)
            self.event_times.pop(eid)
            

    def ViewCalendar(self):

        idx = np_argsort(self._sort_time)
        print(" EVENT CALENDAR")
        print(20*"-")
        for i,k in enumerate(idx):
            nk = self.event_names[k]
            tk = str(self.event_times[k])
            tk = tk.replace('.',":")
            print(f"{i:3d} | {tk:5s} | {nk}")
        print(20*"-")


    def _getTime(self,tstr):
        t = tstr.replace(":",".")
        t = float(t)
        return t

if __name__ == '__main__':

    organizer = EventOrganizerConsole()
    organizer.Run()