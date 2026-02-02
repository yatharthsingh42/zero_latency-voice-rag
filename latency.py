import time
START_TIME = time.time()

def now_ms():
    """Return milliseconds since program start."""
    return int((time.time() - START_TIME) * 1000)

def log(message):
    """Human-readable log with relative timestamp."""
    print(f"[{now_ms()}ms] {message}")
