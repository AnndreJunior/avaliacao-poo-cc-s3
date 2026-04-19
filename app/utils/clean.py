import os
import subprocess


def clean():
    subprocess.call("cls" if os.name == "nt" else "clear")
