import openai
import os
import json
import GPT.apiKey as apiKey
from GPT.functions import search_youtube
from GPT.functions import search_google
from GPT.functions import create_new_folder
from GPT.functions import writecode

# Set your API key
openai.api_key = os.getenv("OPENAI_API_KEY", apiKey.apikey)

# Define the function calling structure
functions = [
    {
        "name": "search_google",
        "description": "Searches Google for a query",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The query to search on Google"
                },
            },
            "required": ["query"],
        }
    },
    {
        "name": "open_youtube",
        "description": "Opens YouTube and searches for a video with a given query",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The query to search on YouTube"
                },
            },
            "required": ["query"],
        }
    },
    {
        "name": "create_folder",
        "description": "Creates folder with a certain name",
        "parameters": {
            "type": "object",
            "properties": {
                "foldername": {
                    "type": "string",
                    "description": "The name of the folder to create"
                },
                "directory": {
                    "type": "string",
                    "description": "The directory to put the file in"
                }
            },
            "required": ["foldername", "directory"],
        }
    },
    {
        "name": "write_code",
        "description": "writes code in a file with a certain name in a certain folder directory",
        "parameters": {
            "type": "object",
            "properties": {
                "filename": {
                    "type": "string",
                    "description": "The name of the folder to create"
                },
                "directory": {
                    "type": "string",
                    "description": "The directory to put the file in"
                },
                "prompt": {
                    "type": "string",
                    "description": "The code to write"
                },
            },
            "required": ["filename", "directory", "prompt"],
        }
    },
]

# Function to call ChatGPT with function calling
def call_chatgpt(prompt, memory):
    # Make a shallow copy of memory to avoid accidental circular references
    conversation_history = memory
    
    # Append the user input to the conversation history
    conversation_history.append({"role": "user", "content": prompt})
    if type(prompt) != str:
        prompt = ''
    # Call GPT with the conversation history
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=conversation_history,
        functions=functions,
        function_call="auto",
    )
    # Access the message from the response
    message = response.choices[0].message
    
    # Append GPT's response to the conversation history
    conversation_history.append({"role": "assistant", "content": str(message.content)})
    
    # Check if the message includes a function call
    if hasattr(message, "function_call") and message.function_call is not None:
        function_call = message.function_call
        function_name = function_call.name
        function_parameters = function_call.arguments
        params = json.loads(function_parameters)

        # Handle function calls
        if function_name == 'search_google':
            print('searching on google for ' + params['query'])
            search_google(params['query'])
        elif function_name == 'open_youtube':
            search_youtube(params['query'])
        elif function_name == 'create_folder':
            print("creating new folder " + params["foldername"] + " in directory " + params["directory"])
            create_new_folder(params['foldername'], params["directory"])
        elif function_name == 'write_code':
            print('writing code: ' + str(params['prompt']) + 'in file ' + str(params['filename']) + "in directory " + str(params['directory']))
            writecode(params['filename'], params['directory'], params['prompt'])
    # Return GPT's response and the updated memory
    return message.content, conversation_history