from GPT.callGPT import call_chatgpt
from stt import stt

def main():
    text = stt()
    memory = []
    while text != 'exit':
        result = call_chatgpt(text, memory)
        print("chatGPT says " + str(result[0]))
        text = stt()
main()