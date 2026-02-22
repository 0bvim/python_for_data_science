import time
from datetime import datetime

from Utils import Utils


def format_ft_time() -> tuple[str, str]:
    timestamp = time.time()
    timestamp_string = f"Seconds since January 1, 1970: {timestamp:,.4f} or {timestamp:.2e} in scientific notation"
    date_str = datetime.now().strftime("%b %d %Y")
    return timestamp_string, date_str


if __name__ == "__main__":
    Utils().check_version()
    ts, ds = format_ft_time()
    print(f"{ts}\n{ds}")
