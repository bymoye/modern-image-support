"""
Django view example using modern-image-support.
"""
from django.http import HttpResponse, FileResponse, JsonResponse
from django.shortcuts import render
from modern_image_support import webp_supported, avif_supported
import os

# Assume we have these image files
IMAGE_FILES = {
    'avif': 'static/sample.avif',
    'webp': 'static/sample.webp',
    'jpeg': 'static/sample.jpg'
}

def serve_optimized_image(request):
    """Serve the best supported image format based on user agent."""
    user_agent = request.META.get('HTTP_USER_AGENT', '').encode('utf-8')
    
    # Choose the best format
    if avif_supported(user_agent):
        format_choice = 'avif'
        content_type = 'image/avif'
    elif webp_supported(user_agent):
        format_choice = 'webp'
        content_type = 'image/webp'
    else:
        format_choice = 'jpeg'
        content_type = 'image/jpeg'
    
    # In a real application, check if file exists
    image_path = IMAGE_FILES[format_choice]
    
    print(f"Serving {format_choice.upper()} format for user agent: {user_agent.decode('utf-8')[:50]}...")
    
    # Return the appropriate image
    if os.path.exists(image_path):
        return FileResponse(open(image_path, 'rb'), content_type=content_type)
    else:
        return HttpResponse(f"Would serve: {image_path} with content_type: {content_type}")

def index(request):
    """Simple index page with image."""
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Modern Image Support Demo - Django</title>
    </head>
    <body>
        <h1>Modern Image Support Demo (Django)</h1>
        <p>This server automatically serves the best image format your browser supports.</p>
        <img src="/image" alt="Optimized image" style="max-width: 500px;">
        <p>Check the network tab to see which format was served!</p>
    </body>
    </html>
    '''
    return HttpResponse(html)

def check_support_api(request):
    """API endpoint to check format support."""
    user_agent = request.META.get('HTTP_USER_AGENT', '').encode('utf-8')
    
    return JsonResponse({
        "user_agent": user_agent.decode('utf-8'),
        "webp_supported": webp_supported(user_agent),
        "avif_supported": avif_supported(user_agent),
        "recommended_format": (
            "avif" if avif_supported(user_agent) 
            else "webp" if webp_supported(user_agent) 
            else "jpeg"
        )
    })

# Example URLs configuration (add to your urls.py):
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('image/', views.serve_optimized_image, name='serve_image'),
    path('api/check-support/', views.check_support_api, name='check_support'),
]
"""
