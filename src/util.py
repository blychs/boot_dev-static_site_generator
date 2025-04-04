import pprint
from textnode import TextNode, TextType
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        split_node = node.text.split(delimiter)
        if len(split_node) % 2 == 0:
            raise ValueError(
                f"Invalid markdown, delimiter not closed in {node}")
        for count, split in enumerate(split_node):
            if split == "":
                continue
            if count % 2 == 0:
                new_nodes.append(TextNode(split, node.text_type))
            else:
                new_nodes.append(TextNode(split, text_type))
    return new_nodes


def extract_markdown_images(text):
    images = re.findall(r"!\[[^\]]*\]\([^\)]*\)", text)
    found_images = []
    for image in images:
        parsed_image = re.findall(r"[^(![)\(\)\[\]]+", image)
        found_images.append(tuple((parsed_image)))
    return found_images


def extract_markdown_links(text):
    links = re.findall(r"(?<!!)\[[^\]]*\]\([^\)]*\)", text)
    found_links = []
    for link in links:
        parsed_links = re.findall(r"[^(![)\(\)\[\]]+", link)
        found_links.append(tuple((parsed_links)))
    return found_links


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        parsed_nodes = re.split(r"((?<!!)\[[^\]]*\]\([^\)]*\))", node.text)
        for new_node in parsed_nodes:
            if new_node == "":
                continue
            if re.search(r"(?<!!)\[[^\]]*\]\([^\)]*\)", new_node):
                linktext = extract_markdown_links(new_node)[0]
                new_nodes.append(
                    TextNode(linktext[0], TextType.LINK, url=linktext[1]))
            else:
                new_nodes.append(TextNode(new_node, TextType.TEXT))
    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        parsed_nodes = re.split(r"(!\[[^\]]*\]\([^\)]*\))", node.text)
        for new_node in parsed_nodes:
            if new_node == "":
                continue
            elif re.search(r"!\[[^\]]*\]\([^\)]*\)", new_node):
                linktext = extract_markdown_images(new_node)[0]
                new_nodes.append(
                    TextNode(linktext[0], TextType.IMAGE, url=linktext[1]))
            else:
                new_nodes.append(TextNode(new_node, TextType.TEXT))
    return new_nodes


def text_to_nodes(text):
    node = TextNode(text, TextType.TEXT)
    nodes_bold = split_nodes_delimiter([node], '**', text_type=TextType.BOLD)
    nodes_italic = split_nodes_delimiter(nodes_bold, '_', TextType.ITALIC)
    nodes_code = split_nodes_delimiter(nodes_italic, '`', TextType.CODE)
    nodes_images = split_nodes_image(nodes_code)
    nodes_links = split_nodes_link(nodes_images)
    return nodes_links


def markdown_to_blocks(markdown):
    texts = re.split("\n\n+", markdown)
    lines = []
    for text in texts:
        _t = text.rstrip("\n").strip()
        if _t != "":
            lines.append(_t)
    return lines
