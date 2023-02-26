"""
Utilities to extract markdown marks from text and turn them into html marks.
"""

from typing import TypedDict, List
import re


Mark = TypedDict("Marks", {"md_mark": str, "text": str})


def get_md_marks(text: str) -> List[Mark]:
    """
    Get all markdown marks from the given text and return a list of them.
    Each list item is a dictionary with the following keys:
    - mark: the exact match
    - text: the extracted text
    """
    md_marks = []
    md_marks_regex = r"==([^=\n]+)=="
    for match in re.finditer(md_marks_regex, text):
        out = {
            "md_mark": match.group(),
        }

        out["text"] = match.group(1)

        md_marks.append(out)
    return md_marks


def md_marks_to_html_marks(md_mark: Mark) -> str:
    """
    Convert the markdown mark into an html mark.
    """
    html_mark = f'<mark>{md_mark["text"]}</mark>'
    return html_mark


def replace_md_marks(text: str) -> str:
    """
    Replace all markdown marks in the given text with html marks.
    """
    marks = get_md_marks(text)
    for mark in marks:
        html_mark = md_marks_to_html_marks(mark)
        text = text.replace(mark["md_mark"], html_mark)
    return text
