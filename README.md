## About
This bot helps users to practice and improve English speaking skills. The bot takes a voice message or a text message and answers like a Tutor. <br>
It supports as many languages as OpenAI GPT 3.5 model. However voice message generation depends on ElevenLabs TTS model.

## Documentation
### 1. Prerequisite libraries
- Aiogram
- OpenAI
- Asyncio
- ElevenLabs

### 2. Clone the repository
```
git clone https://github.com/iamboisov/kai-tutor.git
```

### 3. Create a file in the root folder with .env extension
Create a file with the .env extension to put the API keys of third-party services in it

### 4. API keys
Get API keys from Telegram BotFather, OpenAI and ElevenLabs

### 5. Copy and paste the following code into the .env file.
```
BOT_KEY = "API_KEY"
OPENAI_KEY = "API_KEY"
ELEVEN_LABS = "API_KEY"
```
Put your API keys instead of API_KEY. Do not forget to put the quotes.
### 6. Run main.py
```
python main.py
```
## License
The project KAI Tutor is distributed under the MIT license.