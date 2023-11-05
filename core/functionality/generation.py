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
                "content": "You are Kai Tutor.You teach languages.Provide answers maximum 150 characters according to example:'To help you learn both English and Russian,let's start with some basic phrases.In English, 'Good morning' means wishing someone a nice morning, while in Russian, it's 'Доброе утро.' I'll provide answers in both languages.What other phrases or words would you like to learn?'.Continue dialogue and suggest other options.Never provide code,only plain English."}, {
            "role": "user",
            "content": transcription
        }],
        temperature=0.5,
        max_tokens=256
    )
    answer = str(response['choices'][0]['message']['content'])
    generate_tts(answer, chat_id)
    # print(response['choices'][0]['message']['content'])

# generate_answer("Let's start")