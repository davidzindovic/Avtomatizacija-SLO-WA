import sounddevice as sd
import numpy as np
import queue
import torch
from transformers import pipeline
import argparse

# Set up argument parsing
parser = argparse.ArgumentParser(description='Slovenian keyword spotter (Microphone)')
parser.add_argument('--output', type=str, default="keywords_detected.txt",
                    help='Output file for detected keywords')
args = parser.parse_args()

# Target Slovenian words to detect
TARGET_WORDS = ["pokliči", "napiši", "monika", "darja", "helena"]

# Audio parameters for microphone
SAMPLE_RATE = 16000
CHANNELS = 1  # Microphone is typically mono
BLOCKSIZE = 8000  # 0.5 second chunks
DEVICE = 1  # Will use default microphone

# Initialize Whisper model
print("Loading Whisper model... (this may take a moment)")
pipe = pipeline("automatic-speech-recognition",
                model="openai/whisper-small",
                device="cuda" if torch.cuda.is_available() else "cpu")

# Audio queue
audio_queue = queue.Queue()

def audio_callback(indata, frames, time, status):
    """Called for each audio block from microphone."""
    if status:
        print(status, flush=True)
    audio_queue.put(indata.copy())

def contains_target_words(text, words):
    """Check if text contains any of the target words"""
    text_lower = text.lower()
    detected = [word for word in words if word.lower() in text_lower]
    return detected

# List available audio devices
print("Available audio devices:")
print(sd.query_devices())

print(f"\nListening for Slovenian words: {', '.join(TARGET_WORDS)}")
print("Speak into your microphone. Press Ctrl+C to stop...")

try:
    with open(args.output, "w", encoding="utf-8") as outfile:
        with sd.InputStream(samplerate=SAMPLE_RATE,
                         blocksize=BLOCKSIZE,
                         device=DEVICE,
                         dtype='float32',
                         channels=CHANNELS,
                         callback=audio_callback):
            while True:
                data = audio_queue.get()
                audio_np = np.frombuffer(data, dtype=np.float32)
                
                # Recognize speech with forced Slovenian language
                result = pipe(audio_np, generate_kwargs={"language": "slovenian"})
                text = result['text'].strip()
                
                if text:
                    detected = contains_target_words(text, TARGET_WORDS)
                    if detected:
                        print(f"✅ Detected: {', '.join(detected)} in: '{text}'")
                        for word in detected:
                            outfile.write(f"{word} (in: '{text}')\n")
                        outfile.flush()
                    else:
                        print(f"Heard: '{text}'")

except KeyboardInterrupt:
    print("\nRecording stopped.")
except Exception as e:
    print("Error:", str(e))