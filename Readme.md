# Lan ClipBoard 
## Why use it - Who needs it

Sharing simple code and text while working in a group
can be hard. You can always work in collaboration using GitHub but sometimes you want to copy just a line or something small. Sure you can be hardcore and paste it on Pastebin but you can also be smart and use **Lan ClipBoard**.

## What is it

**Lan ClipBoard** is a simple python application designed for windows
It shares clipboard content with the press of a button across network
all you need to do is be connected in the same WiFi network.
> can also work on linux with a few changes

## How to use 

 1. Download the executable or the python files and open it
 2. Copy what you need into the clipboard
 3. Press windows + c to send your message to the network
 4. Everyone with an open instance of the program will receive it directly in their clipboard

## Build from source

- open the files in a virtual environment and install pyinstaller:

    `pip install pyinstaller`

- got to .spec file and change:


	> ~~['C:\\Users\\jim\\PycharmProjects\\lanclipboard\\custom.ico'~~

	To:

	> ['*%files_path%*\\\custom.ico']

	*don't forget to use double '\\\\'* 

-  Finally build the files with the new spec file
	open terminal and type
	`pyinstaller clipboardshare.spec`
- Binary file should be inside dist folder
