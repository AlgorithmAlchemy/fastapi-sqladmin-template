import subprocess
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path
import time

WATCH_DIRS = ["./"]


class ReloadHandler(FileSystemEventHandler):
    def __init__(self):
        self.process = None
        self.start_server()

    def start_server(self):
        print("start Uvicorn...")
        self.process = subprocess.Popen([sys.executable, "-m", "uvicorn", "main:app"])

    def stop_server(self):
        if self.process:
            print("Restarting the server...")
            self.process.terminate()
            self.process.wait()

    def restart_server(self):
        self.stop_server()
        self.start_server()

    def on_any_event(self, event):
        if event.src_path.endswith(".py"):
            self.restart_server()


if __name__ == "__main__":
    event_handler = ReloadHandler()
    observer = Observer()

    for watch_dir in WATCH_DIRS:
        observer.schedule(event_handler, path=watch_dir, recursive=True)

    observer.start()
    print("Watchdog keeps an eye on files...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nExits...")
        event_handler.stop_server()
        observer.stop()
    observer.join()
