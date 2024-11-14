import tools
import ollama   
from typing import List, Dict, Any, Callable, Optional
import time
import os

class Assistant:
    def __init__(self, model: str, tool_list = None):
        self.model: str = model
        self.memory: List[Dict[str, Any]] = []
        self.active: bool = True
        self.creation_date: str = time.strftime("%Y-%m-%d %H-%M-%S")
        self.tool_list = [(self.save_memory_desc , self.save_memory), (self.off_desc, self.off)] + tool_list
        
    def prompt(self, text: str) -> str:
        self.memory.append({'role': 'user', 'content': text})
        response = ollama.chat( model=self.model, messages=self.memory, tools= [tool[0] for tool in self.tool_list])
        self.memory.append({'role': 'assistant', 'content': response['message']['content']})
        
        # Check if the model decided to use the provided function //debugging purposes
        if not response['message'].get('tool_calls'):
            #print("The model didn't use the function. Its response was:")
            return response['message']['content']
        
        # Process function calls made by the model
        if response['message'].get('tool_calls'):
            available_functions = {}
            for tool in self.tool_list:
                #print(f'functions accessible: {tool[0]['function']['name']}')
                available_functions.update({tool[0]['function']['name']: tool[1]})
                
            for tool in response['message']['tool_calls']:
                #print(available_functions[tool['function']['name']])
                function_to_call: Callable = available_functions[tool['function']['name']]
                #if function_to_call.__name__ == 'run_query': #find a way for this to not be ifs but rather modular statement
                '''function_response: str = function_to_call(tool['function']['arguments']['query'])'''
                function_args = tool['function']['arguments']
                function_response: str = function_to_call(**function_args)
                self.memory.append(
                    {
                    'role': 'tool',
                    'content': function_response,
                    }
                )
                    
        final_response: Dict[str, Any] = ollama.chat(model=self.model, messages=self.memory)
        self.memory.append({'role': 'assistant', 'content': final_response['message']['content']})
        return final_response['message']['content']
        
        
    save_memory_desc = {
            'type': 'function',
            'function': {
            'name': 'save_memory',
            'description': 'save the chat history',
            'parameters': {
                'type': 'object',
                'properties': {
                },
                'required': [],
            },
            },
        }
    def save_memory(self) -> str:
        log_filename = f"Logs/assistant_memory_{self.model}_{self.creation_date}.log"
        with open(log_filename, 'w') as log_file:
            for entry in self.memory:
                log_file.write(f"{entry['role']}: {entry['content']}\n")
        return f"Memory saved to {log_filename}"
    # Ensure the Logs directory exists
    if not os.path.exists('Logs'):
        os.makedirs('Logs')
    
    off_desc = {
        'type': 'function',
        'function': {
          'name': 'off',
          'description': 'Turn off the assistant upon being told to sleep or be turned off',
          'parameters': {
            'type': 'object',
            'properties': {
              'save': {
                'type': 'bool',
                'description': 'Wether ot not the chat history should be saved',
              },
            },
            'required': [],
          },
        },
      }
    
    def off(self, save: bool = True) -> str:
        self.active = False
        if save: self.save_memory()
        return "Assistant is now off"
    
