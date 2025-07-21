"""
FastAPI web server example using modern-image-support.
"""
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, HTMLResponse
from modern_image_support import webp_supported, avif_supported
import os

app = FastAPI(title="Modern Image Support Demo", version="1.0.0")

# Assume we have these image files
IMAGE_FILES = {
    'avif': 'static/sample.avif',
    'webp': 'static/sample.webp',
    'jpeg': 'static/sample.jpg'
}

@app.get("/image")
async def serve_optimized_image(request: Request):
    """Serve the best supported image format based on user agent."""
    user_agent = request.headers.get('user-agent', '').encode('utf-8')
    
    # Choose the best format
    if avif_supported(user_agent):
        format_choice = 'avif'
        media_type = 'image/avif'
    elif webp_supported(user_agent):
        format_choice = 'webp'
        media_type = 'image/webp'
    else:
        format_choice = 'jpeg'
        media_type = 'image/jpeg'
    
    # In a real application, check if file exists
    image_path = IMAGE_FILES[format_choice]
    
    print(f"Serving {format_choice.upper()} format for user agent: {user_agent.decode('utf-8')[:50]}...")
    
    # Return the appropriate image
    if os.path.exists(image_path):
        return FileResponse(image_path, media_type=media_type)
    else:
        return {"message": f"Would serve: {image_path} with media_type: {media_type}"}

@app.get("/", response_class=HTMLResponse)
async def index():
    """Simple index page with image."""
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Modern Image Support Demo - FastAPI</title>
    </head>
    <body>
        <h1>Modern Image Support Demo (FastAPI)</h1>
        <p>This server automatically serves the best image format your browser supports.</p>
        <img src="/image" alt="Optimized image" style="max-width: 500px;">
        <p>Check the network tab to see which format was served!</p>
        <p><a href="/docs">View API Documentation</a></p>
    </body>
    </html>
    '''

@app.get("/api/check-support")
async def check_support(request: Request):
    """API endpoint to check format support."""
    user_agent = request.headers.get('user-agent', '').encode('utf-8')
    
    return {
        "user_agent": user_agent.decode('utf-8'),
        "webp_supported": webp_supported(user_agent),
        "avif_supported": avif_supported(user_agent),
        "recommended_format": (
            "avif" if avif_supported(user_agent) 
            else "webp" if webp_supported(user_agent) 
            else "jpeg"
        )
    }

if __name__ == '__main__':
    import uvicorn
    print("Starting FastAPI server with modern image support...")
    print("Visit http://localhost:8000 to test!")
    print("API docs available at http://localhost:8000/docs")
    uvicorn.run(app, host="0.0.0.0", port=8000)
