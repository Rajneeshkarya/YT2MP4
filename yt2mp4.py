#!/usr/bin/env python3

# YT2MP4: A Python Tool for Direct YouTube Video Downloads
# Project Purpose:
#     YT2MP4 was created to provide a straightforward, efficient alternative to online websites for downloading YouTube videos,
#     helping users avoid intrusive ads, redirects, and privacy concerns associated with third-party download services.
#
# Key Features:
#     - Directly download YouTube videos in MP4 format using a command-line interface
#     - Customize download quality (e.g., "best" or "worst")
#     - Specify a destination folder for downloaded videos
#
# Built by Rajneesh Kumar Arya
#
# Usage:
#     ./yt2mp4.py -u <YouTube URL> -q <quality> -d <destination>
# 
# Example:
#     ./yt2mp4.py -u https://www.youtube.com/watch?v=S6qWYpBkNvE -q best -d /path/to/destination




import argparse
import textwrap
import os
import re
import sys
import yt_dlp
from tqdm import tqdm

class Yt2mp4:
    def __init__(self, args):
        self.args = args
        self.ydl_opts = {
            'format': 'best',
            'progress_hooks': []
        }
    
    # Check the URL is valid or not
    def checkURL(self, url):
        pattern = r"^https:\/\/www\.youtube\.com\/watch\?v=[\w-]{11}$"
        if re.match(pattern, url):
            return True
        else:
            return False
        

    # Handling the Directory Creation
    def createDir(self, path):
        try:
            if not os.path.exists(path):
                os.makedirs(path)
            # Set output template to include a file name
            if self.args.filename:
                self.ydl_opts['outtmpl'] = os.path.join(path, self.args.filename)
            else:
                self.ydl_opts['outtmpl'] = os.path.join(path, '%(title)s.%(ext)s')
        except Exception as e:
            print(f"[-] Error while creating/accessing Directory : {e}")
        

    # Main Downloading Logic
    def download_video(self):
        try:
            progress_bar = tqdm(unit='B', unit_scale=True, desc="Downloading")

            def progress_hook(d):
                if d['status'] == 'downloading':
                    progress_bar.total = int(d.get('total_bytes', 0))
                    progress_bar.update(int(d.get('downloaded_bytes', 0)) - progress_bar.n)    
                elif d['status'] == 'finished':
                    progress_bar.close()
                    print("\nDownloading completed successfully!!!")

            self.ydl_opts['progress_hooks'].append(progress_hook)

            with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
                ydl.download([self.args.url])
        except Exception as e:
            print("[-] An Error Occured.", e)

    # Run Method to manage the working or Argument separately
    def run(self):
        if self.checkURL(self.args.url):
            if self.args.destination:
                self.createDir(self.args.destination)
            if self.args.quality:
                if self.args.quality in ['best', 'worst']:
                    self.ydl_opts['format'] = self.args.quality
                else:
                    print(f"[-] Invalid Argument {self.args.quality} in --quality/-q")
                    sys.exit()
            
            self.download_video()
        else:
            print("[-] Invalid URL")
            sys.exit()
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="YT to MP4 Converter",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''
        Examples:
                               
        ./yt2mp4.py -u https://www.youtube.com/watch?v=S6qWYpBkNvE
        ./yt2mp4.py -u https://www.youtube.com/watch?v=S6qWYpBkNvE -d /home/kairaj5456/Desktop
        ./yt2mp4.py -u https://www.youtube.com/watch?v=S6qWYpBkNvE -q best
        ./yt2mp4.py -u https://www.youtube.com/watch?v=S6qWYpBkNvE -d /home/kairaj5456/Desktop -f myvideo.mp4
        ''')
    )

    parser.add_argument('-u', '--url', help="Specify the URL", required=True)
    parser.add_argument('-d', '--destination', help="Specify the Destination Folder")
    parser.add_argument('-q', '--quality', help="Specify the Quality (best, worst)")
    parser.add_argument('-f', '--filename', help="Specify the Output File Name (optional)")

    args = parser.parse_args()

    yt = Yt2mp4(args)

    yt.run()


    


