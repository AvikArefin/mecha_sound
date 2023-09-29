from pydub import AudioSegment
import json
import os

keyboard_name = "eg-oreo"
audio_type = "wav"

audio_file_path = ".\keyboardsounds\\" + keyboard_name + "\sound." + audio_type

sound = AudioSegment.from_file(audio_file_path)

audio_str_map = json.load(open(".\keyboardsounds\\" + keyboard_name + "\config.json"))['defines']

# Specify the directory path you want to create
audio_output_path = "./audio_split_output/" + keyboard_name

# Check if the directory doesn't already exist
if not os.path.exists(audio_output_path):
    # Create the directory
    os.makedirs(audio_output_path)
    print(f"Created directory: {audio_output_path}")
else:
    print(f"Directory already exists: {audio_output_path}")


for keys, timestamps in audio_str_map.items():
    if timestamps is not None:
        sound_i = sound[timestamps[0]: timestamps[0] + timestamps[1]]
        sound_i.export(audio_output_path + "/" + keys + "." + audio_type, format=audio_type)