from GPT.callGPT import call_chatgpt
import sound.stt as stt
from sound.tts import TTS

result = call_chatgpt(stt.text)
print(result)