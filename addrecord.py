"Objectives"
"" '' # Import connect module
"" '' # Create a function to add record(s) to a table in a database
"" '' # Use try and except to handle error(s)
"" '' # Use the execute method from the cursor object to run sql statement


"" '' # Notes
"" '' # The SQL statement may be parametrized (i. e. placeholders instead of SQL literals). 
"" '' # A parameter specifies the value a particular field must contain when carrying out a query. 	

from connect import *

def insert_record():
    try:
       film_title = input("Enter film title: ")
      
       film_yearReleased = input("Enter film year release: ")
      
       film_rating = input("Enter film rating: ")   
      
       film_duration = input("Enter film duration: ")
      
       film_genre = input("Enter film genre: ")
       # Execute SQL insert statement
       db_cursor.execute("INSERT INTO tblFilms VALUES(NULL,?,?,?,?,?)",(film_title, film_yearReleased, film_rating, film_duration, film_genre))
       
       db_con.commit() #permanently inserting a film in the db in the films table
       print(f"{film_title} inserted into the film table")
    except sql.ProgrammingError as pe:
        print(f"Failed operation: {pe}")
    except sql.OperationalError as oe: # raise a sql error as 
        #handle the exception/error raised
        print(f"Connection failed because: {oe}")
    except sql.Error as e: # raise a sql error as 
        #handle the exception/error raised
        print(f"Error resulted in: {e}")
    finally:
        print("Operation completed")
if __name__ == "__main__":
    insert_record()
