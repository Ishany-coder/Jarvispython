import speech_recognition as sr
# Create a recognizer object
r = sr.Recognizer()

# Use the microphone as the source
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# Recognize the speech
try:
    text = r.recognize_google(audio)
    print('you said ' + text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
