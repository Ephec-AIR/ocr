"""Wrapper around raspistill"""

from subprocess import run as subproc_run
from datetime import datetime
from pathlib import Path
from contextlib import contextmanager
from os import remove
from functools import partial

def capture(filepath):
    """Capture a image to the given path"""
    subproc_run(["raspistill", "-o", str(filepath)])

@contextmanager
def temp_capture():
    """Capture a temporary image, yield the path of the generated file"""
    filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.jpg")
    filepath = Path(Path.home(), "Pictures", filename)
    capture(filepath)
    yield filepath
    remove(filepath)
