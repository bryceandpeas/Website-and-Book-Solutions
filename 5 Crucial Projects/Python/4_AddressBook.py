'''
5 Crucial Projects for Beginners - https://www.daniweb.com/programming/software-development/threads/131973/5-crucial-projects-for-beginners

4 -  Address Book:

The user wants to create an address book and downloads your program.
How would you make it? Create a program that prompts the user for the
information in most address books and then stores it in a .txt file!

What you will be Using:

Input/Output, Print, Python File Commands, If/Elif/Else

My Thoughts on Project:

This is a great intermediate Python project once you are really going with Python.
This will teach you how to access files, edit them, save them, delete them, and more.
If you get stuck you can look at my source code but I strongly suggest that you use
Google and then try to apply what you find into your program.
'''

import os.path
import sys


def menu():
  print('\n -----------------------\n',
      '|       Menu          |\n',
      '-----------------------\n',
      '| 0 | Add Contact     |\n',
      '-----------------------\n',
      '| 1 | Delete Contact  |\n',
      '-----------------------\n',
      '| 2 | Change Contact  |\n',
      '-----------------------\n',
      '| 3 | List Contacts   |\n',
      '-----------------------\n',
      '| 4 | Search Contacts |\n',
      '-----------------------\n',
      '| 5 | Save            |\n',
      '-----------------------\n',
      '| 6 | Exit            |\n',
      '-----------------------\n')


def add_contact(contact_list, first_name, surname, address, email, number):
  if first_name in contact_list and contact_list[contact_list.index(first_name) + 1] == surname:
    print('\nA contact with that name already exists, please differentiate...\n')
    main(contact_list)

  else:
    contact_list.append([first_name, surname, address, email, number])
    print('\nAdded {0} to your address book.\n'.format(first_name))


def delete_contact(contact_list, contact_to_delete):
  count_check = 0
  for contact in contact_list:

    if contact_to_delete == contact[0]:
      count_check += 1

  if count_check > 1:

    print('\nThere is more than one contact with that name,'
        '\nplease enter the correct contact number to delete.\n')

    for contact in contact_list:
      if contact_to_delete in contact:

        print('Contact no: {0}, '
            'First name: {1}, '
            'Last name: {2}\n'.format(contact_list.index(contact),
                         contact[0],
                         contact[1]))

    try:
      new_selection = int(input('Please enter a contact number: '))

      for contact in contact_list:
        if new_selection == contact_list.index(contact):
          contact_list.remove(contact_list[contact_list.index(contact)])
          print('\nDeleted: {0} {1}'.format(contact[0], contact[1]))

    except:
      print('That is not a valid choice, please try again.')

  elif count_check == 1:
    for contact in contact_list:
      if contact_to_delete in contact:
        contact_list.remove(contact_list[contact_list.index(contact)])
        print('\nDeleted: {0} {1}'.format(contact[0], contact[1]))

  else:
    print('\nThat is not a valid choice, please try again.')


def change_contact(contact_list, contact_to_change):
  count_check = 0
  for contact in contact_list:

    if contact_to_change == contact[0]:
      count_check += 1

    original_contact = contact

  if count_check > 1:

    print('\nThere is more than one contact with that name,'
        '\nplease enter the correct contact number to change.\n')

    for contact in contact_list:
      if contact_to_change in contact:

        print('Contact no: {0}, '
            'First name: {1}, '
            'Last name: {2}\n'.format(contact_list.index(contact),
                         contact[0],
                         contact[1]))

    try:
      new_selection = int(input('Please enter a contact number: '))

      for contact in contact_list:
        if new_selection == contact_list.index(contact):

          contact[0] = input('\nPlease enter your contact\'s first name: ')
          contact[1] = input('Please enter your contact\'s surname: ')
          contact[2] = input('Please enter your contact\'s address: ')
          contact[3] = input('Please enter your contact\'s email: ')
          contact[4] = input('Please enter your contact\'s number: ')

          if original_contact[0] != contact[0]:
            print('\nChanged first name: {0} to {1}'.format(original_contact[0],
                               contact[0]))
          if original_contact[1] != contact[1]:
            print('\nChanged surname: {0} to {1}'.format(original_contact[1],
                               contact[1]))
          if original_contact[2] != contact[2]:
            print('\nChanged address: {0} to {1}'.format(original_contact[2],
                               contact[2]))
          if original_contact[3] != contact[3]:
            print('\nChanged email: {0} to {1}'.format(original_contact[3],
                               contact[3]))
          if original_contact[4] != contact[4]:
            print('\nChanged number: {0} to {1}'.format(original_contact[4],
                               contact[4]))

          print('\nFinished changes')

    except:
      print('\nThat is not a valid choice, please try again.')

  elif count_check == 1:
    for contact in contact_list:
      if contact_to_change in contact:
        original_contact = contact
        contact[0] = input('\nPlease enter your contact\'s first name: ')
        contact[1] = input('Please enter your contact\'s surname: ')
        contact[2] = input('Please enter your contact\'s address: ')
        contact[3] = input('Please enter your contact\'s email: ')
        contact[4] = input('Please enter your contact\'s number: ')

        if original_contact[0] != contact[0]:
          print('\nChanged first name: {0} to {1}'.format(original_contact[0],
                               contact[0]))
        if original_contact[1] != contact[1]:
          print('\nChanged surname: {0} to {1}'.format(original_contact[1],
                               contact[1]))
        if original_contact[2] != contact[2]:
          print('\nChanged address: {0} to {1}'.format(original_contact[2],
                               contact[2]))
        if original_contact[3] != contact[3]:
          print('\nChanged email: {0} to {1}'.format(original_contact[3],
                               contact[3]))
        if original_contact[4] != contact[4]:
          print('\nChanged number: {0} to {1}'.format(original_contact[4],
                               contact[4]))

        print('\nFinished changes')

  else:
    print('\nThat is not a valid choice, please try again.')


