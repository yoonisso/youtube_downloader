import PySimpleGUI as sg
import re
import os
from pytube import YouTube

output_path = f"{os.environ['HOME']}/Desktop"

def download_mp4(youtube_object):
    try:
        video_stream = youtube_object.streams.get_highest_resolution()
        video_stream.download(output_path)
        print("Download completed successfully")
    except Exception as e:
        print(f"An error has occurred: {e}")

def download_mp3(youtube_object):
    try:
        audio_stream = youtube_object.streams.filter(only_audio=True).first()
        audio_stream.download(output_path)
        print("Download completed successfully")
    except Exception as e:
        print(f"An error has occurred: {e}")

# building window
layout = [
            [sg.Text('Enter Youtube video link'), sg.InputText()],
            [sg.Radio("MP3", "file_type", default=True, key="mp3")],
            [sg.Radio("MP4", "file_type", key="mp4")],
            [sg.Button('Download'), sg.Button('Cancel')]
        ]
window = sg.Window('youtube downloader', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if re.search(r'\byoutube.com\b', values[0]) or re.search(r'\byoutu.be\b', values[0]):
        video_url = values[0]

        if values["mp3"]:
            download_mp3(YouTube(video_url))
        elif values["mp4"]:
            download_mp4(YouTube(video_url))
        sg.popup('You downloaded a video')
    else:
        sg.popup('This is not a Youtube link, please try again')
window.close()