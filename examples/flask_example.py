"""
Flask web server example using modern-image-support.
"""
from flask import Flask, request, send_file
from modern_image_support import webp_supported, avif_supported
import os

app = Flask(__name__)

# Assume we have these image files
IMAGE_FILES = {
    'avif': 'static/sample.avif',
    'webp': 'static/sample.webp',
    'jpeg': 'static/sample.jpg'
}

@app.route('/image')
def serve_optimized_image():
    """Serve the best supported image format based on user agent."""
    user_agent = request.headers.get('User-Agent', '').encode('utf-8')
    
    # Choose the best format
    if avif_supported(user_agent):
        format_choice = 'avif'
        mimetype = 'image/avif'
    elif webp_supported(user_agent):
        format_choice = 'webp'
        mimetype = 'image/webp'
    else:
        format_choice = 'jpeg'
        mimetype = 'image/jpeg'
    
    # In a real application, check if file exists
    image_path = IMAGE_FILES[format_choice]
    
    print(f"Serving {format_choice.upper()} format for user agent: {user_agent.decode('utf-8')[:50]}...")
    
    # Return the appropriate image
    if os.path.exists(image_path):
        return send_file(image_path, mimetype=mimetype)
    else:
        return f"Would serve: {image_path} with mimetype: {mimetype}", 200

@app.route('/')
def index():
    """Simple index page with image."""
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Modern Image Support Demo</title>
    </head>
    <body>
        <h1>Modern Image Support Demo</h1>
        <p>This server automatically serves the best image format your browser supports.</p>
        <img src="/image" alt="Optimized image" style="max-width: 500px;">
        <p>Check the network tab to see which format was served!</p>
    </body>
    </html>
    '''

if __name__ == '__main__':
    print("Starting Flask server with modern image support...")
    print("Visit http://localhost:5000 to test!")
    app.run(debug=True)
