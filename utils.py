import requests
from fastai.vision.all import *
from fastai.vision.widgets import *
from pathlib import Path

def mkdir_aftercheck(path: Path) -> None:
    if not path.is_dir():
        try:
            path.mkdir()
        except Exception as e:
            print(e)


