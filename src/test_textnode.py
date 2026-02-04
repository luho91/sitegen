import unittest

from textnode import TextNode, TextType, text_node_to_html_node, split_nodes_delimiter, extract_markdown_images, extract_markdown_links


class TestTextNode(unittest.TestCase):
    def test_eq1(self):
        n1 = TextNode("This is a text node", TextType.BOLD)
        n2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(n1, n2)


    def test_eq2(self):
        n1 = TextNode("This is a text node", TextType.BOLD, None)
        n2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(n1, n2)  
    

    def test_neq1(self):
        n1 = TextNode("This is a text", TextType.ITALIC)
        n2 = TextNode("This is a different text", TextType.ITALIC)
        self.assertNotEqual(n1, n2)


    def test_neq2(self):
        n1 = TextNode("abc", TextType.LINK, "http.com")
        n2 = TextNode("abc", TextType.TEXT, "http.com")
        self.assertNotEqual(n1, n2)


    def test_neq3(self):
        n1 = TextNode("def", TextType.IMAGE, None)
        n2 = TextNode("def", TextType.IMAGE, "google.com")
        self.assertNotEqual(n1, n2)

    
    def test_text(self):
        node = TextNode("this is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "this is a text node")


    def test_split_nodes_delimiter(self):
        nodes = [
            TextNode("_would you look_ at this?", TextType.ITALIC),
            TextNode("You are *fat*.", TextType.TEXT),
            TextNode("`this is all code`", TextType.CODE),
        ]

        new_nodes = split_nodes_delimiter(nodes, "*", TextType.BOLD)
        self.assertEqual(new_nodes[2], TextNode("fat", TextType.BOLD))

    
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)


if __name__ == "__main__":
    unittest.main()
