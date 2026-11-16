# processor.py  -- FIXED VERSION

def sanitize_string(s):
    """Trim surrounding whitespace and exclamation marks from strings."""
    if not isinstance(s, str):
        return ""
    return s.strip().strip("!").strip()


def parse_int_list(s):
    """Parse valid comma-separated integers, skipping empty/invalid tokens."""
    if not isinstance(s, str):
        return []

    result = []
    for part in s.split(","):
        part = part.strip()
        if not part:
            continue
        try:
            result.append(int(part))
        except (ValueError, TypeError):
            continue
    return result


def is_palindrome(s):
    """Check whether the alphanumeric characters form a palindrome."""
    if not isinstance(s, str):
        return False
    normalized = "".join(ch.casefold() for ch in s if ch.isalnum())
    return normalized == normalized[::-1]


if __name__ == "__main__":
    print(sanitize_string("  !hello!  "))
    print(parse_int_list("1,2,3"))
    print(is_palindrome("racecar"))
