import unittest

from textnode import TextNode, TextType, text_node_to_html_node, split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes


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


    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )


    def test_split_links(self):
        node = TextNode(
            "Please go to [secure link](https://i.will.scam.you.ru) or u will [get scammed](https://this-is-safe.com)[get scammed](https://this-is-safe.com)",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Please go to ", TextType.TEXT),
                TextNode("secure link", TextType.LINK, "https://i.will.scam.you.ru"),
                TextNode(" or u will ", TextType.TEXT),
                TextNode("get scammed", TextType.LINK, "https://this-is-safe.com"),
                TextNode("get scammed", TextType.LINK, "https://this-is-safe.com"),
            ],
            new_nodes,
        )


    def test_split_madness(self):
        text = "**SOME** _body_ `once` ![told me](the.world.is) [gonna](roll.me) I ain't the sharpest **TOOL** in the _shed_"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("SOME", TextType.BOLD),
                TextNode(" ", TextType.TEXT),
                TextNode("body", TextType.ITALIC),
                TextNode(" ", TextType.TEXT),
                TextNode("once", TextType.CODE),
                TextNode(" ", TextType.TEXT),
                TextNode("told me", TextType.IMAGE, "the.world.is"),
                TextNode(" ", TextType.TEXT),
                TextNode("gonna", TextType.LINK, "roll.me"),
                TextNode(" I ain't the sharpest ", TextType.TEXT),
                TextNode("TOOL", TextType.BOLD),
                TextNode(" in the ", TextType.TEXT),
                TextNode("shed", TextType.ITALIC),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()
