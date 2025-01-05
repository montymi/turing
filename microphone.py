import os
import wave
import pyaudio
import threading

class Microphone:
    def __init__(self, archive="archive", device_index=None):
        self.archive = archive
        self.device_index = device_index  # Optional: Use a specific microphone device
        self.sample_rate = 16000
        self.chunk_size = 1024  # Buffer size for audio chunks
        self.format = pyaudio.paInt32  # Audio format
        self.channels = 1  # Mono audio
        self.p = pyaudio.PyAudio()

    def record(self, file: str):
        """Record audio from the microphone until user input is detected."""
        print("🎤 Recording in progress... Press Enter to stop. 🔴")
        stream = self.p.open(format=self.format,
                             channels=self.channels,
                             rate=self.sample_rate,
                             input=True,
                             frames_per_buffer=self.chunk_size,
                             input_device_index=self.device_index)

        frames = []

        def stop_recording():
            input()
            nonlocal recording
            recording = False

        recording = True
        stop_thread = threading.Thread(target=stop_recording)
        stop_thread.start()

        while recording:
            data = stream.read(self.chunk_size)
            frames.append(data)

        stop_thread.join()

        stream.stop_stream()
        stream.close()

        # Save the recorded audio to the specified file
        path = os.path.join(self.archive, file)
        with wave.open(path, 'wb') as wf:
            wf.setnchannels(self.channels)
            wf.setsampwidth(self.p.get_sample_size(self.format))
            wf.setframerate(self.sample_rate)
            wf.writeframes(b''.join(frames))

    def samples(self):
        print("Input Samples:")
        [print(file) for file in os.listdir(self.archive)]

    def __del__(self):
        """Ensure proper cleanup of resources."""
        self.p.terminate()
