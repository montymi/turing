import argparse
from linguist import Linguist

def main():
    parser = argparse.ArgumentParser(description="CLI for TTS and STT using Linguist")
    subparsers = parser.add_subparsers(dest="command")
    
    # Configuration
    parser.add_argument("--use_gpu", action="store_true", help="Flag to use GPU for TTS")
    parser.add_argument("--output_file", type=str, default="output.wav", help="Output file for TTS")
    parser.add_argument("--archive", type=str, default="archive", help="Archive directory for TTS")
    parser.add_argument("--coqui_model", type=str, default="tts_models/multilingual/multi-dataset/your_tts", help="Model name for Coqui-AI TTS")
    parser.add_argument("--whisper_model", type=str, default="base", help="Whisper model for STT")

    # Speak command
    speak_parser = subparsers.add_parser("speak", help="Convert text to speech")
    speak_parser.add_argument("text", type=str, help="Text to convert to speech")
    speak_parser.add_argument("--language", type=str, help="Language for TTS")
    speak_parser.add_argument("--speaker", type=str, help="Speaker for TTS")

    # Listen command
    listen_parser = subparsers.add_parser("listen", help="Convert speech to text")
    listen_parser.add_argument("--print", action="store_true", default=True, help="Flag to print the recognized text")
    listen_parser.add_argument("--duration", type=int, default=5, help="Duration of recording in seconds")

    # Help command
    help_parser = subparsers.add_parser("help", help="Show help message")
    help_parser.set_defaults(func=lambda _: parser.print_help())

    args = parser.parse_args()

    if args.command in ["speak", "listen"]:
        # Initialize Linguist with the provided arguments
        linguist = Linguist(
            use_gpu=args.use_gpu,
            output_file=args.output_file,
            archive=args.archive,
            coqui_model=args.coqui_model,
            whisper_model=args.whisper_model
        )

        linguist.init()

        # Handle commands
        if args.command == "speak":

            # Set language and speaker if provided
            if args.language:
                linguist.set_language(args.language)
            if args.speaker:
                linguist.set_speaker(args.speaker)

            # Generate speech from text
            linguist.speak(args.text)

        elif args.command == "listen":

            # Record audio until 'q' key press
            audio = linguist.listen()

            # Transcribe the recorded audio file
            text = linguist.transcribe(audio, show_text=args.print)

    else:
        # Show help message
        parser.print_help()

if __name__ == '__main__':
    main()