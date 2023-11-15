import subprocess
import argparse

# Function to download and rename videos
def download_and_rename_videos(input_file):
    with open(input_file, 'r') as file:
        lines = file.read().splitlines()
        video_urls = []
        titles = []
        set_started = False

        for line in lines:
            if not line:
                if set_started:
                    set_started = False
                    for i in range(len(video_urls)):
                        subprocess.run(['wget', video_urls[i], '-O', f'{titles[i]}.mp4'])
                    video_urls = []
                    titles = []
            else:
                set_started = True
                if len(video_urls) % 2 == 0:
                    video_urls.append(line)
                else:
                    titles.append(line)

def main():
    parser = argparse.ArgumentParser(description="Download and rename videos from a text file with multiple sets.")
    parser.add_argument("input_file", help="Path to the input text file containing video URL sets")
    args = parser.parse_args()

    download_and_rename_videos(args.input_file)

if __name__ == "__main__":
    main()

