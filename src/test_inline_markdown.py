import unittest
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
)

from textnode import TextNode, TextType


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an image ![image](https://image.png)"
        )
        self.assertEqual([("image", "https://image.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [link](https://google.com). This is a second link [second link](https://googles.com)"
        )
        self.assertListEqual(
            [
                ("link", "https://google.com"),
                ("second link", "https://googles.com"),
            ],
            matches,
        )

    def test_split_image(self):
        node = TextNode("Hello ![alt](url) World ![alt2](url2)", TextType.TEXT)
        self.assertListEqual(split_nodes_image([node]), [
            TextNode("Hello ", TextType.TEXT, None),
            TextNode("alt", TextType.IMAGE, "url"),
            TextNode(" World ", TextType.TEXT, None),
            TextNode("alt2", TextType.IMAGE, "url2"),
        ])

    def test_split_link(self):
        node = TextNode("Start [text](url) middle [text2](url2) end", TextType.TEXT)
        self.assertListEqual(split_nodes_link([node]), [
            TextNode("Start ", TextType.TEXT, None),
            TextNode("text", TextType.LINK, "url"),
            TextNode(" middle ", TextType.TEXT, None),
            TextNode("text2", TextType.LINK, "url2"),
            TextNode(" end", TextType.TEXT, None)
        ])

    def test_empty_alt(self):
        node = TextNode("Test ![](url)", TextType.TEXT)
        self.assertListEqual(split_nodes_image([node]), [
            TextNode("Test ", TextType.TEXT, None),
            TextNode("", TextType.IMAGE, "url")
        ])

    def test_split_image_single(self):
        node = TextNode("![image](https://www.example.COM/IMAGE.PNG)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([TextNode("image", TextType.IMAGE, "https://www.example.COM/IMAGE.PNG")], new_nodes)


if __name__ == "__main__":
    unittest.main()
