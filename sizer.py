#!/usr/bin/env python3
import sys
import os

def main():
    if len(sys.argv) != 2:
        print("Usage: sizer <filename>")
        sys.exit(1)
    file = sys.argv[1]
    size = get_bytes(file)
    if size:
        formatted_output = format(size)
        print(formatted_output)
        sys.exit(0)
    else:
        sys.exit(1)


def format(num_bytes):
    units = ["bytes", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", ]
    iterations = 0
    while num_bytes > 999:
        num_bytes /= 1000
        iterations += 1
    return f"{num_bytes} {units[iterations]}"


def get_bytes(file):
    try:
        file_size = os.path.getsize(file)
        return file_size
    except OSError as e:
        print(f"Error reading file: {e}")
        return None


if __name__ == "__main__":
    main()
