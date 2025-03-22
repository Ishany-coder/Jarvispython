import speech_recognition as sr
import sys
# Create a recognizer object
r = sr.Recognizer()

# Use the microphone as the source
def stt():
        #With the micropone as the source ask the user to say something and store it into the audio variable
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
        # Recognize the speech
        try:
            text = r.recognize_google(audio)
            print('you said ' + text)
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            sys.exit()
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            sys.exit()
        except KeyboardInterrupt:
             print("Keyboard Interrupt goodbye")