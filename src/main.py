#!/usr/bin/env python3
"""
MY_Obs - OBS Aiming Assist Tool
Main entry point for the application
"""

import sys
import logging
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.logger import setup_logger
from utils.config_loader import ConfigLoader

# Setup logging
logger = setup_logger(__name__)


def main():
    """
    Main application entry point
    """
    try:
        logger.info("Starting MY_Obs Aiming Assist Tool...")
        
        # Load configuration
        config = ConfigLoader.load_config()
        logger.info(f"Configuration loaded successfully")
        logger.debug(f"Config: {config}")
        
        # TODO: Initialize OBS connection
        # TODO: Initialize aim tracking
        # TODO: Start UI
        
        logger.info("Application initialized successfully")
        
    except Exception as e:
        logger.error(f"Failed to start application: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
