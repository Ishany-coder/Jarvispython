class Functions:
    def __init__(self):
        pass
    
    def search_youtube(self, query):
        import webbrowser
        link = f'https://www.youtube.com/results?search_query={query}'
        webbrowser.open(link)
        return f'Searching on YouTube for \"{query}\"'
    
    def search_google(self, query):
        import webbrowser
        link = f'https://www.google.com/search?q={query}'
        webbrowser.open(link)
        return f'Searching on Google for \"{query}\"'