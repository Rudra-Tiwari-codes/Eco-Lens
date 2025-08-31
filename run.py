#!/usr/bin/env python3
"""
EcoLens - AI-powered Sustainability Lifecycle Tracker
Main entry point for running the application
"""

import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from ecolens.main import app

# For Vercel deployment
app.debug = False

if __name__ == "__main__":
    import uvicorn
    print("Starting EcoLens API Server...")
    print("Web interface: http://127.0.0.1:8000")
    uvicorn.run(app, host="127.0.0.1", port=8000)
