import cleo
import tools
import webview
import os

# Chat history to store messages between user and assistant
chat_history = []

class API:
    def __init__(self, assistant):
        self.assistant = assistant

    def handle_input(self, user_input):
        if user_input:
            # Generate a response from the assistant
            response = self.assistant.prompt(user_input)
            chat_history.append({"role": "user", "text": user_input})
            chat_history.append({"role": "assistant", "text": response})
            return self.format_chat_history()
        return ""

    def format_chat_history(self):
        # Create HTML for chat history
        html = ""
        html += f'<div class="assistant-message">{chat_history[-1]["text"]}</div>'
        return html

if __name__ == '__main__':
    # Initialize the assistant here
    print("Cleo is starting...")
    my_assistant = cleo.Assistant(
        model='Jarvis',
        tool_list=[(tools.run_query_desc, tools.run_query)]
    )

    # Path to the HTML file inside the 'site' folder
    html_file_path = os.path.join(os.path.dirname(__file__), 'site', 'index.html')

    # Use 'file://' URL scheme to load the HTML file
    url = f'file://{html_file_path}'

    # Create the PyWebView window and pass the API
    api = API(my_assistant)
    window = webview.create_window("Cleo Assistant", url=url, js_api=api)
    webview.start()
