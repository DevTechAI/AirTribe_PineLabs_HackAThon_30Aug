#!/usr/bin/env python3
"""
Pine Labs Integration Assistant - Startup Script
"""

import os
import sys
from app import create_app

def main():
    """Main entry point for the application"""
    app = create_app()
    
    # Get port from environment or use default
    port = int(os.environ.get('PORT', 5000))
    
    print("🚀 Starting Pine Labs Integration Assistant...")
    print(f"📡 Server will run on http://localhost:{port}")
    print("🎯 Open your browser and navigate to the URL above")
    
    # Run the application
    app.run(
        host='0.0.0.0',
        port=port,
        debug=os.environ.get('FLASK_ENV') == 'development'
    )

if __name__ == '__main__':
    main()