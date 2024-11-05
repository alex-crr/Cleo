import tools
import ollama   
import main
from typing import List, Dict, Any, Callable, Optional
import time

class Assistant:
    def __init__(self, model: str, tool_list = None):
        self.model: str = model
        self.memory: List[Dict[str, Any]] = []
        self.active: bool = True
        self.creation_date: str = time.strftime("%Y-%m-%d %H-%M-%S")
        self.tool_list = tool_list
        
    def prompt(self, text: str) -> str:
        self.memory.append({'role': 'user', 'content': text})
        response = ollama.chat(model=self.model, messages=self.memory, tools= [tools.run_query_desc])
        self.memory.append({'role': 'assistant', 'content': response['message']['content']})
        
        # Check if the model decided to use the provided function //debugging purposes
        if not response['message'].get('tool_calls'):
            print("The model didn't use the function. Its response was:")
            return response['message']['content']
        
        # Process function calls made by the model
        if response['message'].get('tool_calls'):
            available_functions = {}
            for tool in self.tool_list:
                available_functions.update({tool[0]['function']['name']: tool[1]})
            for tool in response['message']['tool_calls']:
                function_to_call: Callable = available_functions[tool['function']['name']]
                if function_to_call.__name__ == 'run_query': #find a way for this to not be ifs but rather modular statement
                    function_response: str = function_to_call(tool['function']['arguments']['query'])
                    self.memory.append(
                        {
                        'role': 'tool',
                        'content': function_response,
                        }
                    )
                    
        final_response: Dict[str, Any] = ollama.chat(model=self.model, messages=self.memory)
        return final_response['message']['content']
        
    def save_memory(self) -> None:
        log_filename = f"assistant_memory_{self.model}_{self.creation_date}.log"
        with open(log_filename, 'w') as log_file:
            for entry in self.memory:
                log_file.write(f"{entry['role']}: {entry['content']}\n")
        raise NotImplementedError("This method is not implemented yet")
    
    
    
