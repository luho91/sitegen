import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq1(self):
        hn = HTMLNode(props={"href": "click.this", "target": "your_mom"})
        self.assertEqual(hn.props_to_html(), f"href=\"click.this\" target=\"your_mom\"")

    
    def test_eq2(self):
        hn = HTMLNode(tag="a", value="nigger")
        self.assertIn("children: None", str(hn))


    def test_neq1(self):
        hn1 = HTMLNode(tag="ul", value="nigger", props={"style": None})
        hn2 = HTMLNode(tag="li", value="gigger", props={"nostyle": "all"})
        self.assertNotEqual(hn1, hn2)


if __name__ == "__main__":
    unittest.main()
