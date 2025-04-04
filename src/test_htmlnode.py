import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_exist(self):
        node = HTMLNode(tag='a', value='www.google.com', props={
            "href": "https://www.google.com", "target": "_blank",
        })
        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.google.com" target="_blank"'
        )

    def test_values(self):
        node = HTMLNode(tag='a', value='www.google.com', props={
            "href": "https://www.google.com", "target": "_blank",
        })
        self.assertEqual(node.tag, 'a')
        self.assertEqual(node.value, 'www.google.com')
        self.assertEqual(node.props['href'], 'https://www.google.com')
        self.assertEqual(node.props['target'], '_blank')

    def test_repr(self):
        node = HTMLNode(tag='a', value='test', props={
            "class": "primary"})
        self.assertEqual(node.__repr__(),
                         "HTMLNode(tag=a, value=test, children=None, props={'class': 'primary'}")

    def test_props_isempty(self):
        node = HTMLNode(tag='a', value='www.google.com')
        self.assertEqual(node.props_to_html(), "")

    def test_all_empty(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {
                        "href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_div(self):
        node = LeafNode("div", "My name")
        self.assertEqual(node.to_html(), "<div>My name</div>")

    def test_leaf_to_html_notag(self):
        node = LeafNode(None, "My name")
        self.assertEqual(node.to_html(), "My name")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(),
                         "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()
