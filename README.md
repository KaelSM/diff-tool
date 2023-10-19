# Diff-Tool: Comprehensive Text File Comparison

Diff-Tool is an innovative utility designed for contrasting two text files, providing a detailed, user-friendly visualization of differences. The tool generates an HTML file highlighting the discrepancies, enabling users to navigate and understand changes efficiently. This functionality is particularly beneficial for reviewing extensive files or SQL queries, streamlining the creation of seed files.

## Features

- **Intuitive Interface:** Highlights differences in a color-coded format.
- **Navigation Aid:** Scroll through changes using navigational prompts.
- **Change Log Download:** Offers the option to download a record of alterations.
- **Seed File Generation:** Simplifies the creation of seed files based on the differences noted.

## Getting Started

### Prerequisites

- Python 3.x
- Any modern web browser (for viewing the output HTML)

### Installation

Clone the repository to your local machine:
```
git clone https://github.com/KaelSM/diff-tool.git
```

### Usage

To compare two files and view the differences in the console:
```
ython3 diff_tool.py oldText.txt newText.txt
```
To generate an HTML file that visualizes the differences:
```
python3 diff_tool.py oldText.txt newText.txt --html output.html
```
Open the generated `output.html` in a web browser to view the highlighted differences.

## Upcoming Enhancements (To-do)

- [ ] Implement a split-view display for side-by-side text comparison.
- [ ] Introduce interactive text highlights to pinpoint differences.
- [ ] Add scrollable buttons for seamless navigation through changes.
- [ ] Enable the download of a comprehensive change log.
- [ ] Incorporate navigational buttons to jump between changes.
- [ ] Facilitate the generation of seed files from identified differences.

## Contribution

We encourage community participation and contribution to this project. Please see [CONTRIBUTING.md](#) for more details on submitting pull requests. For major changes, please open an issue first to discuss what you would like to improve.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/KaelSM/diff-tool/blob/main/LICENSE) file for details.

## Contact

For any inquiries or issues, please open an issue on the [issues page](https://github.com/KaelSM/diff-tool/issues) of this repository.
