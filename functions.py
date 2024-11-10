def SearchYoutube(query):
    import webbrowser
    link = f'https://www.youtube.com/results?search_query={query["query"]}'
    webbrowser.open(link)
    return f'Searching on YouTube for "{query}'
def SearchGoogle(query):
        import webbrowser
        link = f'https://www.google.com/search?q={query}'
        webbrowser.open(link)
        return f'Searching on Google for "{query}'