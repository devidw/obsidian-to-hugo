<h1 align=center>
<img src=https://raw.githubusercontent.com/devidw/obsidian-to-hugo/master/img/gopher-obsidian.png width=100 height=100>
<br>
Obsidian Vault to Hugo Content
</h1>

Lightweight, zero-dependency CLI written in Python to help us publish [obsidian](https://obsidian.md) notes with [hugo](https://gohugo.io). 

It only takes two arguments: The obsidian vault directory (`--obsidian-vault-dir`) and the hugo content directory (`--hugo-content-dir`).

```console
python -m obsidian_to_hugo --obsidian-vault-dir=<path> --hugo-content-dir=<path>
```

It takes care of the following steps:

- Clears hugo content directory (directory will be deleted and recreated)
- Copies obsidian vault contents into hugo content directory (`.obsidian` gets removed immediately after copying)
- Replaces obsidian wiki links (`[[wikilink]]`) with hugo shortcode links (`[wikilink]({{< ref "wikilink" >}})`)


## Replacement examples

| Obsidian | Hugo
| -------- | --------
| ![](https://raw.githubusercontent.com/devidw/obsidian-to-hugo/master/img/obsidian.png) | ![](https://raw.githubusercontent.com/devidw/obsidian-to-hugo/master/img/hugo.png)
| `[[/some/wiki/link]]` | `[/some/wiki/link]({{< ref "/some/wiki/link" >}})`
| `[[/some/wiki/link\|Some text]]` | `[Some text]({{< ref "/some/wiki/link" >}})`
| `[[/some/wiki/link/_index]]` | `[/some/wiki/link/]({{< ref "/some/wiki/link/" >}})`

> NOTE: For now, there is *no way to escape* obsidian wiki links. Every link
> will be replaced with a hugo link. The only way to get around this is changing
> the wiki link to don't match the exact sytax, for example by adding an
> [invisible space](https://en.wikipedia.org/wiki/Zero-width_space) (Obsidian will highlight the invisible character as a red dot).
> ![](https://raw.githubusercontent.com/devidw/obsidian-to-hugo/master/img/do-not-do-that.png)
> However, this still is really really *not* best
> practice, so if anyone wants to implement real escaping, [please do
> so](https://github.com/devidw/obsidian-to-hugo/pulls).


## Installation

```console
pip install obsidian_to_hugo
```


## Usage

```console
usage: __main__.py [-h] [--hugo-content-dir HUGO_CONTENT_DIR] [--obsidian-vault-dir OBSIDIAN_VAULT_DIR]

options:
  -h, --help            show this help message and exit
  --hugo-content-dir HUGO_CONTENT_DIR
                        Directory of your Hugo content directory, the obsidian notes should be processed into.
  --obsidian-vault-dir OBSIDIAN_VAULT_DIR
                        Directory of the Obsidian vault, the notes should be processed from.
```
