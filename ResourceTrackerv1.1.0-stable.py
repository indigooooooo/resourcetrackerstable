import psutil, time, os, datetime, uuid, json

LOG_INTERVAL = 5
BASE_DIR = os.path.join(os.path.expanduser("~"), "Documents", "Resource Tracker")
CONFIG_FILE = os.path.join(BASE_DIR, "config", "config.json")
DEFAULT_PATH = os.path.join(BASE_DIR, "logs")
os.makedirs(os.path.dirname(CONFIG_FILE), exist_ok=True)
os.makedirs(DEFAULT_PATH, exist_ok=True)

def load_config():
    try:
        return json.load(open(CONFIG_FILE)).get("log_path", DEFAULT_PATH) if os.path.exists(CONFIG_FILE) else DEFAULT_PATH
    except:
        return DEFAULT_PATH

def save_config(path):
    json.dump({"log_path": path}, open(CONFIG_FILE, "w"))

LOG_PATH = load_config()
os.makedirs(LOG_PATH, exist_ok=True)
MB = 1024 * 1024

# Process selection
processes = sorted([(p.info['pid'], p.info['name']) for p in psutil.process_iter(['pid', 'name']) if p.info], key=lambda x: x[1].lower())
print(f"\n{'='*60}\nAvailable processes ({len(processes)} total):\n{'='*60}")
for pid, name in processes:
    print(f"  PID {pid:>6} │ {name}")

print(f"\n{'='*60}\nOptions:\n  1 <PID>  - Select process to log\n  2 <path> - Set log path\n{'='*60}")

while True:
    user_input = input("\nEnter command: ").strip().split(None, 1)
    if not user_input:
        continue
    if user_input[0] == "1" and len(user_input) == 2:
        try:
            proc = psutil.Process(int(user_input[1]))
            break
        except (ValueError, psutil.NoSuchProcess):
            print("Invalid PID. Try again.")
    elif user_input[0] == "2":
        new_path = user_input[1] if len(user_input) == 2 else DEFAULT_PATH
        try:
            os.makedirs(new_path, exist_ok=True)
            LOG_PATH = new_path
            save_config(LOG_PATH)
            print(f"✓ Log path set to: {LOG_PATH}")
        except:
            print("✗ Invalid path. Try again.")
    else:
        print("Invalid command. Use '1 <PID>' or '2 <path>'")

# Setup
run_id, start = uuid.uuid4().hex[:6].upper(), datetime.datetime.now()
log_file = os.path.join(LOG_PATH, f"{proc.name().replace(' ', '_')}_PID{proc.pid}_{start.strftime('%Y-%m-%d_%H-%M-%S')}_{run_id}.log")
cpu_count, last_io, last_time = psutil.cpu_count(logical=True), proc.io_counters(), time.time()
proc.cpu_percent(interval=None)  # Prime CPU

with open(log_file, "w", buffering=1) as f:
    f.write(f"Resource Log\nProcess: {proc.name()}\nPID: {proc.pid}\nRun ID: {run_id}\nStarted: {start}\nInterval: {LOG_INTERVAL}s\n{'-'*50}\n")

print(f"\n{'='*60}\nLogging: {proc.name()} (PID {proc.pid})\nFile: {log_file}\n{'='*60}\n")

# Main loop
with open(log_file, "a", buffering=1) as f:
    while True:
        time.sleep(LOG_INTERVAL)
        now = time.time()
        delta_t, last_time, io = now - last_time, now, proc.io_counters()
        read_mb_s, write_mb_s = (io.read_bytes - last_io.read_bytes) / MB / delta_t, (io.write_bytes - last_io.write_bytes) / MB / delta_t
        last_io = io
        f.write(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] CPU: {proc.cpu_percent(interval=None) / cpu_count:.2f}% | RAM: {proc.memory_info().rss / MB:.1f} MB | Read: {read_mb_s:.2f} MB/s | Write: {write_mb_s:.2f} MB/s\n")