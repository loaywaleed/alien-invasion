# utils.py
import os
import sys


def resource_path(relative_path):
    """
    Get the absolute path to a resource for PyInstaller.
    """
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)