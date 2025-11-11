def string_to_bool(value: str) -> bool:
    if not isinstance(value, str):
        raise ValueError("Input must be a string")
    return value.strip().lower() in ("yes", "true", "1", "y", "on")
    