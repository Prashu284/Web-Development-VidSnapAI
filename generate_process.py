# import os
# from text_to_audio import text_to_speech_file

# def text_to_audio(folder):
#     print("TTA - ", folder)
#     with open(f"user_uploads/{folder}/desc.txt", "r") as f:
#         text = f.read()
#     print(text, folder)
#     # text_to_speech_file(text,folder)

# def create_reel(folder):
#     print("CR - ", folder)

# if __name__ == "__main__":
#     with open("done.txt", "r") as f:
#         done_folders = f.readlines()

#     done_folders = [f.strip() for f in done_folders]
#     folders = os.listdir("user_uploads")
#     for folder in folders:
#         if (folder not in done_folders):
#             text_to_audio(folder) # Generate the audio.mp3 from desc.txt
#             create_reel(folder) # convert the images and audio.mp3 inside the folder to a reel
#             with open("done.txt", "a") as f:
#                 f.write(folder + "\n")
import os
from text_to_audio import text_to_speech_file
import time
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_ROOT = os.path.join(BASE_DIR, "user_uploads")
DONE_FILE = os.path.join(BASE_DIR, "done.txt")

def text_to_audio(folder):
    print("TTA -", folder)

    desc_path = os.path.join(UPLOAD_ROOT, folder, "desc.txt")

    if not os.path.exists(desc_path):
        print(f"⚠️ Skipping {folder}: desc.txt not found")
        return False

    with open(desc_path, "r", encoding="utf-8") as f:
        text = f.read().strip()

    if not text:
        print(f"⚠️ Skipping {folder}: desc.txt is empty")
        return False

    print(text, folder)
    text_to_speech_file(text, folder)
    return True


def create_reel(folder):
    command = ""
    subprocess.run(command, shell=True, check=True)

    print("CR -", folder)
    # Later: ffmpeg / moviepy logic


if __name__ == "__main__":
    while True:
        print("Processing Queue...")

        if os.path.exists(DONE_FILE):
            with open(DONE_FILE, "r") as f:
                done_folders = [line.strip() for line in f.readlines()]
        else:
            done_folders = []

        folders = os.listdir(UPLOAD_ROOT)

        for folder in folders:
            if folder in done_folders:
                continue

            success = text_to_audio(folder)
            if not success:
                continue   # ⛔ do NOT mark done

            create_reel(folder)

            with open(DONE_FILE, "a") as f:
                f.write(folder + "\n")
        time.sleep(15)