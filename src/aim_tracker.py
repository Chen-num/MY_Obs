#!/usr/bin/env python3
"""
Aim Tracker Module
Core functionality for tracking and assisting aim
"""

import logging
from typing import Tuple, Optional
import numpy as np

logger = logging.getLogger(__name__)


class AimTracker:
    """
    Handles aim tracking and assistance
    """
    
    def __init__(self, sensitivity: float = 1.0, smoothing: float = 0.7):
        """
        Initialize Aim Tracker
        
        Args:
            sensitivity: Tracking sensitivity multiplier
            smoothing: Smoothing factor for movement
        """
        self.sensitivity = sensitivity
        self.smoothing = smoothing
        self.target_position = None
        self.crosshair_position = (0, 0)
        self.is_tracking = False
    
    def update_target(self, position: Tuple[int, int]):
        """
        Update target position
        
        Args:
            position: Target position (x, y)
        """
        self.target_position = position
    
    def calculate_aim_offset(self) -> Tuple[int, int]:
        """
        Calculate offset between crosshair and target
        
        Returns:
            tuple: Offset (dx, dy)
        """
        if not self.target_position:
            return (0, 0)
        
        dx = self.target_position[0] - self.crosshair_position[0]
        dy = self.target_position[1] - self.crosshair_position[1]
        
        return (dx, dy)
    
    def smooth_movement(self, target: Tuple[int, int]) -> Tuple[int, int]:
        """
        Apply smoothing to movement
        
        Args:
            target: Target position
            
        Returns:
            tuple: Smoothed position
        """
        current = np.array(self.crosshair_position, dtype=float)
        target = np.array(target, dtype=float)
        
        smoothed = current * (1 - self.smoothing) + target * self.smoothing
        return tuple(smoothed.astype(int))
    
    def start_tracking(self):
        """
        Start aim tracking
        """
        self.is_tracking = True
        logger.info("Aim tracking started")
    
    def stop_tracking(self):
        """
        Stop aim tracking
        """
        self.is_tracking = False
        logger.info("Aim tracking stopped")
