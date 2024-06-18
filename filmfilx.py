# You have now been tasked with developing a python application to manipulate the FilmFlix database.
# Perform CRUD operation on the database from the python command line
# Print all records in  tblfilms in database filmflix.db
# Allows users to add, update or delete records in the filmflix.db database (CRUD)
# Print a selection of reports, these functions demonstrate different techniques of writing sql commands and printing reports
# For example
# Hint: for FilmFlix CRUD: create Options menu to include 
# Options menu
# 1. Add a record
# 2. Delete a record
# 3. Amend a record
# 4. Print all records
# 5. Exit
# Hint: for FilmFlix report create Options menu to include 
# 1. Print details of all films
# 2. Print all films of a particular genre
# 3. Print all films of a particular year
# 4. Print all films of a particular rating
# 5. Exit

# SELECT * FROM tblfilms WHERE yearReleased = 2001
# SELECT * FROM tblfilms WHERE rating = ‘PG’
# SELECT * FROM tblfilms WHERE genre= 'Action’


 # Allows users to add, update or delete records in the filmflix.db database (CRUD)
# import all modules 
import readrecords, addrecord, updaterecord, deleterecord, report

# create a function to read content from the dbMenu.txt file
def read_file():
  try:
    with open('Python project/dbMenu.txt') as file_read:
      fr = file_read.read()
      return fr
  except FileNotFoundError as fnf:
    print(f"Error handling file beause: {fnf}")


def tblFilms_menu():
   option = 0  # declare option variable and intialise it with an integer data type
    # declared option_list variable and initialise with a list data structure with string items
   options_list = ["1", "2", "3", "4", "5", "6"] 

    # declared the menu_choices variable and initalise with the read_file() function
   menu_choices = read_file()
   
   #  create a while loop to repeat the code within the body of the while conditon
   while option not in options_list:
      # repeatedly call/invoke the read_file() function which is initialised with the menu_choices variable 
      print(menu_choices)


     # re-assign the option variable with a new value 
      option = input("Enter an option from the menu choices above")
      if option not in options_list:
        print(f"{option} is not a valid choice! ") 
        return option


main_program = True # declare main_program and initialised with a boolean data type with a value of True

while main_program: # same as while True
    # declare main_menu variable and intialise with the songs_menu() function
   main_menu = tblFilms_menu()
  
   match main_menu:
    # if case value = ( option = input ("Enter an ooption from the menu choices above")) e.g. the value 1
    case "1":
       readrecords.read_records()
    case "2":
           addrecord.insert_record()
    case "3":
           updaterecord.update_record()
    case "4":
           deleterecord.delete_record()
    case "5":
           report.search_report()
    case _:
      # re-assign the main_program variable with a boolean False value     
           main_program = False
input("Press 'Enter' to exit the Menu/App")           