#!/usr/bin/env python

import os
import subprocess

# Check if FFmpeg is installed
if subprocess.call(["ffmpeg", "-version"]) != 0:
    print("FFmpeg is not installed. Please install it before running this script.")
    exit(1)

# Check if the input file is provided as a command-line argument
import sys

if len(sys.argv) != 2:
    print("Usage: {} input.txt".format(sys.argv[0]))
    exit(1)

input_file = sys.argv[1]

# Initialize variables to store video, audio, and title
video_url = ""
audio_url = ""
title = ""

# Process the input file
with open(input_file, 'r') as f:
    for line in f:
        line = line.strip()
        if not video_url:
            video_url = line
        elif not audio_url:
            audio_url = line
        elif not title:
            title = line
        else:
            # Download the video and audio files
            os.system('wget "{}" -O "{}_video.mp4"'.format(video_url, title))
            os.system('wget "{}" -O "{}_audio.mp3"'.format(audio_url, title))

            # Merge video and audio using FFmpeg
            os.system('ffmpeg -i "{}_video.mp4" -i "{}_audio.mp3" -c:v copy -c:a aac -strict experimental "{}.mp4"'.format(title, title, title))

            # Clean up the temporary video and audio files
            os.remove('{}_video.mp4'.format(title))
            os.remove('{}_audio.mp3'.format(title))

            print("Merged and saved as {}.mp4".format(title))

            # Reset variables for the next set
            video_url = ""
            audio_url = ""
            title = ""

# Merge the last set if title is not empty
if title:
    os.system('wget "{}" -O "{}_video.mp4"'.format(video_url, title))
    os.system('wget "{}" -O "{}_audio.mp3"'.format(audio_url, title))
    os.system('ffmpeg -i "{}_video.mp4" -i "{}_audio.mp3" -c:v copy -c:a aac -strict experimental "{}.mp4"'.format(title, title, title))

    # Clean up the temporary video and audio files
    os.remove('{}_video.mp4'.format(title))
    os.remove('{}_audio.mp3'.format(title))

    print("Merged and saved as {}.mp4".format(title))

