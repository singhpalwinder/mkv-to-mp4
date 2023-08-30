#!/usr/bin/env python3
import time
import subprocess
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

path = ''

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            return  # Skip processing if the event is not for a directory

        for filename in os.listdir(event.src_path):
            if filename == ".DS_Store":
                continue  # Skip processing .DS_Store file
            if filename.endswith(".mkv"):
                # Convert .mkv to .mp4
                filepath = os.path.join(event.src_path, filename)
                new_filepath = os.path.splitext(filepath)[0] + '.mp4'
                subprocess.run(["ffmpeg", "-i", filepath, "-vcodec",
                               "copy", "-acodec", "copy", new_filepath])

                # Delete the original .mkv file
                os.remove(filepath)


if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(
        event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
