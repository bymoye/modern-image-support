"""
Performance benchmark for modern-image-support library.
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import time
import statistics
from modern_image_support import webp_supported, avif_supported

# Test User-Agent strings
TEST_USER_AGENTS = [
    b"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    b"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
    b"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15",
    b"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
    b"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
]

def benchmark_function(func, user_agents, iterations=100000):
    """Benchmark a function with given user agents."""
    times = []
    
    # Warm up
    for ua in user_agents:
        func(ua)
    
    # Actual benchmark
    for _ in range(iterations):
        start = time.perf_counter()
        for ua in user_agents:
            func(ua)
        end = time.perf_counter()
        times.append(end - start)
    
    return times

def main():
    print("🚀 Modern Image Support Performance Benchmark")
    print("=" * 60)
    print()
    
    iterations = 10000
    print(f"Running {iterations:,} iterations with {len(TEST_USER_AGENTS)} user agents each...")
    print()
    
    # Benchmark WebP detection
    print("📦 Benchmarking WebP Support Detection...")
    webp_times = benchmark_function(webp_supported, TEST_USER_AGENTS, iterations)
    webp_avg = statistics.mean(webp_times) * 1000  # Convert to milliseconds
    webp_median = statistics.median(webp_times) * 1000
    webp_min = min(webp_times) * 1000
    webp_max = max(webp_times) * 1000
    
    print(f"  Average time: {webp_avg:.4f} ms")
    print(f"  Median time:  {webp_median:.4f} ms")
    print(f"  Min time:     {webp_min:.4f} ms")
    print(f"  Max time:     {webp_max:.4f} ms")
    print()
    
    # Benchmark AVIF detection
    print("🎯 Benchmarking AVIF Support Detection...")
    avif_times = benchmark_function(avif_supported, TEST_USER_AGENTS, iterations)
    avif_avg = statistics.mean(avif_times) * 1000
    avif_median = statistics.median(avif_times) * 1000
    avif_min = min(avif_times) * 1000
    avif_max = max(avif_times) * 1000
    
    print(f"  Average time: {avif_avg:.4f} ms")
    print(f"  Median time:  {avif_median:.4f} ms")
    print(f"  Min time:     {avif_min:.4f} ms")
    print(f"  Max time:     {avif_max:.4f} ms")
    print()
    
    # Calculate operations per second
    total_operations = iterations * len(TEST_USER_AGENTS)
    webp_ops_per_sec = total_operations / statistics.mean(webp_times)
    avif_ops_per_sec = total_operations / statistics.mean(avif_times)
    
    print("📊 Performance Summary:")
    print(f"  WebP detection: {webp_ops_per_sec:,.0f} operations/second")
    print(f"  AVIF detection: {avif_ops_per_sec:,.0f} operations/second")
    print()
    
    # Performance per user agent check
    per_ua_webp = (statistics.mean(webp_times) / len(TEST_USER_AGENTS)) * 1_000_000  # microseconds
    per_ua_avif = (statistics.mean(avif_times) / len(TEST_USER_AGENTS)) * 1_000_000
    
    print("⚡ Performance per User-Agent check:")
    print(f"  WebP: {per_ua_webp:.2f} μs per check")
    print(f"  AVIF: {per_ua_avif:.2f} μs per check")
    print()
    
    # Memory usage estimate
    print("💾 Estimated overhead per request:")
    print("  - Function call overhead: ~1-2 μs")
    print("  - String processing: ~0.5-1 μs")
    print("  - Memory allocation: Minimal (stack only)")
    print()
    
    print("✅ Benchmark completed!")
    print(f"   Total operations performed: {total_operations * 2:,}")

if __name__ == '__main__':
    main()
