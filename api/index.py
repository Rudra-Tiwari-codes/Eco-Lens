#!/usr/bin/env python3
"""
Vercel serverless function entry point for EcoLens
"""

import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from ecolens.main import app

# Export the FastAPI app for Vercel
handler = app
