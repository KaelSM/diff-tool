import argparse
import difflib
from pathlib import Path

#python3 diff_tool.py oldDB.txt newDB3Thursday.txt --html output.html

def create_diff(old_file: Path, new_file: Path, html_output: Path = None):
    file1_lines = old_file.read_text(encoding='utf-8').splitlines()
    file2_lines = new_file.read_text(encoding='utf-8').splitlines()

    differ = difflib.HtmlDiff()
    delta = differ.make_file(file1_lines, file2_lines, str(old_file), str(new_file))

    if html_output:
        with open(html_output, 'w', encoding='utf-8') as f:
            f.write(delta)
        print(f"Differences between the files have been saved to {html_output}.")
    else:
        print(delta)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("old_file_version")
    parser.add_argument("new_file_version")
    parser.add_argument("--html", help="Specify the HTML output file")
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
