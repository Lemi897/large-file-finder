#!/usr/bin/env python3

import os

def find_large_files(start_path, min_size_mb):
    min_size_bytes = min_size_mb * 1024 * 1024

    print(f"\nScanning for files larger than {min_size_mb} MB...\n")

    for root, dirs, files in os.walk(start_path):
        for file in files:
            try:
                file_path = os.path.join(root, file)
                size = os.path.getsize(file_path)

                if size >= min_size_bytes:
                    size_mb = size / (1024 * 1024)
                    print(f"{size_mb:.2f} MB  ->  {file_path}")

            except (PermissionError, FileNotFoundError):
                continue


if __name__ == "__main__":
    path = input("Enter directory to scan (e.g /home): ").strip()
    size = float(input("Minimum file size in MB: "))

    find_large_files(path, size)
