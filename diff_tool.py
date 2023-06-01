import difflib
import sys

from pathlib import Path


def create_diff(old_file: Path, new_file:Path):
    file1 = open(old_file).readlines()
    file2 = open(new_file).readlines()

    delta = difflib.unified_diff(file1, file2, old_file, new_file)
    sys.stdout.writelines(delta)