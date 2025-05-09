import whisper
import ffmpeg
import os
import cv2
import numpy as np
from langdetect import detect
from yt_dlp import YoutubeDL

def download_youtube_video(url, output_path='downloaded_video.mp4'):
    ydl_opts = {
        'outtmpl': output_path,
        'format': 'mp4/bestaudio/best'
    }
    with YoutubeDL(ydl_opts) as ydl:
        print("Downloading video...")
        ydl.download([url])
    return output_path

def extract_audio(video_path, audio_path='audio.wav'):
    ffmpeg.input(video_path).output(audio_path, ac=1, ar='16000').run(quiet=True, overwrite_output=True)
    return audio_path

def extract_key_frames(video_path, output_dir='keyframes', threshold=30):
    print("Extracting key frames...")
    os.makedirs(output_dir, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    prev_frame = None
    index = 0
    saved = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if prev_frame is None:
            prev_frame = gray
            continue

        diff = cv2.absdiff(prev_frame, gray)
        non_zero_count = np.count_nonzero(diff)

        if non_zero_count > threshold * 1000:  # You can fine-tune this
            filename = os.path.join(output_dir, f"frame_{index}.jpg")
            cv2.imwrite(filename, frame)
            saved += 1
            prev_frame = gray

        index += 1

    cap.release()
    print(f"Saved {saved} key frames.")
    return output_dir

def transcribe_audio(audio_path, model_size='medium'):
    print("Loading Whisper model...")
    model = whisper.load_model(model_size)
    result = model.transcribe(audio_path, task="transcribe", language=None, verbose=True)
    transcript = result["text"]
    segments = result.get("segments", [])

    languages = set()
    for seg in segments:
        try:
            lang = detect(seg["text"])
            languages.add(lang)
        except:
            continue

    print(f"Detected languages: {languages}")
    return transcript, languages

def main(youtube_url):
    video_file = 'video.mp4'
    audio_file = 'audio.wav'

    download_youtube_video(youtube_url, video_file)
    extract_audio(video_file, audio_file)
    extract_key_frames(video_file, 'keyframes')

    transcript, languages = transcribe_audio(audio_file, model_size='large')
    
    with open('transcript.txt', 'w', encoding='utf-8') as f:
        f.write(transcript)

    print("\n--- TRANSCRIPTION COMPLETE ---")
    print("Transcript saved as 'transcript.txt'")
    print(f"Detected Languages: {languages}")
    print("Key frames saved in './keyframes/' folder.")

# Example usage
if __name__ == "__main__":
    youtube_url = input("Enter YouTube URL: ")
    main(youtube_url)
