'''
 'digits': ?,
 'non-digits': ?,
 'whitespaces': ?,
 'words': ?
Use regular expressions and the findall function to implement a function
count_chars that returns a dictionary with the counts of the number
of digits, non-digit characters, whitespace characters and words in a string.
The format of the dictionary is
{’digits’: #digits, ’non-digits’: #non-digits, ’whitespaces’: #whitespaces,
’words’: #words}.
Example
If s is ’There are 356 days in a year’, then count_chars(s) should return
the dic-tionary {’digits’: 3, ’non-digits’: 25, ’whitespaces’: 6, ’words’: 7}.
'''
import re


def count_chars(s: str) -> dict:
    digit = len(re.findall(r"\d", s))
    non_digit = len(re.findall(r"\D", s))
    whitespaces = len(re.findall(r"\s", s))
    words = len(re.findall(r"\w+", s))

    return {
        'digits': digit,
        'non_digits': non_digit,
        'whitespaces': whitespaces,
        'words': words
    }


# ([\w.]+)@([\w.]+)\.(\w+)
# print(count_chars('There are 356 days in a year'))
'''
Use regular expressions to implement a function email_splitter that takes
as input a string. The function returns a list of the email
addresses found in the input string such that each email address is split
into user id, domain and suffix.
Note: assume that any email address has the format of one
or more alphanumeric characters and/or dots (.) followed by @
followed by one or more alphanumeric characters followed
by a dot (.) followed by two or three alphanumeric characters.
Example
If s is ’john@doe.com smit.john@work.nu text’, then email_splitter(s)
should return the list [ (’john’, ’doe’, ’com’), (’smit.john’, ’work’, ’nu’)].
'''
email = 'john@doe.com smit.john@work.nu text'
# email_splitter = re.findall(r"([\w.]+)@([\w.]+)\.(\w+)", email)
# print(email_splitter)


def email_splitter(s: str) -> list:
    return re.findall(r"([\w.]+)@([\w.]+)\.(\w+)", s)


# print(email_splitter('john@doe.com smit.john@work.nu text'))


'''
Use regular expressions to implement a function find_words_with_first_letter
that takes as inputs a letter and a text. The function return a list
that contains all the words starting with a given letter case insensitive
form a given text.
Example
If s is ’Alice in amazing America goes class is all the way’, then calling the 
function find_words_with_first_letter(’a’, s) should return the list [ ’Alice’, 
’amazing’, ’America’, ’all’]
'''


def find_words_with_first_letter(s: str) -> list:
    return re.findall(r'\b[Aa]\w*', s)


'''
Use regular expressions to implement a function get_html_text
that given a text that represents an html page, it removes
all the tags and returns the text (inside the body if there is a body tag).
Example
Calling the function get_html_text(s) where:
•s = ’This is <em>emphasized</em> text’ should return ’This is emphasized
text’, while
•s = ’<html><head><title>A Title</title></head><body><h1>My page</h1><p
>Let me refer you to <a href ="...">here</a></body></html>’ should return
’My pageLet me refer you to here’.
'''


def get_html_text(s: str) -> str:
    # Step 1: extract body if it exists
    body_match = re.search(r'<body.*?>(.*?)</body>', s, re.DOTALL)

    if body_match:
        s = body_match.group(1)  # take only body content

    # Step 2: remove all HTML tags
    text = re.sub(r'<.*?>', '', s)

    return text


''' Questions on Files, JSON, and Exceptions'''

import json


def get_keys(filename: str):
    try:
        # Step 1: open file
        with open(filename, 'r') as f:
            data = json.load(f)

        # Step 2: check if dictionary has keys
        if not data:
            raise KeyError

        # Step 3: return list of keys
        return list(data.keys())

    except FileNotFoundError:
        print(f'Oops! file "{filename}" not found')

    except KeyError:
        print(f'Oops! no keys in "{filename}"')


print(get_keys("file1.json"))


def log_json_keys(json_file: str, log_file: str):
    try:
        keys = get_keys(json_file)

        # write keys to file
        with open(log_file, 'w') as f:
            f.write(' '.join(keys))

    except FileNotFoundError:
        with open(log_file, 'w') as f:
            f.write('File not found')

    except KeyError:
        with open(log_file, 'w') as f:
            f.write('No keys found')


# print()
# text = 'Alice in amazing America goes class is all the way'
# capture = re.findall(r'^[a]([\w]+)')
