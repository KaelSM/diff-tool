import argparse
import difflib
import sys

from pathlib import Path


def create_diff(old_file: Path, new_file:Path):
    file1 = open(old_file).readlines()
    file2 = open(new_file).readlines()

    delta = difflib.unified_diff(file1, file2, old_file, new_file)
    sys.stdout.writelines(delta)

def main():
    parser = argoarse.ArgumentParser()
    parser.add_argument('old_file_version')
    parser.add_argument('new_file_version')
    args = parser.parse_args()

    old_file = Path(args.old_file_version)
    new_file = Path(args.new_file_version)

    create_diff(old_file, new_file)


if __name__ == '__main__':
    main()