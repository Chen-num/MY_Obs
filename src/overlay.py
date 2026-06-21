#!/usr/bin/env python3
"""
Overlay Module
Handles crosshair rendering and display
"""

import logging
from typing import Tuple
from enum import Enum

logger = logging.getLogger(__name__)


class CrosshairStyle(Enum):
    """
    Supported crosshair styles
    """
    DOT = "dot"
    CIRCLE = "circle"
    CROSS = "cross"
    RETICLE = "reticle"


class Overlay:
    """
    Manages crosshair overlay rendering
    """
    
    def __init__(self, style: str = "dot", color: str = "#00FF00", size: int = 20):
        """
        Initialize Overlay
        
        Args:
            style: Crosshair style
            color: Crosshair color (hex format)
            size: Crosshair size in pixels
        """
        self.style = CrosshairStyle(style.lower())
        self.color = color
        self.size = size
        self.position = (0, 0)
        self.visible = True
    
    def set_position(self, position: Tuple[int, int]):
        """
        Set crosshair position
        
        Args:
            position: Position (x, y)
        """
        self.position = position
    
    def show(self):
        """
        Show crosshair overlay
        """
        self.visible = True
        logger.debug("Overlay shown")
    
    def hide(self):
        """
        Hide crosshair overlay
        """
        self.visible = False
        logger.debug("Overlay hidden")
    
    def render(self):
        """
        Render crosshair
        TODO: Implement actual rendering logic
        """
        if not self.visible:
            return
        
        logger.debug(f"Rendering {self.style.value} crosshair at {self.position}")
    
    def update_style(self, style: str):
        """
        Update crosshair style
        
        Args:
            style: New style name
        """
        self.style = CrosshairStyle(style.lower())
        logger.info(f"Crosshair style updated to {style}")
