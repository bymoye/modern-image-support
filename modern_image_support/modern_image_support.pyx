# modern_image_support.pyx
cimport cython

cdef extern from "modern_image_support_c.h":
    bint is_webp_supported(const char *user_agent)
    bint is_avif_supported(const char *user_agent)

@cython.boundscheck(False)
@cython.wraparound(False)
cpdef bint webp_supported(user_agent):
    """Check if the browser supports WebP format based on User-Agent string.
    
    Args:
        user_agent (str or bytes): The User-Agent string
        
    Returns:
        bool: True if WebP is supported, False otherwise
    """
    cdef bytes ua_bytes
    if isinstance(user_agent, str):
        ua_bytes = user_agent.encode('utf-8')
    else:
        ua_bytes = user_agent
    return is_webp_supported(ua_bytes)

@cython.boundscheck(False)
@cython.wraparound(False)
cpdef bint avif_supported(user_agent):
    """Check if the browser supports AVIF format based on User-Agent string.
    
    Args:
        user_agent (str or bytes): The User-Agent string
        
    Returns:
        bool: True if AVIF is supported, False otherwise
    """
    cdef bytes ua_bytes
    if isinstance(user_agent, str):
        ua_bytes = user_agent.encode('utf-8')
    else:
        ua_bytes = user_agent
    return is_avif_supported(ua_bytes)