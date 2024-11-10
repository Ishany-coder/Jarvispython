def TTS(text):
    import pyttsx3
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)  # Speed of speech
    engine.setProperty("volume", 0.5)  # Volume (0.0 to 1.0)
    engine.say(text)
    engine.runAndWait()