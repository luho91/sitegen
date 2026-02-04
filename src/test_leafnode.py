import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode(
            "a",
            "http://www.ilove.you",
            {
                "href": "\"https://www.get.fucked\"",
            },
        )
        self.assertEqual(node.to_html(), "<a href=\"https://www.get.fucked\">http://www.ilove.you</a>")


if __name__ == "__main__":
    unittest.main()
