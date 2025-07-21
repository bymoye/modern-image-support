from typing import Union

def webp_supported(user_agent: Union[str, bytes]) -> bool:
    """Check if the browser supports WebP format based on User-Agent string.

    Args:
        user_agent: The User-Agent string (str or bytes)

    Returns:
        True if WebP is supported, False otherwise
    """
    ...

def avif_supported(user_agent: Union[str, bytes]) -> bool:
    """Check if the browser supports AVIF format based on User-Agent string.

    Args:
        user_agent: The User-Agent string (str or bytes)

    Returns:
        True if AVIF is supported, False otherwise
    """
    ...
