#!/bin/sh

ffmpeg -i ~/Downloads/video.mp4 -i ~/Downloads/audio.mp4 -c:v copy -c:a aac $1
