import re

from format_ft_time import format_ft_time


def test_regex_format() -> None:
    ts_str, _ = format_ft_time()
    # Matches "Seconds since... " followed by digits, commas, and a period
    pattern = r"Seconds since January 1, 1970: [\d,]+\.\d{4}"
    assert (re.search(pattern, ts_str))
    print("✅ success")


if __name__ == "__main__":
    test_regex_format()
