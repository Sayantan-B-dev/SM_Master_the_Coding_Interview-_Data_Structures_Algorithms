# root files
- > `.gitattributes`, its the git attributes file, used for line endings.
- > `.gitignore`, its the git ignore file, used for ignore files.
- > `README.md`, its the readme file, used for project description.

- > copy html into `input.txt`.

- > use `python _extract_data_from_input_html.py` to sanitize the html content from `input.txt` and create `output.txt`.
- > use `python _create_complete_folder_and_file_structure.py` to create a tree of the course from `output.txt`.
- > use `python _bulk_rename_to_remove_spaces.py`, its used for rename files in the project and to remove spaces from name.


- > use `_tree_for_the_entire_folder.py`, its used for get the entire project tree.
- > use `_stats_to_get_total_filecount_and_total_filesize.py` to get the file and their total consumed storage stats alongside with file count.

---

in both of the `_tree_for_the_entire_folder.py` and `_stats_to_get_total_filecount_and_total_filesize.py` files there are `EXCLUDE_EXTENSIONS` , `EXCLUDE_DIRS` , `EXCLUDED_FILE_NAMES` which you can toggle to control their output

---
- > ignore `full_folder_tree.txt`, its the entire project tree.
- > ignore `output.txt`, its the output of `extract_data.py`.

- > `python_file_tree.txt` contains all python project file location well structured

---
> Make sure to see the `full_folder_tree.txt` and `python_folder_tree.txt` to see overall file structure. 2nd one might help you with finding appropriate **python projects** that has been done in this repo.

---

```
{open all folder drop down in your udemy course, copy the div, paste it in index.html}

`index.html` -> 
`extract_data_from_input_html.py` -> 
`output.html ` -> 
`create_complete_folder_and_file_structure.py ` -> 
`bulk_rename_to_remove_spaces.py`
```
--- 
