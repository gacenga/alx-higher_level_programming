#!/usr/bin/python3


"""function text_indentation"""


def text_indentation(text):
    """defines text_indentation"""
    delimiters = ['.', '?', ':']
    current_line = ""
    lines = []
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if text == None:
        raise TypeError("text must be a string")
    for char in text:
        current_line += char
        if char in delimiters:
            lines.append(current_line.strip())
            current_line = ""
    if current_line.strip():
        lines.append(current_line.strip())
    for i, line in enumerate(lines):
        print(line, end="\n\n" if i < len(lines) - 1 else "")
