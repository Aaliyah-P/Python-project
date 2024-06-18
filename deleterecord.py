"Objectives"
"" '' # Import connect module
"" '' # Create a function to delete record(s) in a table in a database
"" '' # Use try and except to handle error(s)
"" '' # Use the execute method from the cursor object to run sql statement

"" '' # Notes
"" '' # The SQL statement may be parametrized (i. e. placeholders instead of SQL literals). 
"" '' # A parameter specifies the value a particular field must contain when carrying out a query. 	

from connect import *

def delete_record():
      try:
         id_field = input("Enter the filmID you wish to delete: ")

         db_cursor.execute(f"SELECT * FROM tblFilms WHERE filmID = ? ", (id_field,))

         a_record = db_cursor.fetchone() 

         if a_record == None:
            print(f"The field with ID {id_field} does not exist!")


         else:
            db_cursor.execute(f"DELETE FROM tblFilms WHERE filmID = ? ", (id_field,))
            db_con.commit()
            print(f"Record {id_field} deleted from tblFilms table!")
      except sql.ProgrammingError as pe: # use to handle invalid sql statement
       print(f"Failed operation: {pe}")
      finally:
       print("Operation completed")
if"__name__==__main__":
 delete_record()