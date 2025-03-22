from GPT.callGPT import call_chatgpt
from stt import stt

def main():
    text = input("what would you like to ask chatGPT? ")
    memory = []
    while text != 'exit':
        result = call_chatgpt(text, memory)
        print("chatGPT says " + str(result[0]))
        text = input("What would you like to ask chatGPT next? ")
main()