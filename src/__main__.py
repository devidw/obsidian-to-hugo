import argparse
import os


def cli_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--hugo-content-dir",
        help="The hugo content directory path, the obsidian contents get placed.",
        type=str,
    )
    parser.add_argument(
        "--obsidian-vault-dir",
        help="The directory of the Obsidian vault you would like to process.",
        type=str,
    )
    args = parser.parse_args()
    return args


def dir_exists(directory):
    return os.path.isdir(directory)


def clear_hugo_content_dir(hugo_content_dir):
    """
    Delete the whole content directory.
    """
    import shutil

    shutil.rmtree(hugo_content_dir)
    os.mkdir(hugo_content_dir)


def copy_obsidian_vault_to_hugo_content_dir(obsidian_vault_dir, hugo_content_dir):
    """
    Copy all files and directories from the obsidian vault to the hugo content directory.
    """
    from distutils.dir_util import copy_tree

    copy_tree(obsidian_vault_dir, hugo_content_dir)


def process_content(hugo_content_dir):
    import os
    from wiki_links_processor import replace_wiki_links_helper

    for root, dirs, files in os.walk(hugo_content_dir):
        for file in files:
            if file.endswith(".md"):
                with open(os.path.join(root, file), "r") as f:
                    text = f.read()
                text = replace_wiki_links_helper(text)
                with open(os.path.join(root, file), "w") as f:
                    f.write(text)


def main():
    parser = argparse.ArgumentParser()
    args = cli_args()
    if not dir_exists(args.hugo_content_dir):
        parser.error("The hugo content directory does not exist.")
    if not dir_exists(args.obsidian_vault_dir):
        parser.error("The obsidian vault directory does not exist.")
    clear_hugo_content_dir(args.hugo_content_dir)
    copy_obsidian_vault_to_hugo_content_dir(
        args.obsidian_vault_dir, args.hugo_content_dir
    )
    process_content(args.hugo_content_dir)


if __name__ == "__main__":
    main()
