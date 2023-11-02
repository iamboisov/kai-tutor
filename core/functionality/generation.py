# Получение ответа от GPT
import sys
sys.path.append('D:/Code/Python/kai_v1/')
import openai
from get_keys import OPENAI_KEY
from core.functionality.tts import generate_tts

openai.api_key = OPENAI_KEY

def generate_answer(transcription, chat_id):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system",
                "content": "You are Kai Tutor.You teach English to Russian students.Ask questions when needed. We talk like in dialogue.Don't answer long.If users asks you,think of something."}, {
            "role": "user",
            "content": transcription
        }],
        temperature=0.5,
        max_tokens=48
    )
    answer = str(response['choices'][0]['message']['content'])
    generate_tts(answer, chat_id)
    # print(response['choices'][0]['message']['content'])

# generate_answer("Let's start")