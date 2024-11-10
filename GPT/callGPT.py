import openai
import os
import json
import apiKey
from GPT.GPTfunctions import SearchGoogle
from GPT.GPTfunctions import SearchYoutube

# Set your API key
openai.api_key = os.getenv("OPENAI_API_KEY", apiKey.apikey)

# Define the function calling structure
functions = [
    {
        "name": "search_google",
        "description": "Searches google for a query",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The query to search on google"
                },
            },
            "required": ["query"],
        }
    },
    {

        "name": "open_youtube",
        "description": "opens youtube and searches for a video with a given query",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The query to search on youtube"
                },
            },
            "required": ["query"],
        }
    }
]

# Function to call ChatGPT with function calling
def call_chatgpt(prompt):
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": [{"type": "text", "text": prompt}]}
        ],
        functions=functions,
        function_call="auto",
    )
    
    # Access the message from the response
    message = response.choices[0].message
    
    # Check if the message includes a function call
    if hasattr(message, "function_call") and message.function_call is not None:
        function_call = message.function_call
        function_name = function_call.name
        function_parameters = function_call.arguments
        query = json.loads(function_parameters)

        # Handle function calls
        if function_name == 'search_google':
            SearchGoogle(query['query'])
        elif function_name == 'open_youtube':
            SearchYoutube(query['query'])
    # If no function call, return the assistant's response content
    return message.content
