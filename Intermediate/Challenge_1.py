'''

Reddit Daily Programmer - /r/dailyprogrammer

[Intermediate] - Challenge #1

create a program that will allow you to enter events organizable by hour. There must be menu options of some form, and you must be able to easily edit, add, and delete events without directly changing the source code.
(note that by menu i dont necessarily mean gui. as long as you can easily access the different options and receive prompts and instructions telling you how to use the program, it will probably be fine)

'''

'''

Better explanation:

'
Sounds like you meant to say:
    1. Create a menu driven program
    2. Using the menu drive program allow a user to add/delete items
    3. The menu should be based on an events calender where users enter the events by hour
    4. No events should be hard-coded.
'

'''

import sys

event_list = []
 
def event_organiser():
   
    while True:
   
        option = input('-*-')

        if option == 'exit':
            break

        elif option == 'help':
            print(' If you enter the command \'start\' you can add an event to the organiser \n',
                  'This will allow you to add an event title, location, time, date and descrption. \n',
                  'If you enter the command \'delete\' you can delete an event from the organiser, a list of events will be printed first. \n',
                  'If you enter the command \'check\' you can print a list of your events. \n')

            event_organiser()

        elif option == 'add':
            title = input('Please add the event title: ')
            location = input('Please add the event location: ')
            time = input('Please add the event time: ')
            date = input('Please add the event date: ')
            description = input('Please add the event description: ')

            event = [title, location, time, date, description]

            event_list.append(event)

        elif option == 'delete':
            for i in event_list:
                print ('{0} : {1}'.format(event_list.index(i), i))

            event_to_delete = int(input('Please enter the number of the event you wish to delete: '))
            del event_list[event_to_delete]

        elif option == 'check':
            for i in event_list:
                print('Event: ' + str(event_list.index(i)))
                print('Title: {0} \n Location: {1} \n Time: {2} \n Date: {3} \n Description: {4}'.format(i[0], i[1], i[2], i[3], i[4]))
              
def organiser_wrapper():
   
    option = input('Please enter \'start\' or \'exit\': ')

    if option == 'start':
        event_organiser()
    elif option in ('add', 'help', 'delete'):
        event_organiser()
    elif option in ('quit', 'exit'): 
        sys.exit()

    organiser_wrapper()
 
organiser_wrapper()

