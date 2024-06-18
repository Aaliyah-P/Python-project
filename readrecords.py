"Objectives"
"" '' # Import connect module
"" '' # Create a function to read record(s) from a table in a database
"" '' # Use try and except to handle error(s)
"" '' # Use the execute method from the cursor object to run sql statement


"" '' # Notes
"" '' # The SQL statement may be parametrized (i. e. placeholders instead of SQL literals). 
"" '' # A parameter specifies the value a particular field must contain when carrying out a query. 	

from connect import *
def read_records():

    try: 
      # Select all records
      db_cursor.execute("SELECT * FROM tblFilms")

      # Fetchall() method to fetch/get the selected records from the table
      all_records = db_cursor.fetchall()

      #iterate and print all records
      if all_records:
       for aRecord in all_records:
         print(aRecord)
    except sql.ProgrammingError as pe: # use to handle invalid sql statement
      print(f"Failed operation: {pe}")
    finally:
      print("Displayed all records")
if"__name__==__main__":
   read_records()         