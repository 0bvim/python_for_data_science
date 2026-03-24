from typing import Any

def ft_statistics(*args: Any, **kwargs: Any) -> None:
    valid_options = ["mean", "median", "quartile", "std", "var"]

    data = list(args)
    data.sort()
    data_len = len(data)
    print(f"data_len: {data_len} - sorted data - {data}")
    print(50*'-')
    print(f"kwargs: {kwargs}")