import os


def _format_time(seconds: float) -> str:
    """Convert a duration in seconds to a human-readable time string.

    Args:
        seconds: The elapsed or remaining time in seconds.

    Returns:
        A formatted string in "MM:SS" or "HH:MM:SS" format.
        Returns "00:00" if seconds is None or non-positive.
    """
    if seconds is None or seconds <= 0:
        return "00:00"
    s = int(seconds)
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    if h:
        return f"{h:02d}:{m:02d}:{s:02d}"
    return f"{m:02d}:{s:02d}"


def _build_bar(frac: float, bar_width: int) -> str:
    """Build an ASCII progress bar string.

    Args:
        frac: Completion fraction between 0.0 and 1.0.
        bar_width: Total character width of the bar.

    Returns:
        A string of the form "===>   " representing current progress.
    """
    filled = int(bar_width * frac)
    if filled <= 0:
        return " " * bar_width
    if filled < bar_width:
        return "=" * (filled - 1) + ">" + " " * (bar_width - filled)
    return "=" * bar_width


def _get_cols() -> int:
    """Return the current terminal width in columns.

    Falls back to 80 columns if the terminal size cannot be determined.

    Returns:
        The number of columns available in the terminal.
    """
    try:
        return os.get_terminal_size().columns
    except Exception:
        return 80


def ft_tqdm(lst: range) -> None:
    """Display a progress bar while iterating over a range.

    A lightweight reimplementation of tqdm that prints an updating
    progress bar to the terminal, showing percentage, elapsed time,
    ETA, and iteration rate.

    Args:
        lst: The range (or any sized iterable) to iterate over.

    Yields:
        Each element from lst, one at a time.
    """
    total = None
    try:
        total = len(lst)
    except Exception:
        total = None

    start = os.times()[4]
    prev_len = 0
    for idx, elem in enumerate(lst):
        now = os.times()[4]
        elapsed = now - start
        n = idx + 1

        if total and total > 0:
            frac = n / total
            pct = int(frac * 100)
            try:
                eta = (elapsed / n) * (total - n)
            except Exception:
                eta = 0
            rate = n / elapsed if elapsed > 0 else 0
            elapsed_s = _format_time(elapsed)
            eta_s = _format_time(eta)

            left = f"{pct:3d}%|"
            right = (f"| {n}/{total}"
                     f" [{elapsed_s}<{eta_s}, {rate:.2f}it/s]")
            cols = _get_cols()
            bar_width = max(10, cols - len(left) - len(right))
            bar = _build_bar(frac, bar_width)
            stats = left + bar + right
        else:
            rate = n / elapsed if elapsed > 0 else 0
            elapsed_s = _format_time(elapsed)
            stats = f"{n} [{elapsed_s}, {rate:.2f}it/s]"

        if len(stats) < prev_len:
            stats = stats + " " * (prev_len - len(stats))
        prev_len = len(stats)

        print("\r" + stats, end="", flush=True)
        yield elem

    try:
        if total and total > 0:
            elapsed = os.times()[4] - start
            elapsed_s = _format_time(elapsed)
            rate = total / elapsed if elapsed > 0 else 0

            left = "100%|"
            right = (f"| {total}/{total}"
                     f" [{elapsed_s}<{_format_time(0)}, {rate:.2f}it/s]")
            cols = _get_cols()
            bar_width = max(10, cols - len(left) - len(right))
            bar = "=" * bar_width
            stats = left + bar + right
            if len(stats) < prev_len:
                stats = stats + " " * (prev_len - len(stats))
            print("\r" + stats)
        else:
            print()
    except Exception:
        print()
