#!/usr/bin/env python3
"""
Configuration Loader Module
Handles loading and parsing configuration files
"""

import json
import logging
from pathlib import Path
from typing import Dict, Any

logger = logging.getLogger(__name__)


class ConfigLoader:
    """
    Loads and manages configuration
    """
    
    CONFIG_PATH = Path(__file__).parent.parent / "config" / "settings.json"
    
    @classmethod
    def load_config(cls) -> Dict[str, Any]:
        """
        Load configuration from file
        
        Returns:
            dict: Configuration dictionary
        """
        try:
            if not cls.CONFIG_PATH.exists():
                logger.warning(f"Config file not found: {cls.CONFIG_PATH}")
                return cls._get_default_config()
            
            with open(cls.CONFIG_PATH, 'r') as f:
                config = json.load(f)
            
            logger.info(f"Configuration loaded from {cls.CONFIG_PATH}")
            return config
        
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in config file: {e}")
            return cls._get_default_config()
        
        except Exception as e:
            logger.error(f"Error loading configuration: {e}")
            return cls._get_default_config()
    
    @staticmethod
    def _get_default_config() -> Dict[str, Any]:
        """
        Get default configuration
        
        Returns:
            dict: Default configuration
        """
        return {
            "obs": {
                "host": "localhost",
                "port": 4444,
                "password": ""
            },
            "crosshair": {
                "style": "dot",
                "color": "#00FF00",
                "size": 20
            },
            "tracking": {
                "enabled": True,
                "sensitivity": 1.0
            }
        }
