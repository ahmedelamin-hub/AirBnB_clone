#!/usr/bin/python3
"""innit initialization"""
from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
