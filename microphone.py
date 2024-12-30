import os
import wave
import pyaudio
import keyboard  # Requires `keyboard` library for detecting key press

class Microphone:
    def __init__(self, archive="archive", device_index=None):
        self.archive = archive
        self.device_index = device_index  # Optional: Use a specific microphone device
        self.sample_rate = 16000
        self.chunk_size = 1024  # Buffer size for audio chunks
        self.format = pyaudio.paInt16  # Audio format
        self.channels = 1  # Mono audio
        self.p = pyaudio.PyAudio()

    def record(self, file: str):
        """Record audio from the microphone until a key press is detected."""
        print("Recording... Press 'q' to stop.")
        stream = self.p.open(format=self.format,
                             channels=self.channels,
                             rate=self.sample_rate,
                             input=True,
                             frames_per_buffer=self.chunk_size,
                             input_device_index=self.device_index)

        frames = []
        while True:
            if keyboard.is_pressed('q'):  # Stop recording on 'q' key press
                print("Recording stopped.")
                break
            data = stream.read(self.chunk_size)
            frames.append(data)

        stream.stop_stream()
        stream.close()

        # Save the recorded audio to the specified file
        path = os.path.join(self.archive, file)
        import pdb; pdb.set_trace()
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


