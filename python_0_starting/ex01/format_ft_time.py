import time
from datetime import datetime


def format_ft_time() -> tuple[str, str]:
    """
    Format the current time in seconds since the epoch and in scientific
     notation and return it along with the current date.

    Returns:
        tuple[str, str]: A tuple containing the formatted timestamp string
            and the current date string.
    """
    timestamp = time.time()
    timestamp_string = f"Seconds since January 1, 1970: {timestamp:,.4f} \
        or {timestamp:.2e} in scientific notation"
    date_str = datetime.now().strftime("%b %d %Y")
    return timestamp_string, date_str


if __name__ == "__main__":
    ts, ds = format_ft_time()
    print(f"{ts}\n{ds}")
