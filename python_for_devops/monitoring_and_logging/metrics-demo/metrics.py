import statsd


def get_prefix():
    return "demo.app"


def Counter(name, suffix=None):
    if suffix:
        name_parts = name.split('.')
        name_parts.append(suffix)
        name = '.'.join(name_parts)
    return statsd.Counter(f"{get_prefix()}.{name}")
