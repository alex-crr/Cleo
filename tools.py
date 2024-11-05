import main
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
  print("Query:", query)
  return "5"

def off():
  main.run = False
  print("Turning off the assistant")
  return "Goodbye!"

tools=[      
      {
        'type': 'function',
        'function': {
          'name': 'get_weather',
          'description': 'Get the current temperature in a city',
          'parameters': {
            'type': 'object',
            'properties': {
              'city_name': {
                'type': 'string',
                'description': 'The city in which to get the weather',
              },
            },
            'required': ['city_name'],
          },
        },
      },
      
      {
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
      },
    ]

print("Liste de tool" )
print(tools[0]['function']['name'])