#!/usr/bin/env python3
"""
Example usage of modern-image-support library.
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modern_image_support import webp_supported, avif_supported

# Example User-Agent strings for testing
test_user_agents = [
    # Modern browsers with full support
    b"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    
    # Firefox with WebP and AVIF support
    b"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
    
    # Safari with both formats
    b"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15",
    
    # Edge with support
    b"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
    
    # Older Firefox without AVIF
    b"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
    
    # Very old Chrome without WebP
    b"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/25.0.1364.172 Safari/537.36",
]

def demo_usage():
    print("🖼️  Modern Image Support Demo")
    print("=" * 50)
    print()
    
    for i, ua in enumerate(test_user_agents, 1):
        # Detect browser name for display
        ua_str = ua.decode('utf-8')
        if 'Chrome' in ua_str and 'Edg' not in ua_str and 'Edge' not in ua_str:
            if 'Chrome/' in ua_str:
                version = ua_str.split('Chrome/')[1].split()[0]
                browser = f"Chrome {version}"
            else:
                browser = "Chrome (unknown version)"
        elif 'Firefox' in ua_str:
            if 'Firefox/' in ua_str:
                version = ua_str.split('Firefox/')[1].split()[0]
                browser = f"Firefox {version}"
            else:
                browser = "Firefox (unknown version)"
        elif 'Safari' in ua_str and 'Chrome' not in ua_str:
            if 'Version/' in ua_str:
                version = ua_str.split('Version/')[1].split()[0]
                browser = f"Safari {version}"
            else:
                browser = "Safari (unknown version)"
        elif 'Edg/' in ua_str:
            version = ua_str.split('Edg/')[1].split()[0]
            browser = f"Edge {version}"
        else:
            browser = "Unknown browser"
        
        # Check support
        webp_support = webp_supported(ua)
        avif_support = avif_supported(ua)
        
        # Display results
        print(f"Browser {i}: {browser}")
        print(f"  WebP: {'✅ Supported' if webp_support else '❌ Not supported'}")
        print(f"  AVIF: {'✅ Supported' if avif_support else '❌ Not supported'}")
        
        # Recommendation
        if avif_support:
            recommendation = "🎯 Serve AVIF for best compression"
        elif webp_support:
            recommendation = "📦 Serve WebP for good compression"
        else:
            recommendation = "📷 Use JPEG/PNG fallback"
        
        print(f"  Recommendation: {recommendation}")
        print()

def web_server_example():
    """Example of how to use in a web server context."""
    print("🌐 Web Server Integration Example")
    print("=" * 40)
    print()
    
    # Simulate a request
    user_agent = b"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    
    print("Incoming request User-Agent:")
    print(f"  {user_agent.decode('utf-8')}")
    print()
    
    # Choose best format
    if avif_supported(user_agent):
        image_format = "AVIF"
        mime_type = "image/avif"
        estimated_size = "~15KB"
    elif webp_supported(user_agent):
        image_format = "WebP"
        mime_type = "image/webp"
        estimated_size = "~25KB"
    else:
        image_format = "JPEG"
        mime_type = "image/jpeg"
        estimated_size = "~50KB"
    
    print("Server decision:")
    print(f"  Format: {image_format}")
    print(f"  MIME Type: {mime_type}")
    print(f"  Estimated Size: {estimated_size}")
    print(f"  File: image.{image_format.lower()}")

if __name__ == "__main__":
    demo_usage()
    print()
    web_server_example()
