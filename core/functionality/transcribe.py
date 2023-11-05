import sys
import openai
sys.path.append('D:/Code/Python/kai_v1')
from get_keys import OPENAI_KEY
from core.functionality.generation import generate_answer

openai.api_key = OPENAI_KEY

def transcribe_voice(audio_path: str, chat_id):
    audio_file = open(audio_path, "rb")
    transcript = openai.Audio.transcribe(
    "whisper-1", file=audio_file, response_format="text")
    generate_answer(transcript, chat_id)
