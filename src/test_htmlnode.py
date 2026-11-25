import unittest
from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_html(self):
        node = HTMLNode("p", "This is a test", None, 
                        {"href": "https://www.google.com"})
        self.assertTrue(node)

    def test_prop_to_html(self):
        node = HTMLNode("p", "This is a test", None, 
                        {"href": "https://www.google.com", "name":"Test McTest"})
        test_prop = node.props_to_html()
        expected = ' href="https://www.google.com" name="Test McTest"'
        self.assertEqual(test_prop, expected)

    def test_prop_to_html2(self):
        node = HTMLNode("p", "This is a test", None, 
                        {"href": "https://www.google.com", "target": "_blank"})
        test_prop = node.props_to_html()
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(test_prop, expected)

    def test_empty_props(self):
        node = HTMLNode(props=None)
        self.assertEqual(node.props_to_html(), "")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "This is a link",{"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">This is a link</a>')

    def test_leaf_to_html_p_none(self):
        node = LeafNode(None, "Just a string")
        self.assertEqual(node.to_html(), "Just a string")
    
    def test_leaf_to_html_value_none(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_to_html_b(self):
        node = LeafNode("b", "Hello, world!")
        self.assertEqual(node.to_html(), "<b>Hello, world!</b>")

    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )