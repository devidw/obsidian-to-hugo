"""
Obsidian to Hugo CLI
"""

import argparse
import os
from .obsidian_to_hugo import ObsidianToHugo

__version__ = "0.1.0"

parser = argparse.ArgumentParser()

parser.add_argument(
    "--hugo-content-dir",
    help="Directory of your Hugo content directory, the obsidian notes should be processed into.",
    type=str,
)

parser.add_argument(
    "--obsidian-vault-dir",
    help="Directory of the Obsidian vault, the notes should be processed from.",
    type=str,
)


def main() -> None:
    """
    Main entry point of the CLI.
    """
    args = parser.parse_args()
    if not args.hugo_content_dir or not os.path.isdir(args.hugo_content_dir):
        parser.error("The hugo content directory does not exist.")
    if not args.obsidian_vault_dir or not os.path.isdir(args.obsidian_vault_dir):
        parser.error("The obsidian vault directory does not exist.")
    obsidian_to_hugo = ObsidianToHugo(
        obsidian_vault_dir=args.obsidian_vault_dir,
        hugo_content_dir=args.hugo_content_dir,
    )
    obsidian_to_hugo.process()


if __name__ == "__main__":
    main()
