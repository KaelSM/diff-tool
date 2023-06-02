import argparse
import difflib
import sys

from pathlib import Path


def create_diff(old_file: Path, new_file: Path, html_output: Path = None):
    file1 = open(old_file, encoding='utf-8').readlines()
    file2 = open(new_file, encoding='utf-8').readlines()

    if html_output:
        delta = difflib.HtmlDiff().make_file(
            file1, file2, old_file, new_file)
        with open(html_output, 'w', encoding='utf-8') as f:
            f.write(delta)
    else:
        delta = difflib.unified_diff(file1, file2, old_file, new_file)
        sys.stdout.writelines(delta)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("old_file_version")
    parser.add_argument("new_file_version")
    parser.add_argument("--html", help="Specify the html output file")
    args = parser.parse_args()

    old_file = Path(args.old_file_version)
    new_file = Path(args.new_file_version)

    if args.html:
        html_output = Path(args.html)
    else:
        html_output = None

    create_diff(old_file, new_file, html_output)


if __name__ == '__main__':
    main()
