# Downloads Folder Organizer

This project helps you automatically organize the files in your "Downloads" folder into categorized subfolders based on file type. It's a simple script that makes it easier to manage files and keep your Downloads folder clean.

## Files

- **RunScript.vbs**: A Visual Basic Script (VBS) file that runs the Python scripts on Windows.
- **Runner.bat**: A Batch file to run the Python scripts on Windows, ensuring that the Python environment is correctly set up.
- **organize.py**: The main Python script that organizes files in the Downloads folder based on their extensions (e.g., images, documents, videos, etc.).
- **watch.pyw**: A Python script that continuously monitors your Downloads folder for new files and automatically organizes them when added.

## Prerequisites

Before using this project, make sure you have the following installed:

- Python 3.x
- Required Python libraries (see below)

## How to Use
# Method 1: Manual Run

Download the project files and place them in a directory on your computer.

- Open a terminal or command prompt.
- Navigate to the folder containing the scripts.
- Run the organize.py script manually by typing the following command:

```bash
python organize.py
```
This will organize all files in your "Downloads" folder based on their file type.

# Method 2: Automatic File Organization (Real-Time Monitoring)
To automatically organize files as they are added to your "Downloads" folder:

- Download the project files and place them in a directory on your computer.
- Open a terminal or command prompt.
- Navigate to the folder containing the scripts.
- Run the watch.pyw script:

```bash
pythonw watch.pyw
```
This script will keep running in the background and monitor your "Downloads" folder. Whenever a new file is added, it will be organized automatically.

# Method 3: Run Using Batch or VBS
If you prefer to run the scripts using a batch file or a VBS script:

- Use the Runner.bat file to run the Python scripts in a command prompt automatically.
- Alternatively, use RunScript.vbs to execute the Python script through the Windows Script Host.
