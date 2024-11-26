from GPT.callGPT import call_chatgpt
from stt import stt

def main():
    text = stt()
    while text != 'exit':
        result = call_chatgpt(text)
        print(result)
        text = stt()
main()