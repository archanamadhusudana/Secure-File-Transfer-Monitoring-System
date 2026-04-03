
import time
import hashlib
import logging
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# ── SETTINGS ──────────────────────────────
WATCH_FOLDER = "C:\\SecureFiles"
SENSITIVE_EXTENSIONS = ['.pdf', '.docx', '.xlsx', '.txt']
AUTHORIZED_USERS = ["lenovo", "admin"]
LOG_FILE = "file_monitor.log"
# ──────────────────────────────────────────

# Setup logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

def get_file_hash(filepath):
    sha256 = hashlib.sha256()
    try:
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256.update(chunk)
        return sha256.hexdigest()
    except:
        return "Unable to hash"

def is_sensitive(filepath):
    return any(filepath.endswith(ext) for ext in SENSITIVE_EXTENSIONS)

def log_and_alert(message, alert=False):
    print(message)
    if alert:
        logging.warning(message)
    else:
        logging.info(message)

class SecureFileHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.is_directory:
            return

        filepath = event.src_path
        event_type = event.event_type

        if is_sensitive(filepath):
            file_hash = get_file_hash(filepath)
            message = (
                f"[{event_type.upper()}] Sensitive file detected!\n"
                f"  File    : {filepath}\n"
                f"  Hash    : {file_hash}\n"
                f"  Time    : {datetime.now()}\n"
            )
            log_and_alert(message, alert=True)
        else:
            message = f"[{event_type.upper()}] File: {filepath}"
            log_and_alert(message)

# ── START MONITORING ──
print(f"Monitoring started on: {WATCH_FOLDER}")
print("Press Ctrl+C to stop\n")

observer = Observer()
observer.schedule(SecureFileHandler(), path=WATCH_FOLDER, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
    print("\nMonitoring stopped.")

observer.join()