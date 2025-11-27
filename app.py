from flask import Flask
from datetime import timedelta
from config import get_config
from routes import register_routes
from error_handlers import register_error_handlers

def create_app(config=None):
    """Application factory"""
    app = Flask(__name__)
    
    # Load configuration
    if config is None:
        config = get_config()
    app.config.from_object(config)
    
    # Configure caching headers for static files
    @app.after_request
    def set_cache_headers(response):
        """Set cache headers based on content type"""
        if response.content_type and response.content_type.startswith('text/html'):
            # Cache HTML for 1 hour
            response.cache_control.max_age = 3600
            response.cache_control.public = True
        elif response.content_type and any(ct in response.content_type for ct in ['css', 'javascript', 'font', 'image']):
            # Cache static assets for 30 days
            response.cache_control.max_age = 2592000
            response.cache_control.public = True
        return response
    
    # Register routes and error handlers
    register_routes(app)
    register_error_handlers(app)
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run()
