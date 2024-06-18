"Objectives"
"" '' # Import connect module
"" '' # Create a function to update record(s) in a table in a database
"" '' # Use try and except to handle error(s)
"" '' # Use the execute method from the cursor object to run sql statement

from connect import *

def update_record():
    try:
    # filmID is used to update a record as it is a primary key (unique) field
     
      id_field = input("Enter the filmID that you would like to update: ")
      #db_cursor.execute(f"SELECT * FROM tblFilms WHERE SongID = {id_field}")
     
      db_cursor.execute(f"SELECT * FROM tblFilms WHERE filmID = ? ", (id_field,))
     
      a_record = db_cursor.fetchone() #fetchs a single record in the database

      if a_record == None:  # check if a record is in the table or not
         print(f"The field with ID {id_field} does not exist! ")
      else:
         field_name = input(f"Enter the field name of the record you wish to update ").title()  
        
         field_value = input(f"Enter the value for the field {field_name}: ")
        
         field_value = "'"+field_value+"'" # wrap in single quotes so that the value matches what ever is input in the field value
         db_cursor.execute(f"UPDATE tblFilms SET {field_name} = {field_value} WHERE filmID = {id_field} ")
         db_con.commit()
    except sql.ProgrammingError as pe: # use to handle invalid sql statement
      print(f"Failed operation: {pe}")
    finally:
      print("Operation completed")
if"__name__==__main__":
   update_record()  