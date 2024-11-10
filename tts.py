import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty("rate", 150)  # Speed of speech
engine.setProperty("volume", 1.0)  # Volume (0.0 to 1.0)

# Text to speak
text = "Hello! How can I assist you today?"

# Speak the text
engine.say(text)
engine.runAndWait()