def list_contacts(contact_list):
  for contact in contact_list:
    print('\nContact {0}:\n'
        ' - First Name: {1}\n'
        ' - Surname: {2}\n'
        ' - Address: {3}\n'
        ' - Email: {4}\n'
        ' - Number: {5}\n'.format(contact_list.index(contact),
                   contact[0],
                   contact[1],
                   contact[2],
                   contact[3],
                   contact[4]))


def search_contacts(contact_list, contact_to_search):
  count_check = 0
  for contact in contact_list:

    if contact_to_search == contact[0]:
      count_check += 1

  if count_check > 1:

    print('\nThere is more than one contact with that name,'
        '\nhere are those contacts:\n')

    for contact in contact_list:
      if contact_to_search in contact:

        print('\nContact {0}:\n'
            ' - First Name: {1}\n'
            ' - Surname: {2}\n'
            ' - Address: {3}\n'
            ' - Email: {4}\n'
            ' - Number: {5}\n'.format(contact_list.index(contact),
                        contact[0],
                        contact[1],
                        contact[2],
                        contact[3],
                        contact[4]))

  elif count_check == 1:
    for contact in contact_list:
      if contact_to_search in contact:
        print('\nFound contact for {0}:'.format(contact_to_search))
        print('\nContact {0}:\n'
            ' - First Name: {1}\n'
            ' - Surname: {2}\n'
            ' - Address: {3}\n'
            ' - Email: {4}\n'
            ' - Number: {5}\n'.format(contact_list.index(contact),
                        contact[0],
                        contact[1],
                        contact[2],
                        contact[3],
                        contact[4]))

  else:
    print('\nNo contact found for: {0}'.format(contact_to_search))


def save_contacts(contact_list):
  with open('contacts.txt', 'w') as output_file:
    for contact in contact_list:
      output_file.write('{0}\n'.format(contact))

  print('\nDone saving.')


def load_contacts(contact_list):
  with open('contacts.txt', 'r') as input_file:
    for contact in input_file:
      contact_list.append(contact.strip().replace('[', '').replace(']', '').replace('\'', '').split(','))

  print('\nDone loading.')


def main(contact_list):

  menu()

  try:
    option_selection = int(input('Please select your option: '))

  except:
    print('\nYou must select your option via its assigned number\n',
        ' --> Restarting...')
    main(contact_list)

  if option_selection == 0:
    first_name = input('\nPlease enter your contact\'s first name: ')
    surname = input('Please enter your contact\'s surname: ')
    address = input('Please enter your contact\'s address: ')
    email = input('Please enter your contact\'s email: ')
    number = input('Please enter your contact\'s number: ')

    add_contact(contact_list, first_name, surname, address, email, number)
    main(contact_list)

  elif option_selection == 1:
    contact_to_delete = input('\nPlease enter the first name of the contact to delete: ')

    delete_contact(contact_list, contact_to_delete)
    main(contact_list)

  elif option_selection == 2:
    contact_to_change = input('\nPlease enter the first name of the contact to change: ')

    change_contact(contact_list, contact_to_change)
    main(contact_list)

  elif option_selection == 3:
    list_contacts(contact_list)
    main(contact_list)

  elif option_selection == 4:
    contact_to_search = input('\nPlease enter the first name of the contact to search: ')

    search_contacts(contact_list, contact_to_search)
    main(contact_list)

  elif option_selection == 5:

    save_contacts(contact_list)
    main(contact_list)

  elif option_selection == 6:

    sure_exit = input('\nAre you sure you wish to exit? (y/n): ')

    if sure_exit.lower() == 'y':
      should_save = input('\nDo you wish to save? (y/n): ')
      if should_save.lower() == 'y':
        save_contacts(contact_list)
        sys.exit()

      elif should_save.lower() == 'n':
        sys.exit()

    elif sure_exit.lower() == 'n':
      main(contact_list)


if __name__ == '__main__':
  contact_list = []

  if not os.path.isfile('contacts.txt'):
    contact_list = []
  else:
    load_contacts(contact_list)

  main(contact_list)
