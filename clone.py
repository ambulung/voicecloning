import torch
from TTS.api import TTS
import os

# 0. Check for GPU and set device
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")
if device == "cuda":
    print(f"GPU: {torch.cuda.get_device_name(0)}")

# 1. Define paths
reference_audio_path = "input.wav" # <--- IMPORTANT: REPLACE THIS
text_to_speak = "We passed upon the stairs. We spoke of was and when. Although I wasn't there. He said I was his friend. Which came as a surprise. I spoke into his eyes thought you died alone. A long long time ago"
output_audio_path = "cloned_voice_output.wav"

# --- Sanity Check for reference audio ---
if not os.path.exists(reference_audio_path):
    print(f"ERROR: Reference audio file not found at '{reference_audio_path}'")
    print("Please make sure you have a .wav file at that location.")
    print("You can record one or use an existing clean audio sample.")
    # Create a dummy file for demonstration if it doesn't exist,
    # but this will NOT produce good results without a real voice.
    # This is just to make the script runnable for a quick test.
    try:
        import soundfile as sf
        import numpy as np
        print(f"Creating a DUMMY empty '{reference_audio_path}' for script execution. REPLACE IT with a real voice sample!")
        samplerate = 22050 # A common samplerate
        duration = 5 # seconds
        frequency = 440 # Hz
        amplitude = 0.5
        t = np.linspace(0, duration, int(samplerate * duration), False)
        note = amplitude * np.sin(2 * np.pi * frequency * t)
        # Add some silence to make it slightly more "speech-like" for the model
        silence = np.zeros(int(samplerate*0.5))
        dummy_audio = np.concatenate((silence, note, silence, note, silence))
        sf.write(reference_audio_path, dummy_audio, samplerate)
    except ImportError:
        print("Could not create dummy audio: soundfile or numpy not found. Please install them or provide a real audio file.")
        exit()
    except Exception as e:
        print(f"Could not create dummy audio: {e}. Please provide a real audio file.")
        exit()
# --- End Sanity Check ---


# 2. Initialize TTS model
# XTTSv2 is a multilingual model that's good for voice cloning.
# It will download the model files on the first run (can take a while).
print("Initializing TTS model... This might take a while on the first run to download.")
try:
    # Using XTTSv2 model
    # You can list available models with: `tts --list_models` in your terminal
    # Or explore here: https://github.com/coqui-ai/TTS/blob/dev/TTS/tts/configs/xtts_v2/README.md
    model_name = "tts_models/multilingual/multi-dataset/xtts_v2"
    tts = TTS(model_name=model_name, progress_bar=True).to(device)
    print("TTS model loaded successfully.")
except Exception as e:
    print(f"Error initializing TTS model: {e}")
    print("Make sure you have a stable internet connection if this is the first run.")
    print("If issues persist, check the Coqui TTS GitHub issues page.")
    exit()

# 3. Perform Voice Cloning (TTS synthesis)
print(f"Cloning voice from: {reference_audio_path}")
print(f"Text to synthesize: '{text_to_speak}'")

try:
    tts.tts_to_file(
        text=text_to_speak,
        speaker_wav=reference_audio_path,
        language="en",  # Specify the language of the text (and reference audio)
                       # XTTSv2 supports: en, es, fr, de, it, pt, pl, tr, ru, nl, cs, ar, zh-cn, ja, hu, ko
        file_path=output_audio_path
    )
    print(f"Cloned audio saved to: {output_audio_path}")
    print("You can play this file with any audio player.")
except FileNotFoundError:
    print(f"ERROR: Could not find the reference audio file at '{reference_audio_path}'.")
    print("Please ensure the file exists and the path is correct.")
except Exception as e:
    print(f"An error occurred during TTS synthesis: {e}")

# To play the audio directly in Python (optional, needs a player or library like simpleaudio/pydub)
# For example, using simpleaudio:
# pip install simpleaudio
# try:
#     import simpleaudio as sa
#     wave_obj = sa.WaveObject.from_wave_file(output_audio_path)
#     play_obj = wave_obj.play()
#     play_obj.wait_done()
# except ImportError:
#     print("To play audio directly, install simpleaudio: pip install simpleaudio")
# except Exception as e:
#     print(f"Could not play audio: {e}")