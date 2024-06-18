"Objectives"
"" '' # Import connect module
"" '' # Create a function to run sql statements to generate different type of reports


"" '' # Notes
"" '' # The SQL statement may be parametrized (i. e. placeholders instead of SQL literals). 
"" '' # A parameter specifies the value a particular field must contain when carrying out a query. 	
import logging
import logging.config
import time
from connect import *

logging.basicConfig(filename=r"Python project/tblFilms.log", format = '[%(filename)s:%(lineno)d in function %(funcName)s located at %(pathname)s]%(message)s', datefmt='%Y-%m-%d', level=logging.DEBUG)

def search_report():
     try:
       field = input("Would you like to search by: filmID, title, yearReleased, rating, duration or genre?: ")
       if field == "filmID":
          id_field = input("Enter the filmID: ")

          db_cursor.execute("SELECT * FROM tblFilms WHERE filmID = ?", {id_field,}) # select a signle record based on the filmID
          a_record = db_cursor.fetchone() #fetches a single record

          if a_record == None: # check if the record is in the table or not
             
             print(f"A record with filmID {id_field} doesn't exist in the films table! ")
             #use logging here
             logging.warning(f"On{time.asctime()} ")
          else:
          # for record in a_record
           print(a_record)
       elif field == "title" or field == "yearReleased" or field == "rating" or field == "genre":
         search_str = input(f"Enter the serach criteria for {field}: ")
         db_cursor.execute(f"SELECT * FROM tblFilms WHERE {field} LIKE '%{search_str}%' ")
         search_records = db_cursor.fetchall()

         if search_records == None:
            print(f"No record(s) with the {field} matched the '{search_str} in the table!")
         else: 
            for records in search_records:
              print(records)
       else:
          print(f"Invalid search performed {field}")
     except sql.ProgrammingError as pe: #use to handle invaled sql statement
        print(f"failed operation: {pe}") 
     finally:
        print("Operation completed")
if __name__=="__main__":

   search_report()                