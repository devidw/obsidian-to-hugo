"""
Utilities to extract wiki links from text and turn them into hugo links.
"""

import re


def get_wiki_links(text: str) -> list:
    """
    Get all wiki links from the given text and return a list of them.
    Each list item is a dictionary with the following keys:
    - wiki_link: the exact match
    - link: the extracted link
    - text: the possible extracted text
    """
    wiki_links = []
    wiki_link_regex = r"\[\[(.*?)\]\]"
    for match in re.finditer(wiki_link_regex, text):
        out = {
            "wiki_link": match.group(),
        }

        if "|" in match.group(1):
            out["link"], out["text"] = match.group(1).split("|")
        else:
            out["link"] = match.group(1)
            out["text"] = match.group(1)

        # if the link ends with `_index` remove it
        if out["link"].endswith("_index"):
            out["link"] = out["link"][:-6]

        wiki_links.append(out)
    return wiki_links


def build_hugo_links(links: list) -> list:
    """
    Extens the passed wiki links list by adding a dict key for the hugo link.
    """
    for link in links:
        link["hugo_link"] = f'[{link["text"]}]({{{{< ref "{link["link"]}" >}}}})'
    return links


def replace_wiki_links(text: str, links: list) -> str:
    """
    Replace all wiki links with hugo links in the given text.
    """
    for link in links:
        text = text.replace(link["wiki_link"], link["hugo_link"])
    return text


def replace_wiki_links_helper(text: str) -> str:
    """
    Helper function for replace_wiki_links.
    """
    links = get_wiki_links(text)
    links = build_hugo_links(links)
    return replace_wiki_links(text, links)
