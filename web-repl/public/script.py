from obsidian_to_hugo.wiki_links_processor import replace_wiki_links
from pyodide import create_proxy
# import js


def process_handler(event) -> None:
    input_text = document.querySelector('#input').value
    output_text = replace_wiki_links(input_text)
    document.querySelector('#output').innerHTML = output_text

def setup():
	# Create a JsProxy for the callback function
	event_proxy = create_proxy(process_handler)

	# Set the listener to the callback
	el = document.querySelector('#input')
	el.addEventListener("input", event_proxy)

	# Initially call the callback
	process_handler(None)

setup()
