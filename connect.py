"Objectives"
"" '' # Import sqlite module
"" '' # Understand what is sqlite
"" '' # Create and use a function to create a database file
"" '' # Use try and except to handle error(s)
"" '' # Use the connect function from the sqlite module to create a database file
"" '' # Create a cursor variable from the connect function  

"" '' # Notes:
"" '' #  What is Sqlite
"" '' #  SQLite is a lightweight disk-based database that does not require a separate server process making it easy to integrate into applications
"" '' #  and it uses a variant of the SQL language for database queries to access database. This combination of features makes SQLite a popular 
"" '' #  choice for applications that need a simple and self-contained database solution

import sqlite3 as sql # import the sqlite3 module and alised it as 'sql'


try:
 # to use the sqlite3 module we start by creating a database connection object (variable to hold the folder path with the filename)
  with sql.connect('Python project/filmflix.db')  as db_con:
    # once the db file is created 'python1.db' we create a cursor object (a variable) amd nind it the cursor() method from the sqlite module
    db_cursor = db_con.cursor()  #use execute sql statements 
except sql.OperationalError as oe:  # rasise a sql error as 
  # handle the exception/error raised
    print(f"Connection failed because: {oe}")       

