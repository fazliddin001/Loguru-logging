import sys
from typing import Dict, Optional, Any

from loguru import logger
from settings import LOGGING


# This file should be imported to somewhere or else
# settings will not be loaded


def parse_settings(settings: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """
    Prepares the logging settings dictionary for Loguru.
    If 'path' is provided, it sets it as the sink; otherwise defaults to sys.stdout.

    :param settings: Logging configuration dict
    :return: Dictionary with 'sink' key set for Loguru, or None if input is invalid
    """
    if not settings:
        return None

    sink = settings.pop("path", sys.stdout)
    settings["sink"] = sink
    return settings


def register_loguru(settings: Dict[str, Any]) -> None:
    """
    Registers Loguru logging settings by passing configuration to logger.add().

    :param settings: Dictionary with log settings for Loguru's logger
    """
    try:
        logger.add(**settings)
    except Exception as e:
        logger.error(f"Failed to register logger settings: {e}")


# Register file logging settings
file_settings = parse_settings(LOGGING.get("file"))
if file_settings:
    register_loguru(file_settings)

# Register console logging settings
terminal_settings = parse_settings(LOGGING.get("terminal"))
if terminal_settings:
    register_loguru(terminal_settings)
