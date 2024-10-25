# YouTube Video Downloader

A straightforward Python tool to download YouTube videos directly by pasting the video URL. Say goodbye to annoying redirects and hello to hassle-free downloads!

## 🚀 Features

- **Simple Interface:** Just enter the YouTube video URL.
- **Direct Downloads:** Bypass the hassle of multiple redirects.
- **Fast & Efficient:** Get your videos downloaded quickly!

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Rajneeshkarya/YT2MP4.git
   ```
2. Navigate to Project Directory
   ```bash
   cd YT2MP4
   
4. Install Dependencies
   ```bash
   pip3 install -r requirements.txt
   ```
5. Make the python file executable
   ```bash
   chmod +x yt2mp4.py
   ```

## 💻 Usage

1. Run the tool with the following command:
   ```bash
   ./yt2mp4.py -u <YouTube URL> -q <quality> -d <destination>
   ```
   
## Example Commands

1. Download a video with the best quality:
   ```bash
   ./yt2mp4.py -u https://www.youtube.com/watch?v=S6qWYpBkNvE -q best
   ```
2. Download a video to a specific folder:
   ```bash
   ./yt2mp4.py -u https://www.youtube.com/watch?v=S6qWYpBkNvE -d /path/to/destination
   ```
3. Download a video with a custom filename:
   ```bash
   ./yt2mp4.py -u https://www.youtube.com/watch?v=S6qWYpBkNvE -f myvideo.mp4
   ```

## 📜 requirements.txt

Make sure to check the requirements.txt file for all necessary packages to run the tool. You can add or modify dependencies as needed.

## 🤝 Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or submit a pull request.
   
## 🙌 Acknowledgments

This tool was built by Rajneesh Kumar Arya. Special thanks to everyone who inspired and supported this project!
