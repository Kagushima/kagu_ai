import wave
from piper import PiperVoice

# Carga del modelo ONNX + JSON
VOICE_MODEL = "voices/es_MX-claude-high.onnx"
VOICE_CONFIG = "voices/es_MX-claude-high.onnx.json"

# Carga la voz con la configuración
voice = PiperVoice.load(VOICE_MODEL, VOICE_CONFIG)

def speak_to_file(text: str, output_path: str):
    """
    Genera un archivo WAV con el texto dado.
    """
    with wave.open(output_path, "wb") as wav_file:
        voice.synthesize_wav(text, wav_file)

    return output_path