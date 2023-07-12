"""Restore Notebook execution progress when a browser page is reloaded"""
from .extension import Extension
__version__ = "0.1.0"


def _jupyter_server_extension_points():
    return [{
        "module": "message_replay",
        "app": Extension
    }]
