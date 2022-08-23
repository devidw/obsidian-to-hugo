"""
Utilities to process obsidian notes and convert them to hugo ready content files.
"""

import os
import shutil
from distutils.dir_util import copy_tree
from .wiki_links_processor import replace_wiki_links_helper


class ObsidianToHugo:
    """
    Process the obsidian vault and convert it to hugo ready content.
    """

    def __init__(
        self,
        obsidian_vault_dir: str,
        hugo_content_dir: str,
    ) -> None:
        self.obsidian_vault_dir = obsidian_vault_dir
        self.hugo_content_dir = hugo_content_dir

    def process(self) -> None:
        """
        Delete the hugo content directory and copy the obsidian vault to the
        hugo content directory, then process the content so that the wiki links
        are replaced with the hugo links.
        """
        self.clear_hugo_content_dir()
        self.copy_obsidian_vault_to_hugo_content_dir()
        self.process_content()

    def clear_hugo_content_dir(self) -> None:
        """
        Delete the whole content directory.
        NOTE: The folder itself gets deleted and recreated.
        """
        shutil.rmtree(self.hugo_content_dir)
        os.mkdir(self.hugo_content_dir)

    def copy_obsidian_vault_to_hugo_content_dir(self) -> None:
        """
        Copy all files and directories from the obsidian vault to the hugo content directory.
        """
        copy_tree(self.obsidian_vault_dir, self.hugo_content_dir)
        # We don't want to have the .obsidian folder in the hugo content directory.
        if os.path.isdir(os.path.join(self.hugo_content_dir, ".obsidian")):
            shutil.rmtree(os.path.join(self.hugo_content_dir, ".obsidian"))

    def process_content(self) -> None:
        """
        Looping through all files in the hugo content directory and replace the
        wiki links of each matching file.
        """
        for root, dirs, files in os.walk(self.hugo_content_dir):
            for file in files:
                if file.endswith(".md"):
                    with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                        text = f.read()
                    text = replace_wiki_links_helper(text)
                    with open(os.path.join(root, file), "w", encoding="utf-8") as f:
                        f.write(text)
