#!/usr/bin/env python3
"""
Simple test script to verify WebP and AVIF support detection.
"""

def test_library():
    # Test User-Agent strings
    test_cases = [
        # Chrome 91 - supports both WebP and AVIF
        (b"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36", True, True),
        
        # Firefox 89 - supports WebP but not AVIF  
        (b"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0", True, False),
        
        # Firefox 93 - supports both WebP and AVIF
        (b"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0", True, True),
        
        # Safari 16 - supports both WebP and AVIF
        (b"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/612.1.29 (KHTML, like Gecko) Version/16.0 Safari/612.1.29", True, True),
        
        # Old Chrome 30 - supports neither
        (b"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36", False, False),
        
        # Edge 85 - supports both WebP and AVIF
        (b"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36 Edge/85.0.564.51", True, True),
    ]
    
    try:
        import sys
        import os
        sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from modern_image_support import webp_supported, avif_supported
        
        print("Testing WebP and AVIF support detection...")
        print("=" * 60)
        
        all_passed = True
        
        for i, (ua, expected_webp, expected_avif) in enumerate(test_cases, 1):
            webp_result = webp_supported(ua)
            avif_result = avif_supported(ua)
            
            webp_status = "✓" if webp_result == expected_webp else "✗"
            avif_status = "✓" if avif_result == expected_avif else "✗"
            
            if webp_result != expected_webp or avif_result != expected_avif:
                all_passed = False
            
            # Extract browser name for display
            ua_str = ua.decode('utf-8')
            if 'Chrome' in ua_str and 'Edge' not in ua_str:
                browser = f"Chrome {ua_str.split('Chrome/')[1].split()[0]}"
            elif 'Firefox' in ua_str:
                browser = f"Firefox {ua_str.split('Firefox/')[1].split()[0]}"
            elif 'Safari' in ua_str and 'Chrome' not in ua_str:
                browser = f"Safari {ua_str.split('Version/')[1].split()[0]}"
            elif 'Edge' in ua_str:
                browser = f"Edge {ua_str.split('Edge/')[1].split()[0]}"
            else:
                browser = "Unknown browser"
            
            print(f"Test {i}: {browser}")
            print(f"  WebP: {webp_status} Expected: {expected_webp}, Got: {webp_result}")
            print(f"  AVIF: {avif_status} Expected: {expected_avif}, Got: {avif_result}")
            print()
        
        if all_passed:
            print("🎉 All tests passed!")
            return True
        else:
            print("❌ Some tests failed!")
            return False
            
    except ImportError as e:
        print(f"Import error: {e}")
        print("Make sure to build the extension first:")
        print("  python setup.py build_ext --inplace")
        return False
    except Exception as e:
        print(f"Test error: {e}")
        return False

if __name__ == "__main__":
    test_library()
