# Large File Finder

A Python script to scan your Linux machine for large files, quickly locate them, and generate a report. Ideal for cleaning up storage or managing large files.

## Features
- Scans a folder and all subfolders
- Finds files larger than a specified size (in MB)
- Prints the file path and file size
- Ignores files it can’t access (permission errors)
- Generates a timestamped report for reference

## Installation
```bash
# Clone the repo
git clone git@github.com:Lemi897/large-file-finder.git
cd large-file-finder

# Make the script executable
chmod +x large_files.py

Usage

./large_files.py

    Enter the folder path to scan, e.g., /home

    Enter minimum file size in MB, e.g., 250

Example output:

345.22 MB  ->  /videos/movie1.mkv
512.10 MB  ->  /videos/movie2.mkv

Requirements

    Python 3.x

    No extra Python packages required
