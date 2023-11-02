import elevenlabs
import sys
from get_keys import ELEVEN_LABS
sys.path.append('D:/Code/Python/kai_v1')
elevenlabs.set_api_key(ELEVEN_LABS)


voice = elevenlabs.Voice(
    voice_id="Rachel",
    settings=elevenlabs.VoiceSettings(
        stability=0.5,
        similarity_boost=0.6,
        speaking_rate=0.7
    )
)

def generate_tts(from_gpt, chat_id):
    audio = elevenlabs.generate(    
    text=from_gpt,
    voice="Rachel",
    model="eleven_multilingual_v2"
    )
    elevenlabs.save(audio, f"D:/Code/Python/kai_v1/voice_messages/generated{chat_id}.mp3")
