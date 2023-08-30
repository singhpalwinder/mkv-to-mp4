## MKV-to-MP4 Converter

This Python script watches a directory for changes and automatically converts MKV video files to MP4 format using FFmpeg. It utilizes the `watchdog` library to monitor the directory for modifications and triggers the conversion process on file modification. The converted files are saved as MP4 files, and the original MKV files are deleted after conversion.

### Requirements

- Python 3
- FFmpeg
- `watchdog` library

### Usage

1. Make sure you have Python 3 and FFmpeg installed on your system.
2. Install the required `watchdog` library by running: `pip install watchdog`
3. Set the `path` variable in the script to the directory you want to monitor.
4. Run the script: `python3 script.py`

### Details

The script listens for modifications in the specified directory and, upon detecting an MKV file, uses FFmpeg to convert it to an MP4 file while retaining the video and audio codecs. The original MKV file is then deleted.

---
