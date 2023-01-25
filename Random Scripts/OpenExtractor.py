"""OpenExtractor python class file.

Class outputs prompts to user in the command line for ease of use upon
initialization. Checks for dependencies.

Dependencies
------------
openpyxl
Python 3.4+
"""
import sys
import re
import os
import random


def _setup():
    """Initialize function.

    Performs setup via user input to the console via helper function.
    """
    starts = set(re.split(r',\s*',
                 input("Enter start words as a comma-separated list:\n").
                 lower()))
    terms = set(re.split(r',\s*',
                input("Enter end words as a comma-sperated list:\n").lower()))

    file_name = input("Enter path to spreadsheet file:\n").strip()
    sheet_name = input("\nEnter the name of the worksheet: ").strip()

    rows_to_scan = int(input("Num of rows to scan: "))
    col_number = int(input("Num column to scan (A=1, B=2, etc.): "))

    wb = xl.load_workbook(filename=file_name, read_only=True)
    ws = wb[sheet_name]

    output_dir = (os.path.expanduser("~/Desktop") + "/ExtractorOutput" +
                  str(random.randrange(1, 500)) + ".txt")
    file = None

    try:
        file = open(output_dir, 'a')

    except:
        print("Error creating file!")
        sys.exit()

    # print("\nRESULTS:")
    for row in ws.iter_rows(min_row=1, max_row=rows_to_scan, min_col=col_number,
                            max_col=col_number, values_only=True):
        if row[0] is not None:
            parsed_string = extractor(starts, terms, row[0])

            file.write(parsed_string + "\n")

    print("\nResults outputted to: {}".format(output_dir))


def extractor(starters, terminators, full_string):
    """Light-weight substring extraction function.

    Extracts sub-sentences from full sentences based a list of starting
    and terminating words. Starting word must be first word in the sentence.

    Start is inclusive, termination is exclusive.

    [Deprecated] O(l*m*n), where l is len of starters, m is len of terminators
    and n is num of words in the input sentence.

    [Current] O(n) speed: starters, terminators are hashed sets.

    Returns
    -------
    A substring of full_string
    Variable full_string if no starter word detected

    """
    parsed = full_string.split(" ", 1)

    # if the first word of the sentence is a start flag
    if parsed[0].lower() in starters:
        tmp = parsed[1]

        parsed.remove(parsed[1])
        parsed.extend(tmp.split(" "))

        finalString = ""

        for word in parsed:
            if word.lower() in terminators:
                # finalString += word # makes terminate inclusive(when enabled)
                return finalString

            finalString += (word + " ")

    return full_string
    # use .strip() if trailing/leading whitespace needs removal


if __name__ == "__main__":
    # Version Checking:
    py_version = sys.version_info

    if py_version[0] < 3 or (py_version[0] == 3 and py_version[1] < 4):
        print("Python version not up to date!")
        print("3.4+ required, {}.{} current".format(py_version[0], py_version[1]))
        print("Download from https://python.org")
        sys.exit("")

    # Dependency Checking:
    try:
        import openpyxl as xl

    except ImportError:
        print("Dependency package not installed!")
        print("Run \'pip install openpyxl\' to install.")
        print("See https://openpyxl.readthedocs.io/ for more info...")
        sys.exit("")

    # Checks passed, begin the program:
    _setup()
