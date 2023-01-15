import unittest
from obsidian_to_hugo import md_mark_processor


class MarksProcessorTestCase(unittest.TestCase):
    def test_get_md_marks(self):
        text = "==foo bar=="
        marks = md_mark_processor.get_md_marks(text)
        self.assertEqual(len(marks), 1)
        self.assertEqual(
            marks[0],
            {
                "md_mark": "==foo bar==",
                "text": "foo bar",
            },
        )

    def test_convert_md_mark(self):
        md_mark = md_mark_processor.get_md_marks("==foo bar==")[0]
        html_mark = md_mark_processor.md_marks_to_html_marks(md_mark)
        self.assertEqual(html_mark, '<mark>foo bar</mark>')

    def test_replace_md_marks(self):
        real_in = "==foo bar=="
        expected_out = "<mark>foo bar</mark>"
        real_out = md_mark_processor.replace_md_marks(real_in)
        self.assertEqual(real_out, expected_out)


if __name__ == "__main__":
    unittest.main()
