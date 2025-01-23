from pathlib import Path
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import os


def on_modified(event):
    script_path = os.path.join(os.path.dirname(__file__), 'RunScript.vbs')
    subprocess.Popen(["wscript.exe", script_path], creationflags=subprocess.CREATE_NO_WINDOW)


def on_moved(event):
    script_path = os.path.join(os.path.dirname(__file__), 'RunScript.vbs')
    subprocess.Popen(["wscript.exe", script_path], creationflags=subprocess.CREATE_NO_WINDOW)

if __name__ == "__main__":
    event_handler = FileSystemEventHandler()

    event_handler.on_modified = on_modified
    event_handler.on_moved = on_moved

    path = str(Path.home() / "Downloads") + "\\"
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()
