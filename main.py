import cleo
import tools


run = True 
if __name__ == '__main__':
    print("Cleo is starting...")
    
    my_assistant = cleo.Assistant(model='Jarvis',tool_list = [ (tools.run_query_desc, tools.run_query),(tools.bullshit_desc, tools.bullshit)])
    while run:
        current = input("Speak: ")
        if current:
            response = my_assistant.prompt(current)
            print(response)
        print(run)