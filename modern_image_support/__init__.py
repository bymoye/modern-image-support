"""Modern Image Support - WebP and AVIF detection from User-Agent strings.

This package provides fast, efficient detection of WebP and AVIF image format
support based on browser User-Agent strings.
"""

__version__ = "0.4.0"
__author__ = "bymoye"
__email__ = "s3moye@gmail.com"

from .modern_image_support import webp_supported, avif_supported

# 保留向后兼容的别名
is_webp_supported = webp_supported
is_avif_supported = avif_supported

__all__ = ["webp_supported", "avif_supported", "is_webp_supported", "is_avif_supported"]