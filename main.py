import cleo
import tools
from tkinter import *


run = True 
if __name__ == '__main__':
    print("Cleo is starting...")
    
    
    my_assistant = cleo.Assistant(model='Jarvis',tool_list = [ (tools.run_query_desc, tools.run_query)])
    while run:
        current = input("Speak: ")
        if current:
            response = my_assistant.prompt(current)
            run = my_assistant.active
            print(response)
        print(run)