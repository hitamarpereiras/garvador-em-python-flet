import pyaudio
import wave
from time import sleep
import os

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100 # Taxa em Hz
CHUNK = 1024 # buffer size
#RECORD_SECONDS = 60 # Tempo de gravacao
#OUTPUT_FILENAME = 'rec_python.wav' # Nome de saida 

# Inicializando o pyAudio
audio = pyaudio.PyAudio()

stream_a = None
frames = []
recording = False

def recording_mic():
    global stream_a, frames, recording
    if not recording:
        recording = True
        frames = []

        stream_a = audio.open(
            format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            input=True,
            frames_per_buffer=CHUNK
        )
    rec_now()

def rec_now():
    global stream_a, frames, recording
    while recording:
        data = stream_a.read(CHUNK)
        frames.append(data)

def stop_rec():
    global stream_a, recording
    if recording:
        recording = False
        sleep(2)
        stream_a.stop_stream()
        stream_a.close()

def save_recording(name_file):
        # Salvando dados em formato WAV
        aw = wave.open(name_file, 'wb')
        aw.setnchannels(CHANNELS)
        aw.setsampwidth(audio.get_sample_size(FORMAT))
        aw.setframerate(RATE)
        aw.writeframes(b''.join(frames))
        aw.close()

        os.makedirs(f'./Recordings', exist_ok=True)
        os.rename(f"./{name_file}", f"./Recordings/{name_file}")