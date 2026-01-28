from core.brain import Brain
from tts.tts import speak_to_file
import winsound

brain = Brain()

while True:
    user = input("Tú: ")
    if user.lower() in ["exit", "quit"]:
        break

    response = brain.think(user)
    print("KaguAI:", response)

    # Genera un WAV con la respuesta
    wav_file = f"audio/response.wav"
    speak_to_file(response, wav_file)

    # Reproduce el audio
    winsound.PlaySound(wav_file, winsound.SND_FILENAME)
