import main
import mysql.connector

from mysql.connector import Error

run_query_desc = {
        'type': 'function',
        'function': {
          'name': 'run_query',
          'description': 'Run a given sql query',
          'parameters': {
            'type': 'object',
            'properties': {
              'query': {
                'type': 'string',
                'description': 'Query to be executed',
              },
            },
            'required': ['query'],
          },
        },
      }

'''def run_query(query):
  mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="Cleo",
  password="cleo"
)
  mycursor = mydb.cursor()
  mycursor.execute('USE Cleo_brain;')
  mycursor.execute(query)
  myresult = mycursor.fetchall()
  print("Query:", query)
  print("Result:", myresult)
  print(type(myresult))
  myresult_str = str(myresult)
  print("Result as string:", myresult_str)
  return myresult_str'''

def run_query(query):
    try:
        # Connect to the database
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="Cleo",
            password="cleo"
        )
        mycursor = mydb.cursor()
        
        # Select the database
        mycursor.execute('USE Cleo_brain;')
        
        # Execute the query
        mycursor.execute(query)
        myresult = mycursor.fetchall()

        # Print the query and result
        print("Query:", query)
        print("Result:", myresult)
        print("Result as string:", str(myresult))

        # Commit changes if the query modifies the database
        if query.strip().upper().startswith(('INSERT', 'UPDATE', 'DELETE')):
            mydb.commit()
            print("Changes committed to the database.")

        return str(myresult)

    except Error as e:
        print("Error while executing the query:", e)
        return None

    finally:
        # Close the connection
        if mydb.is_connected():
            mycursor.close()
            mydb.close()
            print("Database connection closed.")


#run_query("SELECT     TABLE_NAME AS 'Table',    COLUMN_NAME AS 'Column',    DATA_TYPE AS 'Data Type',    IS_NULLABLE AS 'Nullable',    COLUMN_DEFAULT AS 'Default',    COLUMN_KEY AS 'Key',    EXTRA AS 'Extra' FROM     INFORMATION_SCHEMA.COLUMNS WHERE    TABLE_SCHEMA = 'projectmanagement'ORDER BY     TABLE_NAME, ORDINAL_POSITION;")