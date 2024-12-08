# Sizer - File Size Utility

## Overview
**Sizer** is a simple Python script that calculates and formats the size of a given file.

## Features
- **File Size Calculation:** Quickly determine the size of any file.
- **Size Formatting:** Converts byte counts into human-readable formats like KB, MB, GB, etc.

## Usage
To use `sizer`, run the script from the command line followed by the path to the file you want to check:

```sh
./sizer /path/to/your/file


Example:

sh

./sizer example.txt


Output:
If the file example.txt is 1234567 bytes, the output would be:

example.txt
1.234567 MB


Installation

    Clone the repository:
    sh

    git clone [your-github-repo-url-here]
    cd sizer

    Ensure Python 3 is installed on your system.
    Make the script executable (on Unix-like systems):
    sh

    chmod +x sizer


Requirements

    Python 3.x


Functions
main()

    Checks if the script is called with exactly one argument (the filename).
    Calls get_bytes() to retrieve the file size.
    Formats the size using format() and prints it.


format(num_bytes)

    Converts byte size into a human-readable format (e.g., KB, MB, GB).


get_bytes(file)

    Attempts to read the file size using os.path.getsize(). 
    Handles exceptions if the file cannot be read or does not exist.


License
[Choose a License - for example, MIT]

Contributions
Feel free to fork this project and submit pull requests. If you find any bugs or have suggestions for improvements, please open an issue.

Author

    Matthew Allison



Make sure to replace `[your-github-repo-url-here]` with the actual URL of your GitHub repository. Also, choose an appropriate license if you decide to make your project open-source.
