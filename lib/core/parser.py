import re

def parse_custom_time(time_str: str):
    """Parst ein benutzerdefiniertes Zeitformat in Sekunden."""
    
    pattern = re.compile(r"(?:(\d+)y)?(?:(\d+)m)?(?:(\d+)w)?(?:(\d+)d)?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?(?:(\d+)s)?$")
    match = pattern.fullmatch(time_str)

    if not match:
        return None

    factors = [31536000, 2628000, 604800, 86400, 3600, 60, 1, 0.1]
    
    total_seconds = sum(int(value) * factor for value, factor in zip(match.groups(default="0"), factors))
    return total_seconds
