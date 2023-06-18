# Find Differences tool

This project is focused on comparing two txt files passed to it, and coming back with and html that will show the 
differences moving up and down with them and highlighting the main differences.

# To-do:
- [x] Created a python skeleton to start comparing and generating an html
- [x]  Added table to help understand the colors highlighted and how to navigate through the page
- [ ]  divide the page with the old and the new text
- [ ]  Add highlight text with the differences
- [ ]  Scrollable buttons to where the changes are 
- [ ]  able to download a text with all the changes
- [ ]  buttons to go to the previous and next change
- [ ]  able to download a seed file

# How to run

First is to just run the differences and show on the output

```bash
			python3 diff_tool.py oldText.txt newText.text 
```

Second is to be able to generate the html

```bash
			python3 diff_tool.py oldText.txt newText.txt --html output.html
```


### Usage

To help difference large files of text/queries and find the changes faster to simplify
making a seed file.

Right now is running on the basic functions, and just outputting one file showing some 
changes.

More to come soon.


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
