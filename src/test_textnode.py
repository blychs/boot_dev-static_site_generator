import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from util import split_nodes_delimiter


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_noteq(self):
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.TEXT)
        node4 = TextNode("This is another text node", TextType.TEXT)
        self.assertNotEqual(node2, node3)
        self.assertNotEqual(node3, node4)

    def test_url_eq(self):
        node = TextNode("This node has URL", TextType.LINK, "https://joda.com")
        node2 = TextNode("This node has URL",
                         TextType.LINK, "https://joda.com")
        node3 = TextNode("This node has URL",
                         TextType.LINK, "https://joda2.com")
        self.assertEqual(node, node2)
        self.assertNotEqual(node2, node3)


class TestHTMLNodeToTextNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE,
                        "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_text_to_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_out = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        for n in range(len(new_nodes)):
            self.assertEqual(new_nodes[n], expected_out[n])

    def test_text_to_italics(self):
        node = TextNode(
            "This is text with a _italic block_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        expected_out = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("italic block", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
        ]
        for n in range(len(new_nodes)):
            self.assertEqual(new_nodes[n], expected_out[n])


if __name__ == "__main__":
    unittest.main()
