# Python File Organizer

A beginner-friendly Python automation tool that automatically organizes files into folders based on their file types.

## Features

* Organizes files automatically
* Creates folders for different file types
* Supports images, videos, music, documents, Excel files, Python files, and ZIP files
* Moves unknown file types into an `Others` folder
* Simple and easy-to-use Python program

## Supported File Types

| Category  | File Types                      |
| --------- | ------------------------------- |
| Images    | `.jpg`, `.jpeg`, `.png`, `.gif` |
| Videos    | `.mp4`, `.mkv`, `.avi`, `.mov`  |
| Music     | `.mp3`, `.wav`, `.flac`         |
| Documents | `.pdf`, `.docx`, `.doc`, `.txt` |
| Excel     | `.xlsx`, `.xls`, `.csv`         |
| Python    | `.py`                           |
| ZIP Files | `.zip`, `.rar`, `.7z`           |

## How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

### 2. Download the project

Download or clone this repository.

### 3. Run the program

Open the terminal in the project folder and run:

```bash
python file_organizer.py
```

### 4. Enter the folder path

The program will ask:

```text
Enter the folder path:
```

Enter the path of the folder you want to organize.

## Example

Before:

```text
MyFolder/
├── photo.jpg
├── video.mp4
├── song.mp3
├── document.pdf
└── program.py
```

After running the program:

```text
MyFolder/
├── Images/
│   └── photo.jpg
├── Videos/
│   └── video.mp4
├── Music/
│   └── song.mp3
├── Documents/
│   └── document.pdf
└── Python/
    └── program.py
```

## Technologies Used

* Python
* `os`
* `shutil`

## Author

**Zikria Imran**

GitHub: [zikriaimranz-alt](https://github.com/zikriaimranz-alt)

## Note

Always test the program on a sample folder first, especially when organizing important files.

