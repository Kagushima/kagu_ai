from core.brain import think
from tts.tts import speak_to_file
import winsound
import json

personality = json.load(open("data/personality.json"))

while True:
    user = input("Tú: ").strip()
    if not user:
        continue

    ai_text = think(personality['name'], user)
    print("KaguAI:", ai_text)

    # Genera un WAV con la respuesta
    wav_file = f"audio/response.wav"
    speak_to_file(ai_text, wav_file)

    # Reproduce el audio
    winsound.PlaySound(wav_file, winsound.SND_FILENAME)
