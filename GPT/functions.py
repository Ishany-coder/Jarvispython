def search_youtube(query):
    import webbrowser
    link = f'https://www.youtube.com/results?search_query={query}'
    webbrowser.open(link)
    return f'Searching on YouTube for \"{query}\"'
    
def search_google(query):
    import webbrowser
    print("searching on google for " + query)
    link = f'https://www.google.com/search?q={query}'
    webbrowser.open(link)
    return f'Searching on Google for \"{query}\"'
def create_new_folder(foldername, dir):
    # importing os module  
    import os 
    
    # Directory 
    directory = foldername
    
    # Parent Directory path 
    parent_dir = "/Users/ishanghosh/" + dir.capitalize()
    # Path 
    path = os.path.join(parent_dir, directory) 

    try: 
        os.mkdir(path) 
        print("Directory '%s' created" %directory)
    except FileExistsError:
        print('this folder has already been made')
    except Exception as e:
        print('error ' + str(e))
def writecode(filename, directory, prompt):
    import openai
    import GPT.apiKey as key
    import os
# Set your API key
    openai.api_key = os.getenv("OPENAI_API_KEY", key.apikey)


    file = open(f"/Users/ishanghosh/{directory.capitalize()}/{filename}", "w")

    # Prepare the messages
    messages = [
        {"role": "system", "content": "You are a helpful assistant used only for coding who write the code in python"},
        {"role": "user", "content": str(prompt)}
    ]

    # Make the API call
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    file.writelines(response.choices[0].message.content)
    file.close()
