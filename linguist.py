from TTS.api import TTS
import shutil
import subprocess
import os
import sys
from microphone import Microphone
from datetime import datetime
import whisper
import warnings

warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead") # Ignore FP16 warning because it defaults to FP32

class Linguist:
    def __init__(
            self, 
            coqui_model="tts_models/multilingual/multi-dataset/your_tts", 
            use_gpu=False, 
            output_file="output.wav", 
            archive="archive", 
            whisper_model="base"
        ):
        self.coqui_model = coqui_model
        self.use_gpu = use_gpu
        self.whisper_model = whisper_model
        self.default_output = output_file
        self.language = None
        self.speaker_file = None
        self.speaker = None
        self.archive = archive

    def __init_TTS__(self):
        sys.stdout = open(os.devnull, 'w')
        sys.stderr = open(os.devnull, 'w')
        self.tts = TTS(model_name=self.coqui_model, gpu=self.use_gpu, progress_bar=False)
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

    def init(self):
        self.tts = self.__init_TTS__()
        self.mic = Microphone(archive=self.archive)
        self.whisper_model = whisper.load_model(self.whisper_model)

    def list_languages(self):
        """List available languages for the TTS model."""
        return self.tts.languages

    def set_language(self, lang):
        """Set the language for the TTS model."""
        if lang in self.tts.languages:
            self.language = lang
            print(f"Language set to: {lang}")
        else:
            print(f"Error: Language '{lang}' is not supported.")

    def list_speakers(self):
        """List available speakers for the TTS model."""
        return self.tts.speakers

    def set_speaker(self, speaker_name):
        """Set the speaker for the TTS model."""
        # Clean and filter out empty speakers
        speakers = [speaker.strip() for speaker in self.tts.speakers if speaker.strip()]
        if speaker_name in speakers:
            self.speaker = speaker_name
            print(f"Speaker set to: {speaker_name}")
        else:
            print(f"Error: Speaker '{speaker_name}' is not available. Defaulting to first speaker.")
            self.speaker = speakers[0] if speakers else None

    def set_speaker_embedding(self, audio_path):
        """Set the speaker embedding from a reference audio file."""

        if not audio_path or not os.path.join(self.archive, audio_path):
            print(f"Error: Invalid reference audio path: {audio_path}")
            return
        self.speaker_file = os.path.join(self.archive, audio_path)
        print("Speaker embedding set successfully.")

    def record(self, words: str, output_path=None):
        """Generate speech from text with optional language and speaker embedding."""
        output_path = output_path or self.default_output
        try:
            if self.speaker_file:
                self.tts.tts_to_file(
                    text=words,
                    file_path=output_path,
                    speaker_wav=self.speaker_file,
                    language=self.language,
                )
            else:
                self.speaker = self.speaker or self.tts.speakers[0]
                self.language = self.language or self.tts.languages[0]
                
                self.tts.tts_to_file(
                    text=words,
                    speaker=self.speaker,
                    file_path=output_path,
                    language=self.language,
                )
            print(f"Speech saved to {output_path}")
        except Exception as e:
            print(f"Error during recording: {e}")

    def say(self, path=None):
        """Play the generated audio using 'afplay'."""
        path = path or self.default_output
        if not self._is_afplay_available():
            print("Error: 'afplay' command is not available. Please install or use another player.")
            return
        try:
            subprocess.run(["afplay", path], check=True)
            self.speaker_file = None
        except subprocess.CalledProcessError as e:
            print(f"Error: Unable to play audio. Details: {e}")

    @staticmethod
    def _is_afplay_available():
        """Check if 'afplay' is available on the system."""
        return shutil.which("afplay") is not None
    
    def speak(self, text: str, name: str=datetime.now().strftime("%Y-%m-%d@%H:%M:%S")):
        """Convert text to speech and play it."""
        try:
            self.record(text, name)
            self.say(name)
        except KeyboardInterrupt:
            print("Speaker interrupted. Exiting...")

    def listen(self, name: str=datetime.now().strftime("%Y-%m-%d@%H:%M:%S")+'.wav') -> str:
        """Record audio for a given duration."""
        try:
            if name == "":
                name = input("Name the recording (ENTER for datetime): ") or datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            self.mic.record(file=name)
        except KeyboardInterrupt:
            print("Recording interrupted. Exiting...")
        return name

    def transcribe(self, file: str, show_text: bool) -> str:
        """Transcribe recorded audio to text."""
        try:
            audio_path = os.path.join(self.archive, file)
            if not os.path.exists(audio_path):
                raise FileNotFoundError(f"Audio file not found: {audio_path}")
            print("📝 Transcribing audio... Press Ctrl+C to stop. 🔊")
            result = self.whisper_model.transcribe(audio_path)
            text = result["text"]
            if text:
                print(f"\n📜 Transcription successful ✅")
            if show_text and text:
                print(f"\n❝{text} ❞")
            return text
        except KeyboardInterrupt:
            print("Transcription interrupted. Exiting...")
            return ""
        except Exception as e:
            print(f"Error during transcription: {e}")
            return ""
    

def main():
    linguist = Linguist()

    while True:
        # Step 0: Record User for Voice Cloning
        try:
            selection = input("Record audio clip for voice cloning? (y/N): ") or 'N'
            if selection.lower() in ['y', 'yes']:
                name = input("Name the audio clip (ENTER for datetime): ") or datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                linguist.mic.record(file=name)
        except Exception as e:
            print(f"Error during recording: {e}")

        # Step 1: Set Language
        try:
            print("Available Languages:")
            languages = linguist.list_languages()
            if languages:
                [print(lang) for lang in languages]
                selected_language = input("Select a language (ENTER for Default): ")
                if selected_language in languages:
                    linguist.set_language(selected_language)
                else:
                    print("Invalid language selected. Defaulting to first available language.")
                    linguist.set_language(languages[0])
            else:
                print("No languages available for this model.")
        except Exception as e:
            print(f"Error during language selection: {e}")

        # Step 2: Set Speaker (Optional)
        try:
            print("Available Speakers:")
            speakers = [speaker for speaker in linguist.list_speakers() if speaker]
            if speakers:
                [print(speaker) for speaker in speakers]
                selected_speaker = input(f"Select a speaker (ENTER for Default '{speakers[0]}'): ") or speakers[0]
                linguist.set_speaker(selected_speaker)
            else:
                print("No speakers available for this model. Defaulting to the first available speaker.")
                linguist.set_speaker(speakers[0] if speakers else None)
        except Exception as e:
            print(f"Error during speaker selection: {e}")

        # Step 3: Set Speaker Embedding (Optional)
        try:
            linguist.mic.samples()
            ref_audio = input("Provide path to reference audio for voice cloning (ENTER to skip): ")
            if ref_audio:
                linguist.set_speaker_embedding(ref_audio)
        except Exception as e:
            print(f"Error during speaker embedding: {e}")

        # Step 4: Record Speech
        try:
            text = input("Enter text to convert to speech: ")
            linguist.record(text)
        except Exception as e:
            print(f"Error during speech recording: {e}")

        # Step 5: Play the Audio
        try:
            linguist.say()
        except Exception as e:
            print(f"Error during audio playback: {e}")

        # Ask if the user wants to repeat the process
        again = input("\nWould you like to do another? (y/N): ").lower()
        if again.lower() not in ['y', 'yes']:
            print("Exiting program.")
            break


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        selection = input("\nAborted session. Would you like to restart? (y/N): ")
        if selection.lower() not in ['y', 'yes']:
            print("Exiting program.")
            exit()   
        print("Restarting Linguist and Microphone")
        main()