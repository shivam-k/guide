# WildCards ('?' & '*')
"?" will replace any single character
"*" will replace any string of characters

--- "sudo rm" will remove system files and folders ---

"man [command]" will show the commands manual  #E-version of --help


---Navigation---
"find [file or directory]" will look inside c-directory   # find *.png
"locate [file or directory]" will look everywhere on the system  # locate *.png


---Pipe in Linux---
"locate *.png | more" page by page
"locate *.png | less" first page, navigate up and down

---File and Directory Handling---
"touch [file name]" craete empty file
"zip [archive.zip] [file]" create zip
"unzip [archive.zip]"


---File Content---
'echo "text" > [file.txt]' overwrite the "file.txt" with "text"
'echo "text" >> [file.txt]' appends the "text" in the "file.txt"
"cat [text file]" display Contents of a "text file" at the terminal
# cat [text file] | more; cat [text file] | less
"head [text file]" display first ten lines
"tail [text file]" last ten lines

'grep "pattern" [file]' search "pattern" inside "file"(text document)
'grep -r "pattern" [dir]' search "pattern" inside "dir"(directory)

"nano [text file]" text editor
"wc [text file]" word count
