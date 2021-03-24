import pyperclip
import re

# Create phone regex
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|\.)?                      # separator
    (\d{3})                         # first 3 digits
    (\s|-|\.)?                      # separator
    (\d{4})                         # first 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
    )''', re.VERBOSE)

#TODO Create email regex

#TODO Find matches in clipboard text

#TODO Copy results to the clipboard