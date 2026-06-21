#!/usr/bin/env python3
"""
Unit tests for main module
"""

import pytest
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))


class TestMain:
    """
    Test cases for main functionality
    """
    
    def test_import_main(self):
        """
        Test if main module can be imported
        """
        try:
            from src import main
            assert main is not None
        except ImportError as e:
            pytest.fail(f"Failed to import main module: {e}")
    
    def test_config_loading(self):
        """
        Test configuration loading
        """
        from utils.config_loader import ConfigLoader
        
        config = ConfigLoader.load_config()
        assert isinstance(config, dict)
        assert "obs" in config
        assert "crosshair" in config
    
    def test_logger_setup(self):
        """
        Test logger setup
        """
        from utils.logger import setup_logger
        
        logger = setup_logger("test")
        assert logger is not None
        assert logger.name == "test"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
