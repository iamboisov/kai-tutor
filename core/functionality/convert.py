import subprocess


def convert(input_file, output_file):
    ffmpeg_cmd = [
        'ffmpeg',
        '-i', input_file,
        '-acodec', 'libmp3lame',
        '-ab', '192k',
        '-ar', '44100',
        '-y',
        output_file
    ]

    try:
        subprocess.run(ffmpeg_cmd, check=True)
        print("Success")
    except subprocess.CalledProcessError as e:
        print("Conversion failed")


# convert('D:/Code/Python/kai_v1/voice_messages/voice.ogg',
#         'D:/Code/Python/kai_v1/voice_messages/voice.mp3')
