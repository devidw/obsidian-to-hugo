import unittest
from obsidian_to_hugo import wiki_links_processor


class TestWikiLinksProcessor(unittest.TestCase):
    def test_get_wiki_links(self):
        text = "[[foo]] [[bar|baz]]"
        links = wiki_links_processor.get_wiki_links(text)
        self.assertEqual(len(links), 2)
        self.assertEqual(
            links[0],
            {
                "wiki_link": "[[foo]]",
                "link": "foo",
                "text": "foo",
            },
        )
        self.assertEqual(
            links[1],
            {
                "wiki_link": "[[bar|baz]]",
                "link": "bar",
                "text": "baz",
            },
        )

    def test_build_hugo_links(self):
        extracted_links = [
            {"wiki_link": "[[foo]]", "link": "foo", "text": "foo"},
            {"wiki_link": "[[bar|baz]]", "link": "bar", "text": "baz"},
            {"wiki_link": "[[bar/_index|baz]]", "link": "bar/", "text": "baz"},
        ]
        links = wiki_links_processor.build_hugo_links(extracted_links)
        self.assertEqual(len(links), 3)
        self.assertEqual(links[0]["hugo_link"], '[foo]({{< ref "foo" >}})')
        self.assertEqual(links[1]["hugo_link"], '[baz]({{< ref "bar" >}})')
        self.assertEqual(links[2]["hugo_link"], '[baz]({{< ref "bar/" >}})')

    def test_replace_wiki_links(self):
        text = "[[foo]] [[bar|baz]]"
        links = wiki_links_processor.get_wiki_links(text)
        links = wiki_links_processor.build_hugo_links(links)
        replaced_text = wiki_links_processor.replace_wiki_links(text, links)
        self.assertEqual(
            replaced_text,
            '[foo]({{< ref "foo" >}}) [baz]({{< ref "bar" >}})',
        )

    def test_replace_wiki_links_helper(self):
        text = "[[foo]] [[bar|baz]]"
        replaced_text = wiki_links_processor.replace_wiki_links_helper(text)
        self.assertEqual(
            replaced_text,
            '[foo]({{< ref "foo" >}}) [baz]({{< ref "bar" >}})',
        )


if __name__ == "__main__":
    unittest.main()
