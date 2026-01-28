import wave
from piper import PiperVoice

voice = PiperVoice.load("voices/es_MX-claude-high.onnx")
with wave.open("test.wav", "wb") as wav_file:
    voice.synthesize_wav("Esto es una prueba de síntesis de voz", wav_file)