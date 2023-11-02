from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import FSInputFile
from main import bot
from core.functionality.convert import convert
from core.functionality.transcribe import transcribe_voice
from get_keys import OPENAI_KEY
import openai
from aiogram.methods import SendChatAction

openai.api_key = OPENAI_KEY

router = Router()


@router.message(Command('start'))
async def get_start(message: Message):
    await message.answer('Hello my friend')


@router.message(F.voice)
async def get_voice(message: Message):
    await bot.send_chat_action(message.chat.id, action="record_voice")
    voice_message = await bot.get_file(message.voice.file_id)
    await bot.download_file(voice_message.file_path, f'D:/Code/Python/kai_v1/voice_messages/voice{message.chat.id}.ogg')
    convert(f'D:/Code/Python/kai_v1/voice_messages/voice{message.chat.id}.ogg',
        f'D:/Code/Python/kai_v1/voice_messages/voice{message.chat.id}.mp3')
    transcribe_voice(f'D:/Code/Python/kai_v1/voice_messages/voice{message.chat.id}.mp3', message.chat.id)
    local_voice = FSInputFile(f"D:/Code/Python/kai_v1/voice_messages/generated{message.chat.id}.mp3")
    await message.answer_voice(local_voice)


@router.message(F.text)
async def send_message(message: Message):
    await bot.send_chat_action(message.chat.id, action="typing")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system",
                "content": "You are Kai Tutor.You teach English to Russian students.Ask questions when needed. We talk like in dialogue.Don't answer long.If users asks you,think of something.Answer 120 characters maximum."}, {
            "role": "user",
            "content": message.text
        }],
        temperature=0.5,
        max_tokens=48
    )
    answer = response['choices'][0]['message']['content']
    await message.answer(answer)
