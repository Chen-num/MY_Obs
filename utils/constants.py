#!/usr/bin/env python3
"""
Constants Module
Defines application-wide constants
"""

from enum import Enum

# Application Info
APP_NAME = "MY_Obs"
APP_VERSION = "0.1.0"
APP_AUTHOR = "Chen-num"

# OBS Settings
DEFAULT_OBS_HOST = "localhost"
DEFAULT_OBS_PORT = 4444

# Crosshair Settings
DEFAULT_CROSSHAIR_SIZE = 20
DEFAULT_CROSSHAIR_COLOR = "#00FF00"

# Tracking Settings
DEFAULT_SENSITIVITY = 1.0
DEFAULT_SMOOTHING = 0.7
MAX_TRACKING_DISTANCE = 500

# Performance
DEFAULT_FPS_LIMIT = 60
UPDATE_INTERVAL = 16  # milliseconds (approximately 60 FPS)


class GameProfile(Enum):
    """
    Supported game profiles
    """
    VALORANT = "valorant"
    CS2 = "cs2"
    APEX = "apex"
    OW2 = "ow2"
    R6S = "r6s"
