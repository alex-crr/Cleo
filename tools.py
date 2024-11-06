import main
import mysql.connector

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

def run_query(query):
  mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="Cleo",
  password="cleo"
)
  mycursor = mydb.cursor()
  mycursor.execute('USE ProjectManagement;')
  mycursor.execute(query)
  myresult = mycursor.fetchall()
  print("Query:", query)
  print("Result:", myresult)
  print(type(myresult))
  myresult_str = str(myresult)
  print("Result as string:", myresult_str)
  return myresult_str

bullshit_desc = {
        'type': 'function',
        'function': {
          'name': 'bullshit',
          'description': 'returns the bullshit sum of two numbers',
          'parameters': {
            'type': 'object',
            'properties': {
              'a': {
                'type': 'string',
                'description': 'first number to be added',
              },
              'b': {
                'type': 'string',
                'description': 'second number to be added',
              },
            },
            'required': ['a', 'b'],
          },
        },
      }

def bullshit(a, b):
  print("Bullshit:", a, b)
  return "69"


def off():
  main.run = False
  print("Turning off the assistant")
  return "Goodbye!"
