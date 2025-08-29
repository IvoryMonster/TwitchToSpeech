import os
import TTS

AZURE_VOICES = [
    "en-US-DavisNeural",
    "en-US-TonyNeural",
    "en-US-JasonNeural",
    "en-US-GuyNeural",
    "en-US-JaneNeural",
    "en-US-NancyNeural",
    "en-US-JennyNeural",
    "en-US-AriaNeural",
    "en-US-SaraNeural",
]

for voice in AZURE_VOICES:
    print(f"Now Testing {voice}:")
    TTS.speak(f"Now Testing {voice}", 'hopeful', voice)
    print('Normal...')
    TTS.speak("Lorem ipsum dolor sit amet, consectetur adipiscing elit.", 'hopeful,', voice)
    print('Whispering...')
    TTS.speak("Lorem ipsum dolor sit amet, consectetur adipiscing elit.", 'whispering', voice)
    print('Shouting...')
    TTS.speak("Lorem ipsum dolor sit amet, consectetur adipiscing elit.", 'shouting', voice)